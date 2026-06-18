from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).parent
orders_path = BASE_DIR / "dirty_orders.csv"

orders = pd.read_csv(orders_path)

print("\n=== 1. First rows ===")
print(orders.head())

print("\n=== 2. Data info ===")
print(orders.info())

print("\n=== 3. Missing values count ===")
print(orders.isna().sum())

print("\n=== 4. Status counts ===")
print(orders["status"].value_counts())

print("\n=== 5. Paid orders ===")
paid_orders = orders[orders["status"] == "paid"]
print(paid_orders)

print("\n=== 6. Positive amount orders ===")
positive_amount = orders[orders["amount"] > 0]
print(positive_amount)

print("\n=== 7. Valid paid orders ===")
valid_paid = orders[(orders["amount"] > 0) & (orders["status"] == "paid")]
print(valid_paid)

print("\n=== 8. Suspicious orders ===")
suspicious_orders = orders[
    (orders["amount"] <= 0) |
    (orders["amount"].isna())
]
print(suspicious_orders)
print("\n=== 8. Orders sorted by amount descending ===")
orders_sorted_by_amount = orders.sort_values("amount", ascending=False)
print(orders_sorted_by_amount)

print("9 Отсортируй paid_orders по order_date по возрастанию.Выведи результат.")
paid_orders_new = paid_orders.sort_values('order_date', ascending=True)
print(paid_orders_new)

print("\n=== 10 ")
product_and_status = orders[["product", "status"]]
print(product_and_status)
#Из valid_paid выбери только колонки:
#order_id, product, amount, status

print("\n 11")
valid_paid_new = valid_paid[["order_id", "product", "amount", "status"]]
print(valid_paid_new)

#Из valid_paid выбрать колонки product и amount,
#затем отсортировать по amount по убыванию.
print("\n 12") 
valid_paid_sorted = valid_paid[["product", "amount"]].sort_values('amount', ascending=False)
print(valid_paid_sorted)
print("\n=== 13. Fill missing amount with 0 ===")
orders_with_filled_amount = orders.copy()
orders_with_filled_amount["amount"] = orders_with_filled_amount["amount"].fillna(0)
print(orders_with_filled_amount)

print("\n 14")
orders_with_empty_date = orders.copy()
orders_with_empty_date["order_date"] = orders_with_empty_date["order_date"].fillna("unknown_date")
print(orders_with_empty_date)

print("\n=== 15. Drop rows with missing order_date ===")
orders_with_empty_date = orders.dropna(subset=["order_date"])
print(orders_with_empty_date)

print("\n=== 16. Drop rows with missing amount ===")
orders_with_amount = orders_with_empty_date.dropna(subset=["amount"])
print(orders_with_amount)

print("\n=== 17. Has order date flag ===")
orders_with_flags = orders.copy()
orders_with_flags["has_order_date"] = orders_with_flags["order_date"].notna()
print(orders_with_flags[["order_id", "order_date", "has_order_date"]])

print("\n=== 18. Is positive amount flag ===")
orders_with_flags["is_positive_amount"] = (
    (orders_with_flags["amount"] > 0) &
    (orders_with_flags["amount"].notna())
)
print(orders_with_flags[["order_id", "amount", "is_positive_amount"]])