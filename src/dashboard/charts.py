from __future__ import annotations

"""Facade for dashboard chart modules.

Keeps backward-compatible imports while delegating each chart section
into dedicated visualization modules.
"""

from src.dashboard.plots.advanced import render_advanced
from src.dashboard.plots.distribution import render_rating_distribution
from src.dashboard.plots.genre_range import render_genre_range_metrics
from src.dashboard.plots.genre import render_genre
from src.dashboard.plots.temporal import render_temporal

# Legacy alias name preserved for backward compatibility.
render_genre_boxplots = render_genre_range_metrics

__all__ = [
    "render_temporal",
    "render_genre",
    "render_advanced",
    "render_rating_distribution",
    "render_genre_range_metrics",
    "render_genre_boxplots",
]
