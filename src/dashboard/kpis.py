from __future__ import annotations

import pandas as pd
import streamlit as st


def _kpi_card(label: str, value: str) -> None:
    st.markdown(
        f"""
        <div class="kpi-card">
          <div class="kpi-label">{label}</div>
          <div class="kpi-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_kpis(filtered: pd.DataFrame) -> None:
    top_movie = filtered.sort_values(["Rating", "Votes"], ascending=[False, False]).iloc[0]
    most_freq_genre = filtered["PrimaryGenre"].value_counts().idxmax()
    c1, c2, c3, c4 = st.columns(4, gap="medium")
    with c1:
        _kpi_card("Total movies", f"{len(filtered):,}")
    with c2:
        _kpi_card("Average rating", f"{filtered['Rating'].mean():.2f}")
    with c3:
        _kpi_card("Top rated movie", f"{top_movie['Title']} ({top_movie['Rating']:.1f})")
    with c4:
        _kpi_card("Most frequent genre", most_freq_genre)

