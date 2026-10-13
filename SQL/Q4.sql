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
