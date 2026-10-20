--  user_logins
-- user_id
-- login_date

-- Question: Find users who logged in for at least 5 consecutive days.

-- isme yeh logic use hoga ki agar date se row nu ber minus kar rha to wo same date pr land karega
--  to agar continues login hia
--  aur m yeh karu, aur ur column pr groupby kardu to kaam ho jayega

-- always go woth edge cases
-- here, might be user have logged multiple times ina single day, then we might want to dedupe the table first
with user_grp as (
    select *, login_date - row_number() over(partition by user_id order by login_date) as grp
    from user_logins 
)

select distinct user_id 
from user_grp
group by user_id, grp
having count(*)>=5

-- distinct as one user might have 5 streak two times, then he will be repeated in the output.


-- same method, more informations


-- Longest consecutive-day streak (gaps and islands)
-- logins: user_id	,login_date

-- if logins table have multiple entries for same user_id and date , then dedupe it wil the simple step,
-- with dedupe as (select distinct user_id, login_date from logins) 
-- other alternate is using the dense_rank().

with groups as (
    select user_id, login_date
login_date - row_number()over(partition by user_id order by login_date) as grps
from logins
),

ranked as (
    select user_id, count(user_id), row_number() over(partition by user_id order by count(user_id) desc) as rnk,
    min(login_date) as streak_start,
    max(login_date) as streak_end       -- added if we need to add strat start and end dates also.
from groups
group by user_id, grps)

-- changed to row_number, as rank() can produce ties. 1,1,1,4, if filter for 1, it will give three rows.
select * from ranked where rnk =1

-- catch: if user have logged in multiple times in a day, then i can use dense rank, 
-- so that the order will not be braked.

