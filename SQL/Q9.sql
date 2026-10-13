-- orders
-- order_id
-- customer_id
-- order_date 
-- status

-- status:
-- PLACED
-- SHIPPED
-- DELIVERED
-- CANCELLED

-- Question: Calculate cancellation rate by month.

-- NOTE: 
-- In standard SQL (Snowflake, PostgreSQL, SQL Server), double quotes mean an identifier 
-- like a column name, so "CANCELLED" is read as a column and errors. String literals 
-- need single quotes: 'CANCELLED'. MySQL accepts double quotes, but single quotes work everywhere.


--  can multiply with 100.0 to get a decimal value


select month(order_date) as "month", 
 
sum(case when status = "CANCELLED" then 1 else 0 end)*100/count(*)  as cancel_rate
from orders
group by month(order_date) 
order by month(order_date)     -- order lga dena chchiye , acha lagta hai
