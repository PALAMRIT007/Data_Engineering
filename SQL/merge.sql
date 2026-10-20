Upsert with MERGE
Target table dim_customer:

customer_id	name	city	updated_at
1	Asha	Pune	2026-01-05
2	Ravi	Delhi	2026-01-03
3	Meera	Mumbai	2026-01-10

Staging table stg_customer (today’s incoming batch):

customer_id	name	city	updated_at
2	Ravi	Gurgaon	2026-02-01
2	Ravi	Noida	2026-02-05
3	Meera	Mumbai	2026-01-10
4	Kiran	Chennai	2026-02-02

-- first lets dedupe the stg_customer, bcs duplication in source can throw error in snowflake

-- merging without deduping in Snowflake. If two source rows match the same target row (customer 2 twice), 
-- the merge is non-deterministic. By default (ERROR_ON_NONDETERMINISTIC_MERGE = TRUE) Snowflake fails with
-- a “duplicate row detected during DML action” error. If that parameter is FALSE, it silently applies 
-- one of the rows, chosen arbitrarily, so the result can differ between runs.

-- good odea but, snowflake mostly dont support with on top of delete or merge statements, so dedupe 
-- in a subquery

with dedupe_stg as (
    select * from stg_customer
    qualify row_number() over(partition by customer_id order by updated_at desc) = 1
)

--merge statement
merge into dim_customer d 
using (select * from stg_customer
    qualify row_number() over(partition by customer_id order by updated_at desc) = 1) s 
on d.customer_id = s.customer_id

when matched and (d.name is distinct from s.name or d.city is distinct from s.city)
then 
update set name = s.name, city = s.city, updated_at = s.updated_at

when not matched then 
insert (customer_id, name, city, updated_at)
values(s.customer_id, s.name, s.city, s.updated_at)


-- IS DISTINCT FROM is an ordinary comparison operator, like = or <>, 
-- so you can use it in a WHERE or CASE as well. Its only difference is how it treats NULL.