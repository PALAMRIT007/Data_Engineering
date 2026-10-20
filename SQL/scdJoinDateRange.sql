SCD Type 2 point-in-time join
Dimension table dim_customer_scd keeps the history of each customer’s city. 
valid_from is inclusive, valid_to is exclusive, and the current row has valid_to = '9999-12-31'.

dim_customer_scd
sk	customer_id	city	valid_from	valid_to
1	1	        Pune	2025-01-01	2026-02-01
2	1	        Mumbai	2026-02-01	9999-12-31
3	2	        Delhi	2025-06-01	9999-12-31

Fact table orders:

order_id	customer_id	order_date	amount
101	                1	2026-01-15	100
102	                1	2026-02-01	200
103	                1	2026-03-10	150
104	                2	2026-01-20	80
105	                2	2025-05-01	60

-- (a)Point-in-time join. Return every order with the city the customer lived in on the order date: 
-- order_id, order_date, amount, city. Every order must appear.

select * 
from orders o 
left join dim_customer_scd d 
on o.customer_id = d.customer_id
where o.order_date between d.valid_from and d.valid_to

-- using where , it is filtering after the join, to filter before the join use and after on 
-- between clause take both the values inclusive. 
select o.order_id, o.order_date, o.amount, d.city
from orders o 
left join dim_customer_scd d 
on o.customer_id = d.customer_id
and o.order_date >= d.valid_from
and o.order_date < d.valid_to
order by o.order_id

-- (b) Revenue by historical city. Using the result of (a), return city and total_amount, 
-- with NULL shown as 'Unknown'.

with joined as (
    select  o.amount, 
case when d.city is null then 'Unknown' else d.city end as new_city
-- coalesce(d.city, 'Unknow') as new_city       same thing, no need to write this long syntax as above
from orders o 
left join dim_customer_scd d 
on o.customer_id = d.customer_id
and o.order_date >= d.valid_from
and o.order_date < d.valid_to
-- order by o.order_id      never use order by inside a cte, as it have no impact on final output.
)

select new_city, sum(amount) as total_amount
from joined 
group by new_city
order by new_city