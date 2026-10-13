customers
customer_id
email
phone

Question: Identify possible duplicate customers where either email or phone is duplicated.

select *
from customers
where email in  (select email from customers group by email having count(*)>1)
or 
phone in (select phone from customers group by phone having count(*)>1)



