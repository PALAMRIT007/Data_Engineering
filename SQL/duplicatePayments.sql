payments(payment_id, driver_id, amount, updated_at, status)

Find duplicate payment records and retain only the latest record for each payment_id.

with ranked as (
    select * , row_number() over(partition by payment_id order by updated_at desc nulls last) as rnk
from payments
)

select *
from ranked 
where rnk = 1

--snowflake shorcut

select * from payments
qualify row_number() over (partition by payment_id order by updated_at desc) = 1;


--to list down the duplicates, just use the count-having query
select payment_id, count(*) as dup_count
from payments
group by payment_id
having count(*)>1