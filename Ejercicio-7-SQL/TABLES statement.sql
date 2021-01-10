CREATE TABLE countries (
    id INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
    continent_id INT(11) NOT NULL,
    name VARCHAR(25) NOT NULL,
    PRIMARY KEY (id)
);
CREATE TABLE continents (
    id INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(25) NOT NULL,
    anual_adjustment INT(11) NOT NULL,
    PRIMARY KEY (id)
);
CREATE TABLE employees (
    id INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
    country_id INT(11) NOT NULL,
    first_name VARCHAR(25) NOT NULL,
    last_name VARCHAR(25) NOT NULL,
    salary INT(11) NOT NULL,
    PRIMARY KEY (id)
);