# Parte 2 - SQL (Resultados de Execucao)

Data de execucao: 2026-02-26

Schema: `looqbox-challenge`

## 1) Top 10 produtos mais caros

| PRODUCT_COD | PRODUCT_NAME | PRODUCT_VAL | DEP_NAME | SECTION_NAME |
|---:|---|---:|---|---|
| 301409 | Whisky Escoces THE MACALLAN Ruby Garrafa 700ml com Caixa | 741.99 | BEBIDAS | BEBIDAS |
| 176185 | Whisky Escoces JOHNNIE WALKER Blue Label Garrafa 750ml | 735.90 | BEBIDAS | BEBIDAS |
| 315481 | Cafeteira Expresso 3 CORACOES Tres Modo Vermelho | 499.00 | BEBIDAS | BEBIDAS |
| 100280 | Vinho Portugues Tinto Vintage QUINTA DO CRASTO Garrafa 750ml | 445.90 | BEBIDAS | VINHOS |
| 320046 | Escova Dental Eletrica ORAL B D34 Professional Care 5000 110v | 399.90 | PERFUMARIA | HIGIENE BUCAL |
| 190817 | Champagne Rose VEUVE CLICQUOT PONSARDIM Garrafa 750ml | 366.90 | MERCEARIA | ARTIGOS-PARA-O-LAR |
| 153795 | Champagne Frances Brut Imperial MOET Rose Garrafa 750ml | 359.90 | MERCEARIA | ARTIGOS-PARA-O-LAR |
| 311397 | Conjunto de Panelas Allegra em Inox TRAMONTINA 5 Pecas Gratis Utensilios 5 Pecas | 359.00 | MERCEARIA | ARTIGOS-PARA-O-LAR |
| 147706 | Whisky Escoces CHIVAS REGAL 18 Anos Garrafa 750ml | 329.90 | BEBIDAS | BEBIDAS |
| 44311 | Champagne Frances Demi Sec Nectar Imperial MOET & CHANDON Garrafa 750ml | 315.90 | MERCEARIA | ARTIGOS-PARA-O-LAR |

## 2) Secoes dos departamentos BEBIDAS e PADARIA

| DEP_COD | DEP_NAME | SECTION_COD | SECTION_NAME |
|---:|---|---:|---|
| 2 | BEBIDAS | 4 | BEBIDAS |
| 2 | BEBIDAS | 29 | CERVEJAS |
| 2 | BEBIDAS | 31 | REFRESCOS |
| 2 | BEBIDAS | 30 | VINHOS |
| 7 | PADARIA | 8 | DOCES-E-SOBREMESAS |
| 7 | PADARIA | 27 | GESTANTE |
| 7 | PADARIA | 19 | PADARIA |
| 7 | PADARIA | 22 | QUEIJOS-E-FRIOS |

## 3) Total de vendas por Area de Negocio (Q1 2019)

| BUSINESS_CODE | BUSINESS_NAME | TOTAL_SALES_VALUE_USD |
|---:|---|---:|
| 4 | Farma | 81776691.73 |
| 1 | Varejo | 81032347.65 |
| 5 | Atacado | 80384884.60 |
| 2 | Proximidade | 80171122.80 |
| 3 | Posto | 32072326.40 |
