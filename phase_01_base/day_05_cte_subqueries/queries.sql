-- Day 05 SQL practice
-- Topic: CTE and subqueries
-- Dataset: users + orders

-- 1. Через CTE посчитать общую сумму заказов по каждому пользователю.
-- Вывести: name, total_amount.
WITH user_totals AS (
    SELECT
        u.user_id,
        u.name,
        SUM(o.amount) AS total_amount
    FROM users AS u
    JOIN orders AS o ON u.user_id = o.user_id
    GROUP BY u.user_id, u.name
)
SELECT
    name,
    total_amount
FROM user_totals
ORDER BY total_amount DESC;


-- 2. Через CTE найти пользователей, у которых total_amount > 10000.
-- Вывести: name, total_amount.
WITH user_totals AS (
    SELECT
        u.user_id,
        u.name,
        SUM(o.amount) AS total_amount
    FROM users AS u
    JOIN orders AS o ON u.user_id = o.user_id
    GROUP BY u.user_id, u.name
)
SELECT
    name,
    total_amount
FROM user_totals
WHERE total_amount > 10000
ORDER BY total_amount DESC;


-- 3. Через CTE посчитать количество заказов по каждому пользователю.
-- Вывести: name, orders_count.
WITH user_orders AS (
    SELECT
        u.user_id,
        u.name,
        COUNT(o.order_id) AS orders_count
    FROM users AS u
    JOIN orders AS o ON u.user_id = o.user_id
    GROUP BY u.user_id, u.name
)
SELECT
    name,
    orders_count
FROM user_orders
ORDER BY orders_count DESC;


-- 4. Через CTE найти пользователей, у которых orders_count >= 2.
-- Вывести: name, orders_count.
WITH user_orders AS (
    SELECT
        u.user_id,
        u.name,
        COUNT(o.order_id) AS orders_count
    FROM users AS u
    JOIN orders AS o ON u.user_id = o.user_id
    GROUP BY u.user_id, u.name
)
SELECT
    name,
    orders_count
FROM user_orders
WHERE orders_count >= 2
ORDER BY orders_count DESC;


-- 5. Через CTE посчитать средний чек по каждому сегменту.
-- Вывести: segment, avg_order_amount.
WITH segment_avg AS (
    SELECT
        u.segment,
        AVG(o.amount) AS avg_order_amount
    FROM users AS u
    JOIN orders AS o ON u.user_id = o.user_id
    GROUP BY u.segment
)
SELECT
    segment,
    avg_order_amount
FROM segment_avg
ORDER BY avg_order_amount DESC;


-- 6. Через CTE найти сегменты, где avg_order_amount > 10000.
-- Вывести: segment, avg_order_amount.
WITH segment_avg AS (
    SELECT
        u.segment,
        AVG(o.amount) AS avg_order_amount
    FROM users AS u
    JOIN orders AS o ON u.user_id = o.user_id
    GROUP BY u.segment
)
SELECT
    segment,
    avg_order_amount
FROM segment_avg
WHERE avg_order_amount > 10000
ORDER BY avg_order_amount DESC;


-- 7. Через подзапрос найти заказы дороже среднего заказа.
-- Вывести: order_id, product, amount.
SELECT
    order_id,
    product,
    amount
FROM orders
WHERE amount > (
    SELECT AVG(amount)
    FROM orders
)
ORDER BY amount DESC;


-- 8. Через подзапрос найти пользователей, у которых есть хотя бы один заказ дороже 50000.
-- Вывести: user_id, name.
SELECT
    user_id,
    name
FROM users
WHERE user_id IN (
    SELECT user_id
    FROM orders
    WHERE amount > 50000
)
ORDER BY user_id;


-- 9. Через два CTE:
-- первый CTE: посчитать total_amount по пользователям
-- второй CTE: добавить customer_level через CASE WHEN
-- Вывести: name, total_amount, customer_level.
WITH user_totals AS (
    SELECT
        u.user_id,
        u.name,
        SUM(o.amount) AS total_amount
    FROM users AS u
    JOIN orders AS o ON u.user_id = o.user_id
    GROUP BY u.user_id, u.name
),
customer_levels AS (
    SELECT
        user_id,
        name,
        total_amount,
        CASE
            WHEN total_amount >= 50000 THEN 'high_value'
            WHEN total_amount >= 10000 THEN 'medium_value'
            ELSE 'low_value'
        END AS customer_level
    FROM user_totals
)
SELECT
    name,
    total_amount,
    customer_level
FROM customer_levels
ORDER BY total_amount DESC;


-- 10. Через CTE посчитать общую сумму заказов по городам,
-- затем вывести только города, где total_amount > 10000.
-- Вывести: city, total_amount.
WITH city_totals AS (
    SELECT
        u.city,
        SUM(o.amount) AS total_amount
    FROM users AS u
    JOIN orders AS o ON u.user_id = o.user_id
    GROUP BY u.city
)
SELECT
    city,
    total_amount
FROM city_totals
WHERE total_amount > 10000
ORDER BY total_amount DESC;