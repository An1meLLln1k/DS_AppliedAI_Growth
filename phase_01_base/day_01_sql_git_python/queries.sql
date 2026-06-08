-- Day 01 SQL practice
-- Dataset: users + orders

-- 1. Вывести всех пользователей из Moscow.
SELECT *
FROM users
WHERE city = 'Moscow';


-- 2. Вывести пользователей старше 25 лет.
SELECT *
FROM users
WHERE age > 25;


-- 3. Посчитать количество пользователей по городам.
SELECT
    city,
    COUNT(*) AS users_count
FROM users
GROUP BY city;


-- 4. Через JOIN вывести:
-- name, city, product, amount
SELECT
    u.name,
    u.city,
    o.product,
    o.amount
FROM users AS u
JOIN orders AS o ON u.user_id = o.user_id;


-- 5. Посчитать общую сумму заказов по каждому пользователю:
-- name, total_amount
-- Отсортировать по total_amount по убыванию.
SELECT
    u.name,
    SUM(o.amount) AS total_amount
FROM users AS u
JOIN orders AS o ON u.user_id = o.user_id
GROUP BY u.user_id, u.name
ORDER BY total_amount DESC;


-- 6. Найти пользователей, у которых сумма заказов больше 10000.
-- Используй GROUP BY + HAVING.
SELECT
    u.name,
    SUM(o.amount) AS total_amount
FROM users AS u
JOIN orders AS o ON u.user_id = o.user_id
GROUP BY u.user_id, u.name
HAVING SUM(o.amount) > 10000
ORDER BY total_amount DESC;


-- 7. Добавить колонку customer_level через CASE WHEN:
-- если сумма заказов >= 50000, то 'high_value'
-- если сумма заказов >= 10000, то 'medium_value'
-- иначе 'low_value'
SELECT
    u.name,
    SUM(o.amount) AS total_amount,
    CASE
        WHEN SUM(o.amount) >= 50000 THEN 'high_value'
        WHEN SUM(o.amount) >= 10000 THEN 'medium_value'
        ELSE 'low_value'
    END AS customer_level
FROM users AS u
JOIN orders AS o ON u.user_id = o.user_id
GROUP BY u.user_id, u.name
ORDER BY total_amount DESC;