-- orders:
-- order_id
-- order_items
-- products


-- Question: Find products frequently purchased together.


-- NOTE: 
-- whenever using order by, always reason for the asc or desc, i make lot of mistakes bcoz of it.

with pdt_pairs as (
    select o1.products as p1, o2.products as p2
from orders o1
join orders o2 
on o1.order_id = o2.order_id
where o1.products<o2.products
)


select p1,p2, count(*) as cnt
from pdt_pairs
group by p1,p2 
having cnt >0     --> if mentioned this, then use it, otherwise just go with order by
order by cnt desc