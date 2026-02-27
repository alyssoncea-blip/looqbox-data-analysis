from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.font_manager import FontProperties
from matplotlib.text import Text


def save_tm_table_visual(
    tm_df: pd.DataFrame,
    output_path: str = "outputs/case2_tm_table.png",
    period_text: str = "Periodo: 2019-10-01 a 2019-12-31",
) -> str:
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    fig_height = max(4.8, 0.33 * len(tm_df) + 0.9)
    fig, ax = plt.subplots(figsize=(5.8, fig_height))
    fig.patch.set_facecolor("white")
    ax.axis("off")

    show_df = tm_df.copy()
    show_df["TM"] = show_df["TM"].map(lambda x: f"{x:.2f}")

    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    font = FontProperties(size=8.7)

    def text_width_px(value: str) -> float:
        txt = Text(0, 0, value, fontproperties=font)
        txt.set_figure(fig)
        bbox = txt.get_window_extent(renderer=renderer)
        return bbox.width

    columns = ["Loja", "Categoria", "TM"]
    padding_px = 8.0
    col_px = []
    for col in columns:
        values = [col, *show_df[col].astype(str).tolist()]
        max_width = max(text_width_px(v) for v in values)
        col_px.append(max_width + padding_px)

    total_content_px = sum(col_px)
    target_width_in = max(3.8, min(6.2, (total_content_px + 20.0) / fig.dpi))
    fig.set_size_inches(target_width_in, fig_height, forward=True)
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()

    axes_width_px = ax.get_window_extent(renderer=renderer).width
    total_table_frac = min(0.995, total_content_px / axes_width_px)
    col_widths = [(w / total_content_px) * total_table_frac for w in col_px]

    ax.text(0.5, 0.99, period_text, transform=ax.transAxes, ha="center", va="top", fontsize=9, color="black")

    table = ax.table(
        cellText=show_df.values,
        colLabels=["Loja", "Categoria", "TM"],
        bbox=[(1.0 - total_table_frac) / 2.0, 0.02, total_table_frac, 0.93],
        cellLoc="left",
        colLoc="left",
        colWidths=col_widths,
    )
    table.auto_set_font_size(False)
    table.set_fontsize(8.7)
    table.scale(1, 1.0)

    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#DDDDDD")
        cell.set_linewidth(0.4)
        if row == 0:
            cell.set_text_props(weight="normal", color="black", ha="center")
            cell.set_facecolor("#FAFAFA")
            cell.get_text().set_ha("center")
        else:
            cell.set_facecolor("#F2F2F2" if row % 2 == 0 else "white")
            cell.get_text().set_color("black")
            if col == 2:
                cell.get_text().set_ha("right")
            else:
                cell.get_text().set_ha("left")

    plt.tight_layout(pad=0.02)
    fig.savefig(output, dpi=200, bbox_inches="tight", pad_inches=0)
    plt.close(fig)
    return str(output.resolve())

