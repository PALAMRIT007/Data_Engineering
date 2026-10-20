Semi-structured JSON with FLATTEN

Table raw_events (payload is a Snowflake VARIANT column):

event_id	payload
1	        {"user": {"id": 101, "name": "Asha"}, "items":  [{"sku": "A1", "qty": 2, "price": 50}, {"sku": "B2", "qty": 1, "price": 120}]}
3	        {"user": {"id": 103, "name": "Meera"}, "items": []}
2	        {"user": {"id": 102, "name": "Ravi"}, "items":  [{"sku": "A1", "qty": 1, "price": 50}]}

(a) Return one row per event with typed columns: event_id, user_id (integer),

select event_id,
payload:user.id::int as user_id,
payload:user.name::string as user_name
from raw_events

--another way   --> payload['user']['id']::int       -- bracket form

-- (b) Return one row per item: event_id, sku, qty, price, line_total (qty * price).


select event_id,
f.value:sku::string as sku,
f.value:qty::int as qty,
f.value:price::int as price,
f.value:qty::int * f.value:price::int as line_total
from raw_events,
lateral flatten(input => payload.items, outer => true) f

-- C, outer => true, will make the empty list flattned as null, so that event_id will not be missed.

-- (d) Total revenue per sku, highest first.

select 
f.value:sku::string as sku,
sum(f.value:qty::int * f.value:price::int) as total_revenue
from raw_events,
lateral flatten(input => payload:items, outer => true) f
group by f.value:sku::string
order by sum(f.value:qty::int * f.value:price::int) desc
