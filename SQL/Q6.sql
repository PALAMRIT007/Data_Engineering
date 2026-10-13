--  transactions
-- account_id
-- transaction_date
-- amount

-- Question: Calculate the running balance after each transaction.

-- need  running total ,
-- bc range rehta hai default me
-- when order by mentione --> running sum(range between unbounded preceding and current row)
-- when order by not memntioned --> full partition(range between unbounded preceding and unbounded following)


-- edge case again, multiple transaction in single day, but question asks running for each transaction, so doesnt matter
select account_id, transaction_date,
sum(amount) over(partition by account_id order by transaction_date rows between unbounded preceding and current row) as running_balance
from transactions