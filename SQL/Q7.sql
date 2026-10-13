-- customer_status
-- customer_id
-- status
-- updated_at

-- Question: Retrieve only the latest status for each customer.

-- this have limitation of not including other columns
select distinct customer_id,
first_value(status) over(partition by customer_id order by updated_at desc) as latest
from customer_status

-- method 2, ache wale hai

with rnked as (
    select *, 
    row_number() over(partition by customer_id order by updated_at desc) as rnk 
    from customer_status
)

select customer_name, status, updated_at
from rnked
where rnk = 1