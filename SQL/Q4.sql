employees
employee_id
department_id
salary

Question: Find employees earning the second-highest salary in each department.

with sal_rnk as (
    select *, 
dense_rank() over(partition by department_id order by salary desc) as rnk
from employees e 
)

select department_id, employee_id, salary 
from sal_rnk
where rnk = 2

-- edge cases
-- what if a dept dont have a single user, 
-- or all the emp in same dept have the same salary, then our query will not return anything.
-- what if we want atleast one row per dept, 

with sal_rnk as (
    select
        employee_id,
        department_id,
        salary,
        dense_rank() over (partition by department_id order by salary desc) as rnk,
        count(distinct salary) over (partition by department_id) as max_rnk     -- agar per dept me ek hi salary hai to mac_rnk 1 hi hogi
    from employees
)
select department_id, employee_id, salary
from sal_rnk
where rnk = least(2, max_rnk);      -- agar 2 hai to 2, else 1 pr fall back hoga.
