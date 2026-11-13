trips(trip_id, driver_id, start_time, end_time)

Calculate the total time each driver spent on trips per day.

select driver_id, date_trunc(day, start_time), sum(end_time-start_time) as trip_min
from trips
group by driver_id, date_trunc(day, start_time) 
order by driver_id, date_trunc(day, date_trunc), trip_min

-- correct version -->

select driver_id,
       date_trunc('day', start_time) as trip_date,
       sum(datediff(minute, start_time, end_time)) as trip_min
from trips
where end_time is not null      -- maybe any runnning trip
group by driver_id, date_trunc('day', start_time)
order by driver_id, trip_date;

-- to handle the trips divided into two days, divide that row into 2 rows, then sum based on days, driver_id