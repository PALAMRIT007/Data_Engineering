-- sales
-- sale_date
-- revenue

-- Question
-- Calculate:
-- • Current month revenue
-- • Previous month revenue
-- • Percentage growth

select 
sum(case when month(sale_date) = month(current_date) then revenue else 0 end ) as current_month,
sum(case when month(sale_date) = month(dateadd(month,-1,current_date)) then revenue else 0 end ) as previous_month,
((sum(case when month(sale_date) = month(current_date) then revenue else 0 end ))-(sum(case when month(sale_date) = month(dateadd(month,-1,current_date)) then revenue else 0 end )))*100.0/(sum(case when month(sale_date) = month(dateadd(month,-1,current_date)) then revenue else 0 end )) as percentage_growth
from sales
where sale_date >= dateadd(month, -2, current_date)  -->early filteration, so months will not interfere with other years



-- mthod 2
-- using date_trunc

-- date_trunc cuts a date or timestamp down to a chosen unit and sets everything smaller than that unit to its first value. In other words, it rounds down to the start of the period.

-- sql
-- date_trunc('month', date '2026-10-13')   -- 2026-10-01
-- date_trunc('year',  date '2026-10-13')   -- 2026-01-01
-- date_trunc('week',  date '2026-10-13')   -- start of that week (Monday in most engines)
-- date_trunc('day',   timestamp '2026-10-13 18:45:00')   -- 2026-10-13 00:00:00


with monthly as (
    select
        sum(case when sale_date >= date_trunc('month', current_date)
                  and sale_date <  dateadd(month, 1, date_trunc('month', current_date))
                 then revenue else 0 end) as current_month,                         -- CHANGED: date range, handles year
        sum(case when sale_date >= dateadd(month, -1, date_trunc('month', current_date))
                  and sale_date <  date_trunc('month', current_date)
                 then revenue else 0 end) as previous_month                         -- CHANGED: date range, handles year
    from sales
    where sale_date >= dateadd(month, -1, date_trunc('month', current_date))        -- CHANGED: only scan the two months
)
select current_month,
       previous_month,
       (current_month - previous_month) * 100.0
           / nullif(previous_month, 0) as percentage_growth                         -- CHANGED: divide by previous, guard zero
from monthly;