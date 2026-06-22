from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
PHASE_DIR = BASE_DIR.parent

input_path = PHASE_DIR / "day_10_ai_assisted_pandas_review" / "cleaned_paid_orders.csv"
df = pd.read_csv(input_path)

print("\n=== 1. Loaded data ===")
print(df.head())

print("\n=== 2. Shape ===")
print(df.shape)

print("\n=== 3. Validation checks ===")

assert len(df) > 0, "Final report is empty"

assert df["status"].eq("paid").all(), "Not all orders have paid status"

assert df["amount"].gt(0).all(), "Some orders have non-positive amount"

assert df.isna().sum().sum() == 0, "Final report has missing values"

assert df["order_id"].is_unique, "order_id values are not unique"

expected_columns = [
    "order_id",
    "user_id",
    "name",
    "city",
    "product",
    "amount",
    "order_date",
    "status",
]

assert list(df.columns) == expected_columns, "Unexpected final report columns"

print("All validation checks passed.")