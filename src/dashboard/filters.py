from __future__ import annotations

from typing import Sequence, Tuple

import streamlit as st

SELECT_ALL_TOKEN = "Selecionar todos"


def _normalize_genres_selection(all_genres: list[str]) -> None:
    selected = st.session_state.get("genres_filter", [])
    if SELECT_ALL_TOKEN in selected:
        st.session_state["genres_filter"] = list(all_genres)


def render_filter_panel(
    min_year: int,
    max_year: int,
    genre_options: Sequence[str],
    max_votes: int,
) -> Tuple[Tuple[int, int], list[str], int]:
    """Render horizontal premium filter bar and return selected values."""
    genre_options_list = list(genre_options)
    options_with_all = [SELECT_ALL_TOKEN, *genre_options_list]

    if "genres_filter" not in st.session_state:
        st.session_state["genres_filter"] = genre_options_list

    st.markdown('<div class="filters-shell">', unsafe_allow_html=True)
    c0, c1, c2, c3 = st.columns([0.95, 1.55, 1.1, 1.1], gap="medium")

    with c0:
        st.markdown(
            """
            <div class="filters-title">FILTERS</div>
            <div class="filters-subtitle">Refine the ranking</div>
            <div class="filters-rule"></div>
            """,
            unsafe_allow_html=True,
        )

    with c1:
        st.markdown('<div class="filter-label">Genres</div>', unsafe_allow_html=True)
        genres = st.multiselect(
            "Genres",
            options=options_with_all,
            key="genres_filter",
            placeholder="Digite para buscar genero...",
            label_visibility="collapsed",
            on_change=_normalize_genres_selection,
            args=(genre_options_list,),
        )
        genres = [g for g in genres if g != SELECT_ALL_TOKEN]

    with c2:
        st.markdown('<div class="filter-label">Year Range</div>', unsafe_allow_html=True)
        year_range = st.slider(
            "Year Range",
            min_value=min_year,
            max_value=max_year,
            value=(min_year, max_year),
            key="year_range_filter",
            label_visibility="collapsed",
        )

    with c3:
        st.markdown('<div class="filter-label">Minimum Votes</div>', unsafe_allow_html=True)
        min_votes = int(
            st.number_input(
                "Minimum Votes",
                min_value=0,
                max_value=max_votes,
                value=0,
                step=100,
                key="min_votes_filter",
                label_visibility="collapsed",
            )
        )

    st.markdown("</div>", unsafe_allow_html=True)
    return year_range, genres, min_votes
