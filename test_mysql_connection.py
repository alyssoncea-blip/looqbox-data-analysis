"""Teste simples de conexao MySQL para o desafio Looqbox.

Uso:
    python test_mysql_connection.py
"""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import List

import pymysql


EXPECTED_SCHEMA = "looqbox-challenge"


def load_env_file(path: str = ".env") -> None:
    env_path = Path(path)
    if not env_path.exists():
        return

    for raw_line in env_path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key:
            os.environ[key] = value


def required_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise ValueError(f"Variavel de ambiente obrigatoria ausente: {name}")
    return value


def required_env_any(*names: str) -> str:
    for name in names:
        value = os.getenv(name, "").strip()
        if value:
            return value
    names_str = ", ".join(names)
    raise ValueError(f"Variavel de ambiente obrigatoria ausente. Esperado um de: {names_str}")


def fetch_tables(conn: pymysql.connections.Connection, schema: str) -> List[str]:
    with conn.cursor() as cur:
        cur.execute(f"SHOW TABLES FROM `{schema}`")
        return [row[0] for row in cur.fetchall()]


def main() -> int:
    load_env_file(".env")

    host = required_env("MYSQL_IP")
    user = required_env_any("MYSQL_USER", "MYSQL_User")
    password = required_env_any("MYSQL_PASS", "MYSQL_Pass")

    print("Iniciando teste de conexao...")
    print(f"Host: {host}")
    print(f"Usuario: {user}")
    print(f"Schema esperado: {EXPECTED_SCHEMA}")

    try:
        conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            port=3306,
            connect_timeout=10,
            read_timeout=10,
            write_timeout=10,
        )
    except Exception as exc:
        print(f"ERRO: falha ao conectar no MySQL: {exc}")
        return 1

    try:
        with conn.cursor() as cur:
            cur.execute("SELECT VERSION()")
            version = cur.fetchone()[0]
            print(f"Conexao OK. Versao do servidor: {version}")

            cur.execute("SHOW DATABASES LIKE 'looqbox%'")
            schemas = [row[0] for row in cur.fetchall()]
            print(f"Schemas encontrados: {schemas}")

        if EXPECTED_SCHEMA not in schemas:
            print(f"ERRO: schema esperado nao encontrado: {EXPECTED_SCHEMA}")
            return 1

        tables = fetch_tables(conn, EXPECTED_SCHEMA)
        print(f"Tabelas em {EXPECTED_SCHEMA}: {tables}")
    except Exception as exc:
        print(f"ERRO: consulta falhou: {exc}")
        return 1
    finally:
        conn.close()

    print("Teste finalizado com sucesso.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
