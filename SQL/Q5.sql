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