from __future__ import annotations

import pandas as pd

from src.imdb_dashboard_data import load_imdb_movies
from src.visualizations.imdb_genre_rating_plot import save_genre_avg_rating_chart


def build_imdb_dataset() -> pd.DataFrame:
    df = load_imdb_movies().copy()
    df["primary_genre"] = df["PrimaryGenre"]
    return df


def create_genre_rating_chart(output_path: str = "outputs/imdb_avg_rating_by_genre.png") -> tuple[pd.DataFrame, str]:
    df = build_imdb_dataset()

    genre_stats = (
        df.groupby("primary_genre", as_index=False)
        .agg(movie_count=("Title", "count"), avg_rating=("Rating", "mean"))
        .query("movie_count >= 20")
        .sort_values("avg_rating", ascending=False)
    )
    genre_stats["avg_rating"] = genre_stats["avg_rating"].round(2)
    image_path = save_genre_avg_rating_chart(genre_stats, output_path=output_path)
    return genre_stats, image_path
