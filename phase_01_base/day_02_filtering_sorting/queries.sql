-- Day 02 SQL practice
-- Topic: filtering, sorting, limits, distinct values
-- Dataset: users + orders

-- 1. Вывести всех пользователей, отсортированных по возрасту по убыванию.
select user_id, name, age
from users
order by age desc;

-- 2. Вывести пользователей из Moscow или Ekaterinburg.
select user_id, name, city
from users
where city in ('Moscow', 'Ekaterinburg');

-- 3. Вывести пользователей в возрасте от 24 до 31 включительно.
select user_id, name, age
from users
where age between 24 and 31
order by age desc;

-- 4. Вывести пользователей из сегментов premium и student.
select user_id, name, segment
from users
where segment in ('premium', 'student')
order by segment;


-- 5. Вывести уникальные города из таблицы users.
select distinct city
from users;

-- 6. Вывести топ-3 самых дорогих заказа.
select u.user_id, u.name, o.product, o.amount
from users as u
join orders as o on u.user_id = o.user_id
order by o.amount desc
limit 3;

-- 7. Вывести заказы с суммой от 5000 до 80000 включительно,
-- отсортировать по сумме по убыванию.
select u.user_id, u.name, o.product, o.amount
from users as u
join orders as o on u.user_id = o.user_id
where o.amount between 5000 and 80000
order by o.amount desc;

-- 8. Вывести пользователей старше 25 лет, которые НЕ относятся к сегменту premium.
select user_id, name, segment
from users
where segment != 'premium' and age > 25
order by user_id asc;

-- 9. Через JOIN вывести name, city, product, amount
-- только для заказов дороже 5000.
select  u.name, u.city, o.product, o.amount
from users as u
join orders as o on u.user_id = o.user_id
where o.amount > 5000
order by o.amount desc;

-- 10. Через JOIN вывести name, segment, product, amount
-- только для пользователей segment IN ('premium', 'standard'),
-- отсортировать по amount по убыванию,
-- вывести только первые 5 строк.
select  u.name, u.segment, o.product, o.amount
from users as u
join orders as o on u.user_id = o.user_id
where segment IN ('premium', 'standard')
order by o.amount desc
limit 5;