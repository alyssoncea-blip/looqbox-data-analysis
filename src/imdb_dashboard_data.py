from __future__ import annotations

import pandas as pd

from src.db_utils import get_connection, read_sql_df


def load_imdb_movies() -> pd.DataFrame:
    query = """
    SELECT
        Id,
        Title,
        Genre,
        Director,
        Actors,
        Year,
        Runtime,
        Rating,
        Votes,
        RevenueMillions,
        Metascore
    FROM IMDB_movies
    """
    with get_connection() as conn:
        df = read_sql_df(conn, query)

    numeric_cols = ["Year", "Runtime", "Rating", "Votes", "RevenueMillions", "Metascore"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["PrimaryGenre"] = df["Genre"].fillna("").astype(str).str.split(",").str[0].str.strip()
    return df


def explode_genres(df: pd.DataFrame) -> pd.DataFrame:
    genres = df[["Id", "Title", "Year", "Rating", "Votes", "RevenueMillions", "Runtime", "Metascore", "Genre"]].copy()
    genres["Genre"] = genres["Genre"].fillna("").astype(str)
    genres = genres.assign(Genre=genres["Genre"].str.split(",")).explode("Genre")
    genres["Genre"] = genres["Genre"].str.strip()
    genres = genres[genres["Genre"] != ""]
    return genres
