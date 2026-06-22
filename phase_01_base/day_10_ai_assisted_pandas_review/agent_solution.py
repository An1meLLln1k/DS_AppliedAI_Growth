from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
PHASE_DIR = BASE_DIR.parent

users_path = PHASE_DIR / "day_08_pandas_basics" / "users.csv"
orders_path = PHASE_DIR / "day_09_pandas_cleaning" / "dirty_orders.csv"
output_path = BASE_DIR / "cleaned_paid_orders.csv"

users = pd.read_csv(users_path)
orders = pd.read_csv(orders_path)

print("\n=== 1. Source data shape ===")
print("users:", users.shape)
print("orders:", orders.shape)

# Keep only paid orders
paid_orders = orders[orders["status"] == "paid"]

# Remove invalid amounts
cleaned_orders = paid_orders[paid_orders["amount"] > 0].copy()

# Fill missing order dates instead of silently leaving NaN in the final report
cleaned_orders["order_date"] = cleaned_orders["order_date"].fillna("unknown_date")

# Add user data
orders_with_users = cleaned_orders.merge(users, on="user_id", how="inner")

# Select final columns
final_report = orders_with_users[
    ["order_id", "user_id", "name", "city", "product", "amount", "order_date", "status"]
]

# Sort by amount
final_report = final_report.sort_values("amount", ascending=False)

print("\n=== 2. Final report ===")
print(final_report)

print("\n=== 3. Final report shape ===")
print(final_report.shape)

print("\n=== 4. Validation checks ===")

print("Paid orders count:", len(paid_orders))
print("Cleaned orders count:", len(cleaned_orders))
print("Rows after merge:", len(orders_with_users))
print("Rows lost after merge:", len(cleaned_orders) - len(orders_with_users))

print("\nStatus values in final report:")
print(final_report["status"].value_counts())

print("\nAmount check:")
print("All amounts are positive:", final_report["amount"].gt(0).all())

print("\nMissing values in final report:")
print(final_report.isna().sum())

unmatched_orders = cleaned_orders.merge(
    users[["user_id"]],
    on="user_id",
    how="left",
    indicator=True
)

unmatched_orders = unmatched_orders[unmatched_orders["_merge"] == "left_only"]

print("\nOrders without matching user:")
print(unmatched_orders[["order_id", "user_id", "product", "amount", "status"]])

final_report.to_csv(output_path, index=False)

print("\nSaved to:", output_path)