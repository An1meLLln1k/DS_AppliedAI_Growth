-- Day 04 SQL practice
-- Topic: JOINs
-- Dataset: users + orders

-- 1. Через INNER JOIN вывести все заказы с именем пользователя.
-- Вывести: user_id, name, product, amount.
select 
u.user_id,
u.name,
o.product,
o.amount
from users as u
inner join orders as o on u.user_id = o.user_id;


-- 2. Через INNER JOIN вывести все заказы пользователей из Moscow.
-- Вывести: name, city, product, amount.
select 
u.name,
u.city,
o.product,
o.amount
from users as u
inner join orders as o on u.user_id = o.user_id
where u.city = 'Moscow';

-- 3. Через INNER JOIN вывести все заказы дороже 5000.
-- Вывести: name, segment, product, amount.
select 
u.name,
u.segment,
o.product,
o.amount
from users as u
inner join orders as o on u.user_id = o.user_id
where o.amount > 5000;

-- 4. Посчитать количество заказов по каждому пользователю.
-- Вывести: name, orders_count.
select 
u.name,
count (o.order_id) as orders_count
from users as u
inner join orders as o on u.user_id = o.user_id
group by u.user_id, u.name;

-- 5. Посчитать общую сумму заказов по каждому пользователю.
-- Вывести: name, total_amount.
select 
u.name,
sum (o.amount) as total_amount
from users as u
inner join orders as o on u.user_id = o.user_id
group by u.user_id, u.name;

-- 6. Через LEFT JOIN вывести всех пользователей и их заказы.
-- Вывести: name, product, amount.
select 
u.name,
o.product,
o.amount
from users as u
left join orders as o on u.user_id = o.user_id;


-- 7. Через LEFT JOIN посчитать количество заказов по каждому пользователю.
-- Вывести всех пользователей, даже если у кого-то 0 заказов.
SELECT
    u.name,
    COUNT(o.order_id) AS orders_count
FROM users AS u
LEFT JOIN orders AS o ON u.user_id = o.user_id
GROUP BY u.user_id, u.name
ORDER BY orders_count DESC;


-- 8. Найти пользователей без заказов.
-- Подсказка: LEFT JOIN + WHERE o.order_id IS NULL.
SELECT
    u.user_id,
    u.name
FROM users AS u
LEFT JOIN orders AS o ON u.user_id = o.user_id
WHERE o.order_id IS NULL;


-- 9. Посчитать общую сумму заказов по каждому городу.
-- Вывести: city, total_amount.
SELECT
    u.city,
    SUM(o.amount) AS total_amount
FROM users AS u
LEFT JOIN orders AS o ON u.user_id = o.user_id
GROUP BY u.city
ORDER BY total_amount DESC;


-- 10. Посчитать средний чек по каждому сегменту.
-- Вывести: segment, avg_order_amount.
SELECT
    u.segment,
    AVG(o.amount) AS avg_order_amount
FROM users AS u
LEFT JOIN orders AS o ON u.user_id = o.user_id
GROUP BY u.segment
ORDER BY avg_order_amount DESC;