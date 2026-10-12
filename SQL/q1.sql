--  Q1: Identify customers who made purchases on exactly three different days in 
-- the last month. 

-- Purchase (customer, purchase_date)

with cnt as (
    select * , count(distinct purchase_date) over(partition by customer) as purchase_cnt
from Purchase 
where purchase_date > dateadd(month, -1, current_date)
)

select * 
from cnt
where purchase_cnt = 3