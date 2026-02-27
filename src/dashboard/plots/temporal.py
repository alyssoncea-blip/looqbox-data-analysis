from __future__ import annotations

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from src.dashboard.plots.common import dark_layout
from src.dashboard.styles import IMDB_YELLOW


def render_temporal(filtered: pd.DataFrame) -> None:
    t1, t2 = st.columns(2, gap="medium")
    yearly = filtered.groupby("Year", as_index=False).agg(avg_rating=("Rating", "mean"), releases=("Id", "count"))

    with t1:
        fig_rating_year = px.line(yearly, x="Year", y="avg_rating", markers=True, title="Average Rating Over Time")
        fig_rating_year.update_traces(line=dict(color=IMDB_YELLOW, width=3), marker=dict(color=IMDB_YELLOW))
        fig_rating_year.add_traces(
            go.Scatter(
                x=yearly["Year"],
                y=yearly["avg_rating"],
                fill="tozeroy",
                mode="none",
                fillcolor="rgba(245,197,24,0.20)",
                showlegend=False,
            )
        )
        dark_layout(fig_rating_year)
        st.plotly_chart(fig_rating_year, use_container_width=True)

    with t2:
        fig_release_year = px.bar(yearly, x="Year", y="releases", title="Movies Released per Year", color_discrete_sequence=[IMDB_YELLOW])
        dark_layout(fig_release_year)
        st.plotly_chart(fig_release_year, use_container_width=True)

