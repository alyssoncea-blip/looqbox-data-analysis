from __future__ import annotations

from typing import Sequence

import pandas as pd

from src.db_utils import get_connection, read_sql_df
from src.visualizations.case2_tm_table_plot import save_tm_table_visual


# Query 1 (must be used exactly as provided)
QUERY_1 = """
SELECT
      STORE_CODE,
      STORE_NAME,
      START_DATE,
      END_DATE,
      BUSINESS_NAME,
      BUSINESS_CODE
FROM data_store_cad
"""

# Query 2 (must be used exactly as provided)
QUERY_2 = """
SELECT
        STORE_CODE,
        DATE,
        SALES_VALUE,
        SALES_QTY
FROM data_store_sales
WHERE DATE BETWEEN '2019-01-01' AND '2019-12-31'
"""


def build_tm_table(date_range: Sequence[str] = ("2019-10-01", "2019-12-31")) -> pd.DataFrame:
    if not isinstance(date_range, (list, tuple)) or len(date_range) != 2:
        raise ValueError("date_range must be ['YYYY-MM-DD', 'YYYY-MM-DD']")

    start_date = pd.to_datetime(date_range[0])
    end_date = pd.to_datetime(date_range[1])

    with get_connection() as conn:
        stores = read_sql_df(conn, QUERY_1)
        sales = read_sql_df(conn, QUERY_2)

    sales["DATE"] = pd.to_datetime(sales["DATE"])
    sales = sales.loc[(sales["DATE"] >= start_date) & (sales["DATE"] <= end_date)].copy()

    merged = sales.merge(stores[["STORE_CODE", "STORE_NAME", "BUSINESS_NAME"]], on="STORE_CODE", how="left")
    tm_df = (
        merged.groupby(["STORE_NAME", "BUSINESS_NAME"], as_index=False)
        .agg(SALES_VALUE=("SALES_VALUE", "sum"), SALES_QTY=("SALES_QTY", "sum"))
        .assign(TM=lambda x: x["SALES_VALUE"] / x["SALES_QTY"])
    )
    tm_df = tm_df[["STORE_NAME", "BUSINESS_NAME", "TM"]].rename(
        columns={"STORE_NAME": "Loja", "BUSINESS_NAME": "Categoria"}
    )
    tm_df["TM"] = tm_df["TM"].round(2)
    return tm_df.sort_values("Loja").reset_index(drop=True)


# Plot function imported from src.visualizations.case2_tm_table_plot
