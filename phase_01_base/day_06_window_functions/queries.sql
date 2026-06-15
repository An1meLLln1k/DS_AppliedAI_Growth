-- Day 06 SQL practice
-- Topic: window functions
-- Dataset: users + orders

-- 1. Для каждого заказа вывести:
-- order_id, user_id, product, amount,
-- а также общую сумму всех заказов пользователя через SUM() OVER.

SELECT
    o.order_id,
    o.user_id,
    o.product,
    o.amount,
    SUM(o.amount) OVER (
        PARTITION BY o.user_id
    ) AS total_sum_by_user
FROM orders AS o
ORDER BY o.user_id, o.amount DESC;


-- 2. Для каждого заказа вывести:
-- order_id, user_id, product, amount,
-- а также количество заказов пользователя через COUNT() OVER.
SELECT
    o.order_id,
    o.user_id,
    o.product,
    o.amount,
    COUNT(o.order_id) OVER (
        PARTITION BY o.user_id
    ) AS orders_count_by_user
FROM orders AS o
ORDER BY o.user_id, o.amount DESC;

-- 3. Для каждого заказа вывести:
-- order_id, user_id, product, amount,
-- а также средний чек пользователя через AVG() OVER.
SELECT
    o.order_id,
    o.user_id,
    o.product,
    o.amount,
    AVG(o.amount) OVER (
        PARTITION BY o.user_id
    ) AS avg_amount_by_user
FROM orders AS o
ORDER BY o.user_id, o.amount DESC;

-- 4. Пронумеровать все заказы по убыванию amount.
-- Вывести: order_id, product, amount, row_number.
SELECT
    order_id,
    product,
    amount,
    row_number() over(order by amount desc) as row_number
FROM orders AS o;

-- 5. Пронумеровать заказы внутри каждого пользователя по убыванию amount.
-- Вывести: user_id, order_id, product, amount, order_rank.
SELECT
    u.user_id,
    o.order_id,
    o.product,
    o.amount,
    ROW_NUMBER() OVER (
        PARTITION BY u.user_id
        ORDER BY o.amount DESC
    ) AS order_rank
FROM orders AS o
JOIN users AS u ON u.user_id = o.user_id
ORDER BY u.user_id, order_rank;

-- 6. Через RANK() сделать рейтинг заказов по amount среди всех заказов.
-- Вывести: order_id, product, amount, amount_rank.
SELECT
    o.order_id,
    o.product,
    o.amount,
    rank() over(order by o.amount desc) as amount_rank
FROM orders AS o;


-- 7. Через CTE + ROW_NUMBER() найти самый дорогой заказ каждого пользователя.
-- Вывести: user_id, name, product, amount.
with most_expensive_order as (
    select u.user_id, u.name,
    o.product, o.amount,
    row_number() over(partition by u.user_id order by o.amount desc) as rn
    from users as u
    join orders as o on u.user_id = o.user_id
)
select user_id, name,
    product, amount
from most_expensive_order
where rn = 1
order by amount desc;
-- 8. Через JOIN вывести заказы с именем пользователя,
-- и добавить total_amount пользователя через SUM() OVER.
-- Вывести: name, product, amount, total_amount.
SELECT
    u.name,
    o.product,
    o.amount,
    SUM(o.amount) OVER (
        PARTITION BY u.user_id
    ) AS total_amount
FROM orders AS o
JOIN users AS u ON u.user_id = o.user_id
ORDER BY u.name, o.amount DESC;


-- 9. Через JOIN вывести заказы с именем пользователя,
-- и добавить номер заказа пользователя по убыванию amount.
-- Вывести: name, product, amount, order_number.
SELECT
    u.name,
    o.product,
    o.amount,
    ROW_NUMBER() OVER (
        PARTITION BY u.user_id
        ORDER BY o.amount DESC
    ) AS order_number
FROM orders AS o
JOIN users AS u ON u.user_id = o.user_id
ORDER BY u.name, order_number;


-- 10. Через CTE найти топ-1 самый дорогой заказ в каждом сегменте.
-- Вывести: segment, name, product, amount.
with most_expensive_order as (
    select u.segment, u.name,
    o.product, o.amount,
    row_number() over(partition by u.segment order by o.amount desc) as rn
    from users as u
    join orders as o on u.user_id = o.user_id
)
select segment, name,
    product, amount
from most_expensive_order
where rn = 1
order by amount desc;