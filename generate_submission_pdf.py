from __future__ import annotations

import textwrap
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages

from src.case1_dynamic_query import retrieve_data
from src.case2_client_visualization import build_tm_table
from src.db_utils import get_connection, read_sql_df
from src.imdb_visualization import create_genre_rating_chart


OUTPUT_PDF = Path("outputs/looqbox_challenge_submission.pdf")


def read_text(path: str) -> str:
    return Path(path).read_text(encoding="utf-8", errors="ignore")


def add_cover(pdf: PdfPages) -> None:
    fig = plt.figure(figsize=(8.27, 11.69))  # A4 portrait
    ax = fig.add_subplot(111)
    ax.axis("off")
    ax.text(0.5, 0.9, "Looqbox Data Challenge", ha="center", va="top", fontsize=18, weight="bold")
    ax.text(0.5, 0.85, "Technical Submission (SQL + Python + Visualization)", ha="center", va="top", fontsize=11)
    ax.text(
        0.1,
        0.76,
        "Contents:\n"
        "1. SQL queries and results\n"
        "2. Case 1 - Dynamic function retrieve_data\n"
        "3. Case 2 - Fixed queries + TM visualization\n"
        "4. IMDB visualization\n",
        ha="left",
        va="top",
        fontsize=10,
    )
    pdf.savefig(fig, bbox_inches="tight")
    plt.close(fig)


def add_code_page(pdf: PdfPages, title: str, code_text: str) -> None:
    fig = plt.figure(figsize=(8.27, 11.69))
    ax = fig.add_subplot(111)
    ax.axis("off")
    ax.text(0.03, 0.98, title, ha="left", va="top", fontsize=12, weight="bold")

    wrapped = []
    for line in code_text.splitlines():
        parts = textwrap.wrap(line, width=96, break_long_words=False, break_on_hyphens=False)
        wrapped.extend(parts if parts else [""])
    code_block = "\n".join(wrapped[:145])  # keep one-page readability

    ax.text(0.03, 0.95, code_block, ha="left", va="top", fontsize=7.6, family="monospace")
    pdf.savefig(fig, bbox_inches="tight")
    plt.close(fig)


def add_table_page(pdf: PdfPages, title: str, df: pd.DataFrame, max_rows: int = 25) -> None:
    show = df.head(max_rows).copy()

    fig_h = max(4.8, 0.32 * len(show) + 1.8)
    fig = plt.figure(figsize=(8.27, min(fig_h, 11.69)))
    ax = fig.add_subplot(111)
    ax.axis("off")
    ax.text(0.03, 0.98, title, ha="left", va="top", fontsize=12, weight="bold")

    for c in show.columns:
        if pd.api.types.is_float_dtype(show[c]):
            show[c] = show[c].map(lambda x: f"{x:.2f}")

    table = ax.table(
        cellText=show.values,
        colLabels=list(show.columns),
        bbox=[0.03, 0.03, 0.94, 0.9],
        cellLoc="left",
        colLoc="left",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    table.scale(1, 1.05)

    for (r, _c), cell in table.get_celld().items():
        cell.set_edgecolor("#DDDDDD")
        cell.set_linewidth(0.4)
        if r == 0:
            cell.set_facecolor("#F5F5F5")
            cell.set_text_props(weight="bold")
        else:
            cell.set_facecolor("#F9F9F9" if r % 2 == 0 else "white")

    pdf.savefig(fig, bbox_inches="tight")
    plt.close(fig)


def add_image_page(pdf: PdfPages, title: str, image_path: Path) -> None:
    fig = plt.figure(figsize=(8.27, 11.69))
    ax = fig.add_subplot(111)
    ax.axis("off")
    ax.text(0.03, 0.98, title, ha="left", va="top", fontsize=12, weight="bold")

    img = plt.imread(str(image_path))
    ax.imshow(img)
    ax.set_position([0.03, 0.05, 0.94, 0.88])
    ax.axis("off")

    pdf.savefig(fig, bbox_inches="tight")
    plt.close(fig)


def sql_results() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    q1 = read_text("sql/part1/01_top_10_produtos_mais_caros.sql")
    q2 = read_text("sql/part1/02_secoes_departamentos_bebidas_padaria.sql")
    q3 = read_text("sql/part1/03_total_vendas_por_area_q1_2019.sql")
    with get_connection() as conn:
        return read_sql_df(conn, q1), read_sql_df(conn, q2), read_sql_df(conn, q3)


def main() -> int:
    OUTPUT_PDF.parent.mkdir(parents=True, exist_ok=True)

    # Ensure all outputs exist and are current.
    case1_df = retrieve_data(18, 1, ["2019-01-01", "2019-01-31"])
    case2_df = build_tm_table(["2019-10-01", "2019-12-31"])
    _, imdb_chart = create_genre_rating_chart("outputs/imdb_avg_rating_by_genre.png")
    sql1, sql2, sql3 = sql_results()

    with PdfPages(OUTPUT_PDF) as pdf:
        add_cover(pdf)

        # SQL
        add_code_page(pdf, "Part 1 - SQL Code Snippets", read_text("sql/part1/01_top_10_produtos_mais_caros.sql"))
        add_code_page(pdf, "Part 1 - SQL Code Snippets (cont.)", read_text("sql/part1/02_secoes_departamentos_bebidas_padaria.sql"))
        add_code_page(pdf, "Part 1 - SQL Code Snippets (cont.)", read_text("sql/part1/03_total_vendas_por_area_q1_2019.sql"))
        add_table_page(pdf, "SQL Result - Top 10 Most Expensive Products", sql1, max_rows=10)
        add_table_page(pdf, "SQL Result - Sections for BEBIDAS and PADARIA", sql2, max_rows=20)
        add_table_page(pdf, "SQL Result - Sales by Business Area (Q1 2019)", sql3, max_rows=10)

        # Case 1
        add_code_page(pdf, "Case 1 - Python Function (retrieve_data)", read_text("src/case1_dynamic_query.py"))
        add_table_page(pdf, "Case 1 Result - data_product_sales sample", case1_df, max_rows=31)

        # Case 2
        add_code_page(pdf, "Case 2 - Fixed Queries + Processing", read_text("src/case2_client_visualization.py"))
        add_table_page(pdf, "Case 2 Result Table - Loja/Categoria/TM", case2_df, max_rows=20)
        add_image_page(pdf, "Case 2 Visualization (PNG)", Path("outputs/case2_tm_table.png"))

        # IMDB
        add_code_page(pdf, "IMDB Visualization - Python Code", read_text("src/imdb_visualization.py"))
        add_image_page(pdf, "IMDB Visualization Result", Path(imdb_chart))

    print(f"PDF generated: {OUTPUT_PDF.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
