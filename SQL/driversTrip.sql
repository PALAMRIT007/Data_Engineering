You have two tables:
- drivers(driver_id, signup_date)
- trips(trip_id, driver_id, trip_date, fare)
Find all drivers who did not complete a single trip within 7 days of signing up.

-- same concet, table A me hai pr table B me nahi hai
-- after singup date he move forawrds each day, so >= singup date, 
-- and then we need to be in range of seven days, so < signup+7 days.

select d.driver_id
from drivers d 
left join trips t 
on d.driver_id = t.driver_id
and t.trip_date >= d.signup_date
and t.trip_date < dateadd(day,7,d.signup_date) 
where t.driver_id is null


select d.driver_id
from drivers d 
WHERE not exists (select 1 from trips t where d.driver_id = t.driver_id
AND t.trip_date >= d.signup_date
AND t.trip_date < d.signup_date + INTERVAL '7 days')