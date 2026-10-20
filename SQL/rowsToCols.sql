Conditional aggregation (pivot) and HAVING
orders: order_id	,customer_id	,category	,amount

category : Electronics, Grocery, Fashion

select customer_id,
sum(case when category = 'Electronics' then amount else 0 end) as Electronics,
sum(case when category = 'Grocery' then amount else 0 end) as Grocery,
sum(case when category = 'Fashion' then amount else 0 end) as Fashion,
sum(amount) as total_spend
from orders
group by customer_id
having sum(amount) > 500
