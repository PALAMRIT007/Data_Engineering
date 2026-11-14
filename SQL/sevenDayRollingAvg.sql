trips(trip_id, city_id, trip_date)

Calculate the daily trip count and its 7-day rolling average for each city.

with counted as (
    select date_trunc(day, trip_date) as trip_dates, city_id, count(*) as trip_cnt 
from trips
group by trip_dates, city
) 

select trip_dates, city, trip_cnt, average(trip_cnt) over(partition by city order by trip_dates rows between 6 preceding and current row) as cnt_avg
from counted 