
-- v_art database

USE v_art;

-- Question 1
select artfile
from artwork
where period = "Impressionism";

-- Question 2
select title, keyword
from artwork a
	join artwork_keyword ak
     on a.artwork_id = ak.artwork_id
     join keyword k
     on k.keyword_id = ak.keyword_id
where keyword like "flower%";

-- Question 3
select fname, lname, title
from artwork a
	right join artist ar 
    on a.artist_id = ar.artist_id;

-- Magazine Database
use magazine;

-- Question 4
select magazineName, subscriberLastName, subscriberFirstName
from magazine m
	join subscription s
    on m.magazineKey = s.magazineKey
    join subscriber su
    on s.subscriberKey = su.subscriberKey
order by magazineName;

-- Question 5
select magazineName
from magazine m
	join subscription s
    on m.magazineKey = s.magazineKey
    join subscriber su
    on s.subscriberKey = su.subscriberKey
where subscriberFirstName = "Samantha";

-- Employee Database
use employees;

-- Question 6
select e.first_name,  e.last_name
from employees e
	join dept_emp de
	on e.emp_no = de.emp_no
	join departments dpt
	on de.dept_no = dpt.dept_no
where dept_name = 'Customer Service'
order by last_name
limit 5;

-- Question 7
select first_name, last_name,dept_name, salary, s.from_date
from employees e
	join salaries s
    on e.emp_no = s.emp_no
    join dept_emp de
	on e.emp_no = de.emp_no
	join departments dpt
	on de.dept_no = dpt.dept_no
where first_name = "Berni" and last_name = "Genin"
order by from_date desc
limit 1;
    
-- Sumary Queries
-- bike database
use bike;

-- Question 8
select round(avg(quantity))
from stock;

-- Question 9
select product_name
from product p
	join stock s
    on p.product_id = s.product_id
order by quantity, product_name
limit 13;

-- Question 10
select category_name, st.store_name, sum(quantity)
from product p
	join category c
    on p.category_id = c.category_id
    join stock s
    on p.product_id = s.product_id
    join store st
    on s.store_id = st.store_id
where st.store_id = 2
group by category_name
order by sum(quantity);

-- employees database
use employees;

-- Question 11
select count(emp_no) as NUmbers_of_employees
from employees;

-- Question 12
select dept_name, format(avg(salary), 2) as avarage_salary
from employees e
	join salaries s
    on e.emp_no = s.emp_no
    join dept_manager dm
    on e.emp_no = dm.emp_no
    join departments d
    on dm.dept_no = d.dept_no
group by dept_name
having avg(salary) < 60000
order by avarage_salary desc;

-- Question 13
select dept_name, count(gender) as Number_of_Female
from employees e
	join dept_emp de
    on e.emp_no = de.emp_no
    join departments d
    on de.dept_no = d.dept_no
Where gender = "F"
group by dept_name
order by dept_name;
    