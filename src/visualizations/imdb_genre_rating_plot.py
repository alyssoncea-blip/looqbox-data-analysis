from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def save_genre_avg_rating_chart(
    genre_stats: pd.DataFrame,
    output_path: str = "outputs/imdb_avg_rating_by_genre.png",
) -> str:
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(9, 5.2))
    bars = ax.barh(genre_stats["primary_genre"], genre_stats["avg_rating"], color="#2F5597")
    ax.invert_yaxis()
    ax.set_title("IMDB: Average Rating by Primary Genre (min 20 movies)", fontsize=11, weight="bold")
    ax.set_xlabel("Average Rating")
    ax.set_ylabel("Primary Genre")
    ax.set_xlim(0, max(10, genre_stats["avg_rating"].max() + 0.5))

    for bar, value in zip(bars, genre_stats["avg_rating"]):
        ax.text(value + 0.05, bar.get_y() + bar.get_height() / 2, f"{value:.2f}", va="center", fontsize=8)

    plt.tight_layout()
    fig.savefig(output, dpi=220, bbox_inches="tight")
    plt.close(fig)
    return str(output.resolve())

