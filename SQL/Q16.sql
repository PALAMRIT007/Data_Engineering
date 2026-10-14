-- Retention analysis

-- Table: User_Activity(user_id, activity_date).
-- signup  (user_id, signup_date)
-- Calculate the percentage of users who signed up on a given date and returned exactly one day later. 
-- Assume a signup table is available with user_id and signup_date. Avoid counting duplicate activities 
-- multiple times.

with signup_cnt as (
    select signup_date, count(distinct user_id) as first_cnt
    from signup 
    group by signup_date
),
next_day as (
    select s.signup_date , count(distinct u.user_id) as next_cnt
    from signup s 
    join User_Activity u 
    on s.user_id = u.user_id
    and u.activity_date = dateadd(DAY, 1, s.signup_date)
    group by signup_date
)

select signup_date, round(100.0*coalescend.(next_cnt,0)/nullif(sn.first_cnt,0),2) as retention_num
from signup_cnt sn 
join next_day nd 
on sn.signup_date = nd.signup_date


-- NOTE:
-- NULLIF(first_cnt, 0) returns NULL if first_cnt = 0; otherwise, it returns first_cnt unchanged.
-- NULLIF(expression1, expression2)  --> if expression1 == expression2, then return null
-- If the denominator becomes NULL, the division returns NULL instead of causing a divide-by-zero error.