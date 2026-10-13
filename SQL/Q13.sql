-- 11. invoice
-- invoice_no

-- Question: Find missing invoice numbers.

-- anti join approach, recursive approach likhi hai
with recursive nums as (
    select min(invoice_no) as n from invoice
    union all
    select n+1
    from nums
    where n+1 < (select max(invoice_no) from invoice) 
)

-- anti join
select n as missing_nums
from nums 
where not exists (select 1 from invoice v  where v.invoice_no = nums.n) 