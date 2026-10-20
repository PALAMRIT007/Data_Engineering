-- Month-over-month change with LAG and a running total
-- sales : sale_id	,sale_date	,amount

-- question: 
-- month: the first day of the month
-- monthly_total: the sum of amount for that month
-- prev_month_total: the previous month’s total (NULL for the first month)
-- mom_pct_change: the percentage change vs the previous month, rounded to 1 decimal (NULL for the first month)
-- running_total: the cumulative total up to and including that month

with total as (
    select date_trunc('month', sale_date) as year_month, 
sum(amount) as monthly_total
from sales 
group by year_month
-- order by year_month       anyways it will not do anything here, final sorting is done on the final order nu clause.
)

select year_month, monthly_total,
lag(monthly_total,1) over(order by year_month) as prev_month_total,
round((monthly_total - lag(monthly_total,1) over(order by year_month))*100.0/nullif(lag(monthly_total,1) over(order by year_month),0),1) as mom_pct_change,
sum(monthly_total) over(order by year_month rows between UNBOUNDED PRECEDING and CURRENT row) as running_total
from total


-- A good follow-up interviewers like: 
-- lag looks at the previous row, not the previous calendar month. 
-- If a month has no sales (say there were none in February), it won’t appear in total at all, 
-- and March would compare against January. To handle that, you’d join against a calendar or date-spine 
-- table first so empty months show up with 0.


-- mention frame when order by column might have similer rows
-- When you write order by with no frame, the default is RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW. 
-- RANGE works on values, not row positions: “current row” means all rows with the same pay_date (its peers).