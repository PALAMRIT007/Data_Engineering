Finding and removing duplicates
cust_raw: id	,customer_id	,email	,updated_at

select customer_id, count(customer_id) as cnt
from cust_raw
group by customer_id
having count(customer_id) > 1

-- (b) Latest row per customer. Return one row per customer_id, keeping the row with the latest 
-- updated_at. If two rows tie on updated_at, keep the one with the higher id.

with ranked as (
select *,
row_number() over(partition by customer_id order by updated_at desc, id desc) as rnk
from cust_raw
)

select id, customer_id, email, updated_at
from ranked
where rnk = 1

-- (c) Delete duplicates. Write a DELETE that removes every row except the 
-- one chosen in (b). After it runs, the table should hold only ids 2, 4 and 6.

-- you cannot use a single CTE across multiple standalone SELECT queries. 
-- A Common Table Expression (CTE) is only valid and visible for the single SQL statement that 
-- immediately follows it. Once that statement executes, the CTE is out of scope and cannot be 
-- referenced again.

-- below query will generate error, 

delete from cust_raw
where id in (select id from ranked where rnk > 1)

--for solution, write an inner query, or define the cte again.
--below will work.
-- AFTER
delete from cust_raw
where id in (
    select id
    from (
        select id,
               row_number() over (partition by customer_id
                                  order by updated_at desc, id desc) as rn
        from cust_raw
    ) t
    where rn > 1
);

