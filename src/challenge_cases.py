from __future__ import annotations

from typing import Sequence

import pandas as pd
from src.case1_dynamic_query import retrieve_data
from src.case2_client_visualization import build_tm_table
from src.db_utils import get_connection, load_env_file, read_sql_df, required_env_any
from src.visualizations.case2_tm_table_plot import save_tm_table_visual


def build_case2_tm_table(date_range: Sequence[str] = ("2019-10-01", "2019-12-31")) -> pd.DataFrame:
    """Compatibility wrapper kept for legacy imports."""
    return build_tm_table(date_range=date_range)


def save_case2_visualization(tm_df: pd.DataFrame, output_path: str = "outputs/case2_tm_table.png") -> str:
    """Compatibility wrapper kept for legacy imports."""
    return save_tm_table_visual(tm_df, output_path=output_path)
