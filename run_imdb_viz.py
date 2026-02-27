from __future__ import annotations

from src.imdb_visualization import create_genre_rating_chart


def main() -> int:
    stats, image_path = create_genre_rating_chart("outputs/imdb_avg_rating_by_genre.png")
    print("IMDB visualization generated.")
    print(stats.to_string(index=False))
    print(f"Saved chart: {image_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
