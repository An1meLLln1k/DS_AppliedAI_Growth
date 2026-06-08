import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).parent / "day01.db"


def create_database() -> None:
    """
    Создаёт маленькую учебную SQLite-базу для SQL-практики.
    Здесь две таблицы:
    - users: пользователи
    - orders: заказы пользователей
    """

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    # На всякий случай удаляем старые таблицы, чтобы скрипт можно было запускать повторно.
    cursor.execute("DROP TABLE IF EXISTS orders")
    cursor.execute("DROP TABLE IF EXISTS users")

    cursor.execute("""
        CREATE TABLE users (
            user_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            city TEXT NOT NULL,
            segment TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE orders (
            order_id INTEGER PRIMARY KEY,
            user_id INTEGER NOT NULL,
            product TEXT NOT NULL,
            amount INTEGER NOT NULL,
            order_date TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    """)

    users = [
        (1, "Alex", 24, "Ekaterinburg", "student"),
        (2, "Maria", 31, "Moscow", "premium"),
        (3, "Ivan", 27, "Kazan", "standard"),
        (4, "Olga", 22, "Saint Petersburg", "student"),
        (5, "Dmitry", 35, "Moscow", "premium"),
        (6, "Anna", 29, "Ekaterinburg", "standard"),
    ]

    orders = [
        (101, 1, "book", 1200, "2026-06-01"),
        (102, 1, "course", 5000, "2026-06-02"),
        (103, 2, "laptop", 90000, "2026-06-01"),
        (104, 3, "headphones", 8000, "2026-06-03"),
        (105, 4, "book", 1500, "2026-06-04"),
        (106, 5, "phone", 70000, "2026-06-05"),
        (107, 5, "monitor", 30000, "2026-06-06"),
        (108, 6, "keyboard", 6000, "2026-06-06"),
    ]

    cursor.executemany(
        "INSERT INTO users (user_id, name, age, city, segment) VALUES (?, ?, ?, ?, ?)",
        users,
    )

    cursor.executemany(
        "INSERT INTO orders (order_id, user_id, product, amount, order_date) VALUES (?, ?, ?, ?, ?)",
        orders,
    )

    connection.commit()
    connection.close()

    print(f"Database created: {DB_PATH}")


if __name__ == "__main__":
    create_database()