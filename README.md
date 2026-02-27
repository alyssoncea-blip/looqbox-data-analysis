# Looqbox Data Challenge

Projeto com solução completa do desafio técnico usando MySQL + Python:
- Parte SQL (3 queries)
- Case 1 (função dinâmica `retrieve_data`)
- Case 2 (queries fixas + visualização TM)
- Dashboard/visualizações IMDb

## Requisitos
- Python 3.12+
- Acesso ao MySQL do challenge
- Arquivo `.env` com credenciais

Exemplo de `.env`:

```env
MYSQL_IP=
MYSQL_USER=
MYSQL_PASS=
```

## Instalação

```bash
pip install -r requirements.txt
```

## Execução

### Testar conexão
```bash
python test_mysql_connection.py
```

### Case 1
```bash
python run_case1.py
```
Saída: `outputs/case1_retrieve_data_sample.csv`

### Case 2
```bash
python run_case2.py
```
Saídas:
- `outputs/case2_tm_by_store.csv`
- `outputs/case2_tm_table.png`

### Dashboard IMDb (Streamlit)
```bash
streamlit run app_imdb_dashboard.py
```

## Estrutura principal
- `sql/part1/` -> queries SQL da Parte 1
- `src/` -> módulos Python (db, cases, dashboard, visualizações)
- `outputs/` -> artefatos gerados
- `docs/` -> documentação complementar
