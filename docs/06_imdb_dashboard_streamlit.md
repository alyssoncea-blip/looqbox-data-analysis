# IMDb Interactive Dashboard (Streamlit + Plotly)

## Run

```bash
py -3.12 -m streamlit run app_imdb_dashboard.py
```

## What is included

- IMDb-inspired visual identity (black, yellow `#F5C518`, white)
- IMDb logo badge in header
- KPI cards:
  - Total movies
  - Average rating
  - Top rated movie
  - Most frequent genre
- Interactive filters:
  - Year range
  - Genre selector
  - Minimum votes
- Visual sections:
  - Top 10 movies ranking
  - Average rating over time
  - Movies per year
  - Genre distribution
  - Average rating by genre (donut)
  - Revenue vs rating (bubble)
  - Runtime vs rating
  - Rating distribution

## Files

- App: `app_imdb_dashboard.py`
- Data layer: `src/imdb_dashboard_data.py`
