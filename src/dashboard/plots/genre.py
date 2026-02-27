from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st

from src.dashboard.plots.common import dark_layout
from src.dashboard.styles import IMDB_YELLOW
from src.imdb_dashboard_data import explode_genres


def render_genre(filtered: pd.DataFrame) -> None:
    g1, g2 = st.columns(2, gap="medium")
    genres_exploded = explode_genres(filtered)
    genre_stats = genres_exploded.groupby("Genre", as_index=False).agg(movie_count=("Id", "count"), avg_rating=("Rating", "mean"))
    genre_count_stats = genre_stats.sort_values("movie_count", ascending=False).head(12)
    genre_rating_stats = (
        genre_stats[genre_stats["movie_count"] >= 5]
        .sort_values("avg_rating", ascending=False)
        .head(12)
        .sort_values("avg_rating", ascending=True)
    )

    with g1:
        dist_height = max(360, min(680, 36 * len(genre_count_stats)))
        fig_genre_dist = px.bar(
            genre_count_stats.sort_values("movie_count", ascending=True),
            x="movie_count",
            y="Genre",
            orientation="h",
            title="Movies by Genre",
            text=genre_count_stats.sort_values("movie_count", ascending=True)["movie_count"].astype(int).astype(str),
            color_discrete_sequence=[IMDB_YELLOW],
        )
        fig_genre_dist.update_traces(
            textposition="auto",
            cliponaxis=False,
            hovertemplate="<b>%{y}</b><br>Movies: %{x}<extra></extra>",
        )
        fig_genre_dist.update_layout(
            xaxis_title="Movies",
            yaxis_title="Genre",
            height=dist_height,
            bargap=0.22,
            margin=dict(l=10, r=20, t=52, b=10),
            yaxis=dict(automargin=True),
            xaxis=dict(automargin=True),
        )
        dark_layout(fig_genre_dist)
        st.plotly_chart(fig_genre_dist, use_container_width=True)

    with g2:
        chart_height = max(360, min(680, 36 * len(genre_rating_stats)))
        fig_genre_rating = px.bar(
            genre_rating_stats,
            x="avg_rating",
            y="Genre",
            orientation="h",
            title="Average Rating by Genre",
            text=genre_rating_stats["avg_rating"].map(lambda v: f"{v:.2f}"),
            color_discrete_sequence=[IMDB_YELLOW],
        )
        fig_genre_rating.update_traces(
            textposition="auto",
            cliponaxis=False,
            hovertemplate="<b>%{y}</b><br>Average Rating: %{x:.2f}<extra></extra>",
        )
        fig_genre_rating.update_layout(
            xaxis_title="Average Rating",
            yaxis_title="Genre",
            height=chart_height,
            bargap=0.22,
            margin=dict(l=10, r=20, t=52, b=10),
            yaxis=dict(categoryorder="total ascending", automargin=True),
            xaxis=dict(automargin=True),
        )
        dark_layout(fig_genre_rating)
        st.plotly_chart(fig_genre_rating, use_container_width=True)
