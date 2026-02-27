from __future__ import annotations

from typing import Sequence

import pandas as pd

from src.db_utils import get_connection, read_sql_df


def retrieve_data(product_code: int, store_code: int, date: Sequence[str]) -> pd.DataFrame:
    """Return all columns from data_product_sales using safe dynamic parameters."""
    if not isinstance(product_code, int):
        raise TypeError("product_code must be an integer")
    if not isinstance(store_code, int):
        raise TypeError("store_code must be an integer")
    if not isinstance(date, (list, tuple)) or len(date) != 2:
        raise ValueError("date must be ['YYYY-MM-DD', 'YYYY-MM-DD']")

    start_date, end_date = date
    query = """
    SELECT
        STORE_CODE,
        PRODUCT_CODE,
        DATE,
        SALES_VALUE,
        SALES_QTY
    FROM data_product_sales
    WHERE PRODUCT_CODE = %s
      AND STORE_CODE = %s
      AND DATE BETWEEN %s AND %s
    ORDER BY DATE ASC
    """
    params = (product_code, str(store_code), start_date, end_date)

    with get_connection() as conn:
        return read_sql_df(conn, query, params=params)
