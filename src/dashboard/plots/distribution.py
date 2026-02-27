from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st

from src.dashboard.plots.common import dark_layout
from src.dashboard.styles import IMDB_YELLOW


def render_rating_distribution(filtered: pd.DataFrame) -> None:
    hist = px.histogram(
        filtered,
        x="Rating",
        nbins=20,
        title="Distribution of Ratings",
        color_discrete_sequence=[IMDB_YELLOW],
    )
    dark_layout(hist)
    st.plotly_chart(hist, use_container_width=True)

