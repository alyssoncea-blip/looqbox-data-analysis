# Resposta - Questao 2

## Objetivo

Usar exatamente as duas queries fornecidas pelo cliente, aplicar filtro de periodo em Python e entregar a visualizacao solicitada (Loja, Categoria, TM).

## Implementacao

- Arquivo: `src/case2_client_visualization.py`
- Queries usadas sem alteracao:
  - `QUERY_1`: `data_store_cad`
  - `QUERY_2`: `data_store_sales` com `DATE BETWEEN '2019-01-01' AND '2019-12-31'`
- Filtro adicional aplicado em Python:
  - `['2019-10-01', '2019-12-31']`
- Metrica:
  - `TM = SUM(SALES_VALUE) / SUM(SALES_QTY)` por Loja e Categoria

## Execucao

Runner dedicado:

```bash
py -3.12 run_case2.py
```

Saidas:

- `outputs/case2_tm_by_store.csv`
- `outputs/case2_tm_table.png`
