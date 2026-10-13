
-- 1. customers
-- customer_id
-- customer_name
-- ------
-- orders
-- order_id
-- customer_id
-- order_date
-- amount

-- Question Find the top 5 customers by total revenue in the last 12 months.

-- Find customers who have never placed an order.


select c.customer_name, sum(o.amount) as total_revenue
from customers c 
join orders o 
on c.customer_id = o.customer_id
and o.order_date > dateadd(month, -12 , current_date)
group by c.customer_id
order by sum(o.amount) desc
limit 5

-- table a me hai pr table b me nahi hai
select c.customer_name
from customers c 
left join orders o 
on c.customer_id = o.customer_id
where o.customer_id is null

-- second question ke liye NOT EXISTS(safest, handle nulll values)

select c.customer_name
from customers c 
where not EXISTS (select 1 from orders o where c.customer_id = o.customer_id)