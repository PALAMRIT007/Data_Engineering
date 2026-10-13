-- customer_history
-- customer_id
-- address
-- effective_from
-- effective_to

-- Question: Determine a customer's address on a given date.
-- given date is given_date

select customer_id, address
from customer_history
where effective_from <= given_date
and coalesce(effective_to,current_date) >= given_date      --> this get falied if given_date > current_date
and customer_id = id


-- method 2

select customer_id, address 
from customer_history 
where effective_from <= given_date 
and (effective_to is null or effective_to >= given_date)
and customer_id = id



