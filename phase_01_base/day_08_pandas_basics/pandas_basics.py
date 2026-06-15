from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).parent

users_path = BASE_DIR / "users.csv"
orders_path = BASE_DIR / "orders.csv"

users = pd.read_csv(users_path)
orders = pd.read_csv(orders_path)


print("\n=== 1. Users head ===")
print(users.head())

print("\n=== 2. Orders head ===")
print(orders.head())

print("\n=== 3. Users info ===")
print(users.info())

print("\n=== 4. Orders describe ===")
print(orders.describe())

# 5. Вывести пользователей из Moscow.
print("\n=== 5. Users from Moscow ===")
moscow_users = users[users["city"] == "Moscow"]
print(moscow_users)

# 6. Вывести пользователей старше 25 лет.
print("\n=== 6. Users older than 25 ===")
users_older_25 = users[users["age"] > 25]
print(users_older_25)

# 7. Посчитать количество пользователей по городам.
print("\n=== 7. Users count by city ===")
users_by_city = users.groupby("city")["user_id"].count()
print(users_by_city)

# 8. Посчитать общую сумму заказов.
print("\n=== 8. Total order amount ===")
total_amount = orders["amount"].sum()
print(total_amount)

# 9. Посчитать средний чек.
print("\n=== 9. Average order amount ===")
avg_order_amount = orders["amount"].mean()
print(avg_order_amount)

# 10. Объединить users и orders через merge.
print("\n=== 10. Merged users + orders ===")
merged = orders.merge(users, on="user_id", how="inner")
print(merged)

# 11. Посчитать сумму заказов по пользователям.
print("\n=== 11. Total amount by user ===")
total_by_user = (
    merged
    .groupby(["user_id", "name"])["amount"]
    .sum()
    .reset_index(name="total_amount")
    .sort_values("total_amount", ascending=False)
)
print(total_by_user)

# 12. Добавить customer_level через функцию.
print("\n=== 12. Customer levels ===")


def get_customer_level(total_amount: int) -> str:
    if total_amount >= 50000:
        return "high_value"
    if total_amount >= 10000:
        return "medium_value"
    return "low_value"


total_by_user["customer_level"] = total_by_user["total_amount"].apply(get_customer_level)
print(total_by_user)

# 13. Посчитать сумму заказов по городам.
print("\n=== 13. Total amount by city ===")
total_by_city = (
    merged
    .groupby("city")["amount"]
    .sum()
    .reset_index(name="total_amount")
    .sort_values("total_amount", ascending=False)
)
print(total_by_city)
print("\n=== 15. Top 3 orders ===")
top_3_orders = (
    merged
    .sort_values("amount", ascending=False)
    [["name", "product", "amount"]]
    .head(3)
)
print(top_3_orders)

print("\n=== 16. Average order amount by segment ===")
avg_by_segment = (
    merged
    .groupby("segment")["amount"]
    .mean()
    .reset_index(name="avg_order_amount")
    .sort_values("avg_order_amount", ascending=False)
)
print(avg_by_segment)

print("\n=== 15. Shape of tables ===")
print("users shape:", users.shape)
print("orders shape:", orders.shape)
print("merged shape:", merged.shape)

print("\n=== 16. Columns ===")
print("users columns:", users.columns.tolist())
print("orders columns:", orders.columns.tolist())
print("merged columns:", merged.columns.tolist())

city_summary_path = BASE_DIR / "city_summary.csv"
total_by_city.to_csv(city_summary_path, index=False)

print(f"\nSaved city summary to: {city_summary_path}")

