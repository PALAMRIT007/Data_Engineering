 SELECT *
FROM orders o

JOIN customers c

ON o.customer_id = c.customer_id

WHERE YEAR(o.order_date) = 2025;

 

Question:

1. Why might this be slow?
2. How would you improve it?
3. What indexes would you add?


-- optimised query
explain         --> to see the execution plan
select o.order_id, o.order_date, o.amount,
       c.customer_id, c.customer_name
from orders o
join customers c
  on o.customer_id = c.customer_id
where o.order_date >= '2025-01-01'
  and o.order_date <  '2026-01-01';


create index idx_orders_order_date on orders (order_date);   ---> range filter
create index idx_orders_customer_id on orders(customer_id);  -->better : filter + join key together


--  also very these things with execution plan, if what we expecting is following or not

Why not index everything

Each index costs storage.
Each insert, update, or delete must also update every index on that table, which slows writes.
Unused indexes are pure overhead.


 