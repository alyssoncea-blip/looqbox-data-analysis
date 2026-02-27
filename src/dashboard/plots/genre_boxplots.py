from __future__ import annotations

import pandas as pd

from src.dashboard.plots.genre_range import render_genre_range_metrics


def render_genre_boxplots(filtered: pd.DataFrame) -> None:
    """Backward-compatible alias for the refactored range metrics view."""
    render_genre_range_metrics(filtered)
