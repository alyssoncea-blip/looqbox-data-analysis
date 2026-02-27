from __future__ import annotations

from pathlib import Path

from src.challenge_cases import build_case2_tm_table, retrieve_data, save_case2_visualization


def main() -> int:
    print("Case 1: testing retrieve_data(product_code, store_code, date)")
    my_data = retrieve_data(product_code=18, store_code=1, date=["2019-01-01", "2019-01-31"])
    print(f"Rows returned: {len(my_data)}")
    print(my_data.head(5).to_string(index=False))

    Path("outputs").mkdir(parents=True, exist_ok=True)
    my_data.to_csv("outputs/case1_retrieve_data_sample.csv", index=False)
    print("Saved: outputs/case1_retrieve_data_sample.csv")

    print("\nCase 2: running fixed queries + period filter + TM visualization")
    tm_df = build_case2_tm_table(date_range=["2019-10-01", "2019-12-31"])
    print(tm_df.to_string(index=False))

    tm_df.to_csv("outputs/case2_tm_by_store.csv", index=False)
    print("Saved: outputs/case2_tm_by_store.csv")

    image_path = save_case2_visualization(tm_df, "outputs/case2_tm_table.png")
    print(f"Saved visualization: {image_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
