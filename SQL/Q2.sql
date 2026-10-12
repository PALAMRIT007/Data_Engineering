-- Q2: Find the top 2 highest-selling products for each category.

-- Tables: sales (productid, sale_amount), products (productid,category)

with rnk as (
    select s.productid, row_number() over(partition by category order by sale_amount desc) as ranks
    from sales s 
    join products p 
    on s.productid = p.productid
)

select * 
from rnk 
where ranks <=2

-- one catch, if productid is repeating multiple times , 
-- then we have to make a cte to aggregate those records

with sales_agg as (
    selct p.category, s.productid, sum(sale_amount) as total_amount
    from sales s 
    join products p 
    on s.productid = p.productid
    group by p.category, s.productid  --> dono pr karna hoga, taaki per product rows intact rahe
)