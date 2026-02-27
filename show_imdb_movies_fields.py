from __future__ import annotations

from src.db_utils import get_connection, read_sql_df


def main() -> int:
    query = """
    SELECT
        COLUMN_NAME,
        COLUMN_TYPE,
        IS_NULLABLE,
        COLUMN_KEY,
        COLUMN_DEFAULT,
        EXTRA
    FROM information_schema.columns
    WHERE table_schema = 'looqbox-challenge'
      AND table_name = 'IMDB_movies'
    ORDER BY ORDINAL_POSITION
    """

    with get_connection() as conn:
        fields_df = read_sql_df(conn, query)

    print("Campos da tabela IMDB_movies:")
    print(fields_df.to_string(index=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
