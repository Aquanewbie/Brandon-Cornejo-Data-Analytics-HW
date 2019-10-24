--1. List the following details of each employee: employee number, last name, first name, gender, and salary.
select * from employees
select * from salaries
-- Use Join to find employee number, last name, first name, gender, and salary
SELECT employees.emp_no, employees.last_name, employees.first_name, employees.gender, salaries.salary
From employees
INNER JOIN salaries on 
salaries.emp_no=employees.emp_no

--2. List employees who were hired in 1986.
SELECT employees.emp_no, employees.first_name, employees.last_name, employees.hire_date
From employees
WHERE employees.hire_date LIKE '1986%';

--3. List the manager of each department with the following information: /
--department number, department name, the manager's employee number, /
--last name, first name, and start and end employment dates.

select * from dept_manager
select * from departments
select * from employees

SELECT departments.dept_no, departments.dept_name, employees.emp_no, employees.last_name, employees.first_name, employees.hire_date, dept_manager.from_date, dept_manager.to_date 
From dept_manager
INNER JOIN departments on 
departments.dept_no=dept_manager.dept_no
INNER JOIN employees on 
employees.emp_no=dept_manager.emp_no

-- 4. List the department of each employee with the following information: /
--employee number, last name, first name, and department name.
select * from dept_emp

Select departments.dept_name, dept_emp.dept_no, employees.emp_no, employees.last_name, employees.first_name
From dept_emp
INNER JOIN departments on 
departments.dept_no=dept_emp.dept_no
INNER JOIN employees on 
employees.emp_no=dept_emp.emp_no
ORDER BY dept_no ASC

--5. List all employees whose first name is "Hercules" /
--and last names begin with "B."

SELECT employees.emp_no, employees.first_name, employees.last_name
From employees
WHERE employees.first_name LIKE 'Hercules' and employees.last_name LIKE 'B%';

--6. List all employees in the Sales department, including their /
--employee number, last name, first name, and department name.
Select departments.dept_name, employees.emp_no, employees.last_name, employees.first_name
From dept_emp
INNER JOIN departments on 
departments.dept_no=dept_emp.dept_no
INNER JOIN employees on 
employees.emp_no=dept_emp.emp_no
WHERE dept_name = 'Sales'
ORDER BY emp_no ASC;

--7. List all employees in the Sales and Development departments,/
--including their employee number, last name, first name, and department name.
Select departments.dept_name, employees.emp_no, employees.last_name, employees.first_name
From dept_emp
INNER JOIN departments on 
departments.dept_no=dept_emp.dept_no
INNER JOIN employees on 
employees.emp_no=dept_emp.emp_no
WHERE dept_name = 'Sales' or dept_name = 'Development'
ORDER BY emp_no ASC;

--8. In descending order, list the frequency count of employee last names, 
--i.e., how many employees share each last name.
SELECT count(emp_no), last_name
From employees
Group by last_name
ORDER BY count(emp_no) desc;

