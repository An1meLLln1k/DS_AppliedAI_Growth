-- Week 01 SQL Mini Report
-- Dataset: users + orders
-- Goal: summarize customer and order behavior

-- 1. Общая сводка:
-- количество пользователей, количество заказов, общая сумма заказов, средний чек.
SELECT
    (SELECT COUNT(*) FROM users) AS total_users,
    (SELECT COUNT(*) FROM orders) AS total_orders,
    (SELECT SUM(amount) FROM orders) AS total_amount,
    (SELECT AVG(amount) FROM orders) AS avg_order_amount;


-- 2. Сумма заказов по пользователям.
-- Вывести: name, total_amount, orders_count.
-- Отсортировать по total_amount по убыванию.
SELECT
    u.name,
    SUM(o.amount) AS total_amount,
    COUNT(o.order_id) AS orders_count
FROM users AS u
JOIN orders AS o ON u.user_id = o.user_id
GROUP BY u.user_id, u.name
ORDER BY total_amount DESC;


-- 3. Категории пользователей по total_amount через CTE + CASE WHEN.
-- high_value: total_amount >= 50000
-- medium_value: total_amount >= 10000
-- low_value: иначе
-- Вывести: name, total_amount, customer_level.
WITH category AS (
    SELECT
        u.user_id,
        u.name,
        SUM(o.amount) AS total_amount
    FROM orders AS o
    JOIN users AS u ON u.user_id = o.user_id
    GROUP BY u.user_id, u.name
)
SELECT
    name,
    total_amount,
    CASE
        WHEN total_amount >= 50000 THEN 'high_value'
        WHEN total_amount >= 10000 THEN 'medium_value'
        ELSE 'low_value'
    END AS customer_level
FROM category
ORDER BY total_amount DESC;


-- 4. Сумма заказов по городам.
-- Вывести: city, total_amount, orders_count.
SELECT
    u.city,
    SUM(o.amount) AS total_amount,
    COUNT(o.order_id) AS orders_count
FROM users AS u
JOIN orders AS o ON o.user_id = u.user_id
GROUP BY u.city
ORDER BY total_amount DESC;


-- 5. Средний чек по сегментам.
-- Вывести: segment, avg_order_amount, orders_count.
SELECT
    u.segment,
    AVG(o.amount) AS avg_order_amount,
    COUNT(o.order_id) AS orders_count
FROM users AS u
JOIN orders AS o ON u.user_id = o.user_id
GROUP BY u.segment
ORDER BY avg_order_amount DESC;


-- 6. Топ-3 самых дорогих заказа.
-- Вывести: name, product, amount.
SELECT
    u.name,
    o.product,
    o.amount
FROM users AS u
JOIN orders AS o ON u.user_id = o.user_id
ORDER BY o.amount DESC
LIMIT 3;


-- 7. Самый дорогой заказ каждого пользователя через CTE + ROW_NUMBER().
-- Вывести: name, product, amount.
WITH ranked_orders AS (
    SELECT
        u.name,
        o.product,
        o.amount,
        ROW_NUMBER() OVER (
            PARTITION BY u.user_id
            ORDER BY o.amount DESC
        ) AS rn
    FROM users AS u
    JOIN orders AS o ON u.user_id = o.user_id
)
SELECT
    name,
    product,
    amount
FROM ranked_orders
WHERE rn = 1
ORDER BY amount DESC;


-- 8. Для каждого заказа вывести сумму заказов пользователя через SUM() OVER.
-- Вывести: name, product, amount, total_amount_by_user.
SELECT
    u.name,
    o.product,
    o.amount,
    SUM(o.amount) OVER (
        PARTITION BY u.user_id
    ) AS total_amount_by_user
FROM users AS u
JOIN orders AS o ON o.user_id = u.user_id
ORDER BY u.name, o.amount DESC;