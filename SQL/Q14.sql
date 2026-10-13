-- inventory_snapshot
-- product_id
-- qty

-- transactions
-- product_id
-- qty_change

-- Question: Verify whether current inventory matches transaction history.

-- group each transaction
with agg_qty as (
    select product_id, sum(qty_change) as total_qty
from transactions
group by product_id
)

select coalesce(i.product_id,t.product_id) as product_id,
coalesce(i.qty, 0) as snapshot_qty,   --> remove coalesce if you want null instead of 0
coalesce(t.total_qty, 0) as transaction_qty, 
coalesce(i.qty-t.total_qty, i.qty,t.total_qty,0) as difference
from inventory_snapshot i 
full outer join agg_qty t 
on i.product_id = t.product_id
where coalesce(i.qty,0) <> coalesce(t.total_qty,0)

