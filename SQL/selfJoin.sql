-- Self join, anti-join and the NOT IN trap
-- employees :  emp_id	name	manager_id	dept_id	salary

-- (a) Self join. Return employees who earn more than their own manager, 
-- with employee, emp_salary, manager and mgr_salary.

-- see, emp me manager ko match karwana hai manager table ki emp id se, 
-- taaki agar emp(left) table me 2 emp ke same manager hai, 
-- to right (manager) se dono same records le paaye

select e.name as emp, e.salary emp_salary, m.name as manager, m.salary as manager_salary
from employees e 
join employees m 
on e.manager_id = m.emp_id
where e.salary > m.salary 


-- (b) Anti-join. Return the departments that have no employees: dept_id, dept_name
-- departments : dept_id	,dept_name

-- left me hai pr right me nai hai. --> left anti join hai yeh, so dont forget to put left join

select d.dept_name
from departments d 
left join employees e 
on d.dept_id = e.dept_id
where e.dept_id is null


-- not exits wala code
select d.dept_id, d.dept_name
from departments d
where not exists (
    select 1 from employees e  where d.dept_id = e.dept_id
)

-- For each department, the subquery checks whether any employee row matches. If none does, 
-- NOT EXISTS is true and the department is kept.
-- select 1 is a convention, since EXISTS only checks whether a row exists and ignores the selected columns.



-- part c

-- NOT IN with NULL

-- If the subquery returns even one NULL, NOT IN returns no rows.

-- Reason: x NOT IN (10, 20, NULL) means x<>10 AND x<>20 AND x<>NULL. The last part is UNKNOWN, 
-- so the whole condition is never TRUE, and WHERE keeps only TRUE rows.

-- IN is fine, because it uses OR (TRUE OR UNKNOWN = TRUE).

-- Fix: use NOT EXISTS (or LEFT JOIN ... IS NULL), or add WHERE col IS NOT NULL in the subquery.

-- wrong query, as the inner query might have the null values.

select d.dept_name
from departments d
where not exists (select 1 from employees e where e.dept_id = d.dept_id);