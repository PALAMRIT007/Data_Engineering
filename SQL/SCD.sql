SCD Type 2 practice question: load a dimension with history
Target table dim_customer (SCD Type 2). sk is an auto-increment surrogate key, effective_from is inclusive, effective_to is exclusive, and the open row has effective_to = '9999-12-31'.

sk	customer_id	name	city	effective_from	effective_to	is_current
1	        1	Asha	Pune	 2025-01-01	      9999-12-31	    Y
2	        2	Ravi	Delhi	 2025-01-01	      2026-03-01	    N
3	        2	Ravi	Gurgaon	 2026-03-01	      9999-12-31	    Y
4	        3	Meera	Mumbai	 2025-06-01	      9999-12-31	    Y
5	        4	Kiran	Chennai	 2025-09-01	      9999-12-31	    Y

Source table stg_customer (today’s batch, one row per customer):
Assuming only addressed getting changed
customer_id	name	city
    1	    Asha	Pune
    2	    Ravi	Noida
    3	    Meera	Bengaluru
    4	    Kiran	Chennai
    5	    Neha	Hyderabad
    6	    Arjun	Jaipur

-- first let me get all the new and changed data from source, and save it to staged
create or replace temp table staged as 
select s.customer_id, s.name, s.city
from stg_customer s 
left join dim_customer d        -- all should coming from source, inner willl remove the new cust_ids 
on s.customer_id = d.customer_id
and d.is_current = 'Y'
where d.customer_id is null   -- matlab new rows aayi hai, wo uthao, new customer
    or s.name is distinct from d.name        -- changed
   or s.city is distinct from d.city;

-- second i will expire the already present rows
update dim_customer d 
set effective_to = current_date,
    is_current = 'N'
from staged s 
where s.customer_id = d.customer_id
and d.is_current = 'Y'

-- third i will add all the rows from stage to dim with updated date and status cols
insert into dim_customer (customer_id, name, city,effective_from,effective_to, is_current)
select s.customer_id,
s.name,
s.city,
current_date,
'9999-12-31',
'Y'
from staged s

-- merge method
-- the idea is almost same, i will create a staged temp table, but this table wi;; have 2 rows for 
-- updated customer id and one row for new customer ids.
-- a flag will be used to distingush between them,
-- ex. changed row for c_id one row have flag as 'updated', and one row will have flag as 'insert'
-- and all new coming c_id will have flag of 'insert'


create or replace temp table staged as 
select s.customer_id, s.name, s.city, 'updated' as flag
from stg_customer s 
join dim_customer d        -- inner join to keep only updated one. which are present in both, sorce and target 
on s.customer_id = d.customer_id
and d.is_current = 'Y'
where s.name is distinct from d.name        -- changed
   or s.city is distinct from d.city;

union all

 
select s.customer_id, s.name, s.city, 'insert' as flag
from stg_customer s 
left join dim_customer d        -- all should coming from source, inner willl remove the new cust_ids 
on s.customer_id = d.customer_id
and d.is_current = 'Y'
where d.customer_id is null   -- matlab new rows aayi hai, wo uthao, new customer
    or s.name is distinct from d.name        -- changed , new versions
   or s.city is distinct from d.city;


merge into dim_customer d 
using staged s 
on s.customer_id = d.customer_id        -- c_id should be same
and d.is_current = 'Y'              -- taking only active records from dim table to update them
and s.flag = 'updated'               -- taking only those records from stage, which will get expire, NOTE* read below
when matched then 
update set
    effective_to = current_date(),
    is_current = 'N'
when not matched and s.flag = 'insert' then         -- this insert condition here is for defensive coding and readability
insert into dim_customer (customer_id, name, city,effective_from,effective_to, is_current)
values (s.customer_id,
s.name,
s.city,
current_date,
'9999-12-31',
'Y')







-- NOTE: these three condition, if evalutes to true, then it will enforce the when match section
-- if any condition getting false , we are moving them to insert section, 