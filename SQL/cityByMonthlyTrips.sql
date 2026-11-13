trips(trip_id, driver_id, rider_id, city_id, start_time, end_time)

-- Find the top 3 cities by number of trips for every month.

-- ALWAYS FORGETTING DESC IN ORDER BY CLAUSE.
-- mention that month() will merge all the years, if we want year wise segregations, then i can use date_trunc()

with monthly_trips as (select month(start_time) month_date,city_id,  count(trip_id) as trip_count 
from trips
group by month(start_time), city_id
),

ranked as (
    select *, row_number() over(partition by month_date order by trip_count desc) as rnk 
    from monthly_trips
)

select month_date, city_id
from ranked 
where rnk <=3
order by month_date, rnk


-- count(*) over count(trip_id): marginally cheaper, since it skips the null check on trip_id. 
-- Same result if trip_id is non-null (it should be, as a PK).

-- count is reserved word, lets use monthly_trips
