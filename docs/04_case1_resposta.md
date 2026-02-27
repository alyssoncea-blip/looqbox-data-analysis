# Resposta - Questao 1

## Objetivo

Criar uma funcao dinamica e reutilizavel para retornar dados da tabela `data_product_sales` variando filtros por:

- `product_code` (int)
- `store_code` (int)
- `date` (lista com duas datas ISO)

## Implementacao

- Arquivo: `src/case1_dynamic_query.py`
- Funcao: `retrieve_data(product_code, store_code, date)`
- Boas praticas:
  - validacao de tipos
  - query parametrizada (`%s`) para evitar SQL injection
  - retorno em `pandas.DataFrame`

## Execucao

Runner dedicado:

```bash
py -3.12 run_case1.py
```

Saida:

- `outputs/case1_retrieve_data_sample.csv`
