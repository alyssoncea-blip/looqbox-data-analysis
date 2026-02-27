from __future__ import annotations

from pathlib import Path

from src.case1_dynamic_query import retrieve_data


def main() -> int:
    my_data = retrieve_data(product_code=18, store_code=1, date=["2019-01-01", "2019-01-31"])
    print("Case 1 - retrieve_data")
    print(f"Rows returned: {len(my_data)}")
    print(my_data.head(5).to_string(index=False))

    Path("outputs").mkdir(parents=True, exist_ok=True)
    my_data.to_csv("outputs/case1_retrieve_data_sample.csv", index=False)
    print("Saved: outputs/case1_retrieve_data_sample.csv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
