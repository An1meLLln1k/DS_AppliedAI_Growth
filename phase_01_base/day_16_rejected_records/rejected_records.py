from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
PHASE_DIR = BASE_DIR.parent

orders_path = PHASE_DIR / "day_09_pandas_cleaning" / "dirty_orders.csv"
output_path = BASE_DIR / "rejected_orders.csv"

orders = pd.read_csv(orders_path)

orders_with_reasons = orders.copy()
orders_with_reasons["reject_reasons"] = ""

orders_with_reasons.loc[
    orders_with_reasons["status"] != "paid",
    "reject_reasons",
] += "invalid_status;"

orders_with_reasons.loc[
    orders_with_reasons["amount"].isna(),
    "reject_reasons",
] += "missing_amount;"

orders_with_reasons.loc[
    orders_with_reasons["amount"].notna() & (orders_with_reasons["amount"] <= 0),
    "reject_reasons",
] += "non_positive_amount;"

rejected_orders = orders_with_reasons[
    orders_with_reasons["reject_reasons"] != ""
].copy()

rejected_orders["reject_reasons"] = rejected_orders["reject_reasons"].str.rstrip(";")

valid_orders = orders_with_reasons[
    orders_with_reasons["reject_reasons"] == ""
].copy()

print("\n=== 1. Source orders count ===")
print(len(orders))

print("\n=== 2. Valid orders count ===")
print(len(valid_orders))

print("\n=== 3. Rejected orders count ===")
print(len(rejected_orders))

print("\n=== 4. Rejected orders ===")
print(rejected_orders[["order_id", "user_id", "product", "amount", "status", "reject_reasons"]])

print("\n=== 5. Rejection reason counts ===")
reason_counts = (
    rejected_orders["reject_reasons"]
    .str.split(";")
    .explode()
    .value_counts()
)

print(reason_counts)

rejected_orders.to_csv(output_path, index=False)

print("\nSaved to:", output_path)