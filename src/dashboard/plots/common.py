from __future__ import annotations

import plotly.graph_objects as go

from src.dashboard.styles import IMDB_BLACK, IMDB_WHITE


def dark_layout(fig: go.Figure) -> go.Figure:
    fig.update_layout(
        paper_bgcolor=IMDB_BLACK,
        plot_bgcolor="#1A1A1A",
        font=dict(color=IMDB_WHITE),
        margin=dict(l=40, r=24, t=46, b=40),
        legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color=IMDB_WHITE)),
    )
    return fig

