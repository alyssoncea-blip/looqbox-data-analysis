from __future__ import annotations

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from src.dashboard.plots.common import dark_layout
from src.dashboard.styles import IMDB_YELLOW


def _summary_stats(df: pd.DataFrame, value_col: str, top_n: int = 10) -> pd.DataFrame:
    summary = (
        df.groupby("GenreCombo", as_index=False)[value_col]
        .agg(min_value="min", mean_value="mean", max_value="max", movie_count="count")
        .sort_values(["mean_value", "movie_count"], ascending=[False, False])
        .head(top_n)
    )
    summary["GenreComboLabel"] = summary["GenreCombo"].astype(str).str.replace(",", ",<br>", regex=False)
    return summary.iloc[::-1].reset_index(drop=True)


def _range_marker_fig(stats: pd.DataFrame, title: str, y_title: str) -> go.Figure:
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=stats["GenreComboLabel"],
            y=stats["max_value"] - stats["min_value"],
            base=stats["min_value"],
            marker=dict(color="rgba(245,197,24,0.35)"),
            hovertemplate="<b>%{x}</b><br>Min: %{base:.2f}<br>Max: %{customdata:.2f}<extra></extra>",
            customdata=stats["max_value"],
            name="Faixa (Min-Max)",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=stats["GenreComboLabel"],
            y=stats["mean_value"],
            mode="markers",
            marker=dict(color="#F5F5F5", size=10, symbol="diamond"),
            name="Media",
            hovertemplate="<b>%{x}</b><br>Media: %{y:.2f}<extra></extra>",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=stats["GenreComboLabel"],
            y=stats["max_value"],
            mode="markers",
            marker=dict(color=IMDB_YELLOW, size=10, symbol="star"),
            name="Top Nota",
            hovertemplate="<b>%{x}</b><br>Top Nota (Max): %{y:.2f}<extra></extra>",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=stats["GenreComboLabel"],
            y=stats["min_value"],
            mode="markers",
            marker=dict(color="#9A9A9A", size=8, symbol="circle"),
            name="Minima",
            hovertemplate="<b>%{x}</b><br>Minima: %{y:.2f}<extra></extra>",
        )
    )
    fig.update_layout(
        title=title,
        xaxis_title="Combinacao de Generos",
        yaxis_title=y_title,
        barmode="overlay",
        legend_title_text="Metricas",
        margin=dict(l=10, r=10, t=48, b=28),
    )
    fig.update_xaxes(automargin=True, tickangle=0, tickfont=dict(size=10))
    dark_layout(fig)
    return fig


def render_genre_range_metrics(filtered: pd.DataFrame) -> None:
    combos_df = filtered.copy()
    combos_df["GenreCombo"] = (
        combos_df["Genre"]
        .fillna("")
        .astype(str)
        .str.split(",")
        .apply(lambda parts: ",".join([p.strip() for p in parts if p.strip()]))
    )
    combos_df = combos_df[combos_df["GenreCombo"] != ""]

    left, right = st.columns(2, gap="medium")
    with left:
        meta_stats = _summary_stats(combos_df.dropna(subset=["Metascore"]), "Metascore", top_n=10)
        st.plotly_chart(
            _range_marker_fig(
                meta_stats,
                title="Top 10 Combinacoes de Generos por Metascore",
                y_title="Metascore",
            ),
            use_container_width=True,
        )
    with right:
        rating_stats = _summary_stats(combos_df.dropna(subset=["Rating"]), "Rating", top_n=10)
        st.plotly_chart(
            _range_marker_fig(
                rating_stats,
                title="Avaliacao IMDb por Top 10 Combinacoes de Generos",
                y_title="IMDb Rating",
            ),
            use_container_width=True,
        )
