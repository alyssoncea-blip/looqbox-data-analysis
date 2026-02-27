from __future__ import annotations

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

from src.dashboard.plots.common import dark_layout


def render_advanced(filtered: pd.DataFrame) -> None:
    a1, a2 = st.columns(2, gap="medium")
    with a1:
        bubble_df = filtered.dropna(subset=["RevenueMillions", "Rating", "Votes"]).copy()
        bubble_df["log_votes"] = np.log10(bubble_df["Votes"].clip(lower=1))
        fig_rev_rating = px.scatter(
            bubble_df,
            x="RevenueMillions",
            y="Rating",
            size="log_votes",
            color="PrimaryGenre",
            hover_name="Title",
            title="Revenue vs Rating (bubble size = popularity)",
            size_max=24,
        )
        dark_layout(fig_rev_rating)
        st.plotly_chart(fig_rev_rating, use_container_width=True)

    with a2:
        dur_df = filtered.dropna(subset=["Runtime", "Rating"]).copy()
        fig_runtime = px.scatter(
            dur_df,
            x="Runtime",
            y="Rating",
            color="PrimaryGenre",
            hover_name="Title",
            title="Runtime vs Rating",
        )
        dark_layout(fig_runtime)
        st.plotly_chart(fig_runtime, use_container_width=True)

