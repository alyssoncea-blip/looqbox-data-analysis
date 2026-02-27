# Parte 4 - Visualizacao Livre (IMDB_movies)

## Pergunta analitica

Quais generos principais apresentam maior media de avaliacao no dataset IMDB_movies?

## Visualizacao escolhida

Grafico de barras horizontal com `avg_rating` por `primary_genre` (considerando somente generos com pelo menos 20 filmes).

## Por que esse grafico

- Barras sao o formato mais direto para comparar medias entre categorias.
- O eixo horizontal facilita leitura de valores proximos.
- O filtro de volume minimo reduz ruido estatistico de generos com poucas observacoes.

## Insight principal

O grafico permite identificar rapidamente quais generos mantem melhor avaliacao media e quais ficam abaixo, apoiando comparacoes de qualidade percebida por categoria.

## Arquivos

- Script Python: `src/imdb_visualization.py`
- Runner: `run_imdb_viz.py`
- Saida grafica: `outputs/imdb_avg_rating_by_genre.png`
