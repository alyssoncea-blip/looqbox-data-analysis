from __future__ import annotations

from pathlib import Path

from src.db_utils import get_connection, read_sql_df


def read_sql(path: str) -> str:
    return Path(path).read_text(encoding="utf-8", errors="ignore")


def main() -> int:
    output_dir = Path("outputs")
    output_dir.mkdir(parents=True, exist_ok=True)

    jobs = [
        (
            "sql/part1/01_top_10_produtos_mais_caros.sql",
            output_dir / "q1_top_10_most_expensive_products.csv",
        ),
        (
            "sql/part1/02_secoes_departamentos_bebidas_padaria.sql",
            output_dir / "q2_sections_bebidas_padaria.csv",
        ),
        (
            "sql/part1/03_total_vendas_por_area_q1_2019.sql",
            output_dir / "q3_total_sales_by_business_area_q1_2019.csv",
        ),
    ]

    with get_connection() as conn:
        for sql_path, out_path in jobs:
            df = read_sql_df(conn, read_sql(sql_path))
            df.to_csv(out_path, index=False)
            print(f"Saved: {out_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
