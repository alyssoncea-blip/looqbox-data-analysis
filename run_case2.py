from __future__ import annotations

from pathlib import Path

from src.case2_client_visualization import build_tm_table, save_tm_table_visual


def main() -> int:
    tm_df = build_tm_table(date_range=["2019-10-01", "2019-12-31"])
    print("Case 2 - fixed queries + TM visualization")
    print(tm_df.to_string(index=False))

    Path("outputs").mkdir(parents=True, exist_ok=True)
    tm_df.to_csv("outputs/case2_tm_by_store.csv", index=False)
    print("Saved: outputs/case2_tm_by_store.csv")

    image_path = save_tm_table_visual(
        tm_df,
        "outputs/case2_tm_table.png",
        period_text="Periodo: 2019-10-01 a 2019-12-31",
    )
    print(f"Saved visualization: {image_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
