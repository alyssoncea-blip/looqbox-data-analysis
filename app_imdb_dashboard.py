from __future__ import annotations

import pandas as pd
import streamlit as st

from src.dashboard.charts import (
    render_advanced,
    render_genre,
    render_genre_range_metrics,
    render_rating_distribution,
    render_temporal,
)
from src.dashboard.filters import render_filter_panel
from src.dashboard.kpis import render_kpis
from src.dashboard.styles import apply_theme, render_header, section_title
from src.dashboard.top_movies import render_cinematic_top10
from src.imdb_dashboard_data import load_imdb_movies


def main() -> None:
    apply_theme()
    render_header()

    @st.cache_data(show_spinner=False)
    def get_data() -> pd.DataFrame:
        return load_imdb_movies()

    movies = get_data()
    min_year, max_year = int(movies["Year"].min()), int(movies["Year"].max())
    genre_options = sorted([g for g in movies["PrimaryGenre"].dropna().unique() if g != ""])
    max_votes = int(movies["Votes"].fillna(0).max())

    year_range, selected_genres, min_votes = render_filter_panel(min_year, max_year, genre_options, max_votes)

    filtered = movies[
        (movies["Year"].between(year_range[0], year_range[1]))
        & (movies["PrimaryGenre"].isin(selected_genres))
        & (movies["Votes"].fillna(0) >= min_votes)
    ].copy()

    if filtered.empty:
        st.warning("No records found with current filters.")
        return

    render_kpis(filtered)

    section_title("Top Movies")
    top10 = (
        filtered.sort_values(["Rating", "Votes"], ascending=[False, False])[["Title", "Rating", "Year", "Runtime", "Votes", "Genre"]]
        .head(10)
    )
    render_cinematic_top10(top10)

    section_title("Genre Analytics")
    render_genre(filtered)

    st.markdown("### Rating Distribution")
    render_rating_distribution(filtered)

    section_title("Temporal Trends")
    render_temporal(filtered)

    section_title("Additional Views")
    render_genre_range_metrics(filtered)

    section_title("Advanced Views")
    render_advanced(filtered)


if __name__ == "__main__":
    main()
