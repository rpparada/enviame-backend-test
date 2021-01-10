use enviame;

SELECT 
    employees.first_name,
    employees.last_name,
    employees.salary,
    countries.name,
    continents.name,
    continents.anual_adjustment
FROM
    employees
        INNER JOIN
    countries ON (employees.country_id = countries.id)
        INNER JOIN
    continents ON (countries.continent_id = continents.id)