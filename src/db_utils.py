from __future__ import annotations

import os
from pathlib import Path
from typing import Sequence

import pandas as pd
import pymysql


SCHEMA = "looqbox-challenge"


def load_env_file(path: str = ".env") -> None:
    env_path = Path(path)
    if not env_path.exists():
        raise FileNotFoundError(f".env not found: {env_path.resolve()}")

    for raw_line in env_path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ[key.strip()] = value.strip().strip('"').strip("'")


def required_env_any(*names: str) -> str:
    for name in names:
        value = os.getenv(name, "").strip()
        if value:
            return value
    raise ValueError(f"Missing env var. Expected one of: {', '.join(names)}")


def get_connection() -> pymysql.connections.Connection:
    load_env_file(".env")
    host = required_env_any("MYSQL_IP", "MYSQL_HOST")
    user = required_env_any("MYSQL_USER", "MYSQL_User")
    password = required_env_any("MYSQL_PASS", "MYSQL_Pass")

    return pymysql.connect(
        host=host,
        user=user,
        password=password,
        port=3306,
        database=SCHEMA,
        connect_timeout=10,
        read_timeout=10,
        write_timeout=10,
    )


def read_sql_df(
    conn: pymysql.connections.Connection,
    query: str,
    params: Sequence[object] | None = None,
) -> pd.DataFrame:
    with conn.cursor() as cur:
        cur.execute(query, params)
        rows = cur.fetchall()
        cols = [col[0] for col in cur.description]
    return pd.DataFrame(rows, columns=cols)
