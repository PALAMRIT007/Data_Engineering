--  Q1: Identify customers who made purchases on exactly three different days in 
-- the last month. 

-- Purchase (customer, purchase_date)

with cnt as (
    select * , count(distinct purchase_date) over(partition by customer) as purchase_cnt
from Purchase 
where purchase_date > dateadd(month, -1, current_date)
)

select distinct customer 
from cnt
where purchase_cnt = 3


-- Method 2
select customer 
from Purchase
where purchase_date > dateadd(month, -1, current_date)
group by customer
having count(distinct purchase_date) = 3