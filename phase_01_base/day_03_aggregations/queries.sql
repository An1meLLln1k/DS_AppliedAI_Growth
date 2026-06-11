-- Day 03 SQL practice
-- Topic: aggregations
-- Dataset: users + orders

-- 1. Посчитать общее количество пользователей.
SELECT
    COUNT(*) AS users_count
FROM users;


-- 2. Посчитать общее количество заказов.
SELECT
    COUNT(*) AS orders_count
FROM orders;


-- 3. Посчитать общую сумму всех заказов.
SELECT
    SUM(amount) AS total_amount
FROM orders;


-- 4. Посчитать среднюю сумму заказа.
SELECT
    AVG(amount) AS avg_order_amount
FROM orders;


-- 5. Найти минимальную и максимальную сумму заказа.
SELECT
    MIN(amount) AS min_order_amount,
    MAX(amount) AS max_order_amount
FROM orders;


-- 6. Посчитать количество пользователей по каждому сегменту.
SELECT
    segment,
    COUNT(*) AS users_count
FROM users
GROUP BY segment
ORDER BY users_count DESC;


-- 7. Посчитать количество заказов по каждому пользователю.
-- Вывести: name, orders_count.
SELECT
    u.name,
    COUNT(o.order_id) AS orders_count
FROM users AS u
JOIN orders AS o ON u.user_id = o.user_id
GROUP BY u.user_id, u.name
ORDER BY orders_count DESC;


-- 8. Посчитать общую сумму заказов по каждому пользователю.
-- Вывести: name, total_amount.
-- Отсортировать по total_amount по убыванию.
SELECT
    u.name,
    SUM(o.amount) AS total_amount
FROM users AS u
JOIN orders AS o ON u.user_id = o.user_id
GROUP BY u.user_id, u.name
ORDER BY total_amount DESC;


-- 9. Посчитать средний чек по каждому пользователю.
-- Вывести: name, avg_order_amount.
SELECT
    u.name,
    AVG(o.amount) AS avg_order_amount
FROM users AS u
JOIN orders AS o ON u.user_id = o.user_id
GROUP BY u.user_id, u.name
ORDER BY avg_order_amount DESC;


-- 10. Найти пользователей, у которых общая сумма заказов больше 10000.
-- Использовать GROUP BY + HAVING.
SELECT
    u.name,
    SUM(o.amount) AS total_amount,
    COUNT(o.order_id) AS orders_count
FROM users AS u
JOIN orders AS o ON u.user_id = o.user_id
GROUP BY u.user_id, u.name
HAVING SUM(o.amount) > 10000
ORDER BY total_amount DESC;


-- 11. Посчитать общую сумму заказов по каждому сегменту.
-- Вывести: segment, total_amount.
SELECT
    u.segment,
    SUM(o.amount) AS total_amount,
    COUNT(o.order_id) AS orders_count
FROM users AS u
JOIN orders AS o ON u.user_id = o.user_id
GROUP BY u.segment
ORDER BY total_amount DESC;


-- 12. Найти сегменты, где средняя сумма заказа больше 10000.
-- Вывести: segment, avg_order_amount.
SELECT
    u.segment,
    AVG(o.amount) AS avg_order_amount
FROM users AS u
JOIN orders AS o ON u.user_id = o.user_id
GROUP BY u.segment
HAVING AVG(o.amount) > 10000
ORDER BY avg_order_amount DESC;