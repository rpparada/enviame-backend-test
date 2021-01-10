use enviame;
SET SQL_SAFE_UPDATES = 0;

UPDATE employees
INNER JOIN countries ON employees.country_id = countries.id
INNER JOIN continents ON countries.continent_id = continents.id
SET 
    employees.salary = employees.salary * ((continents.anual_adjustment/100)+1)
WHERE
    employees.salary <= 5000