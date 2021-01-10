use enviame;
SET SQL_SAFE_UPDATES = 0;

DELETE FROM employees;
DELETE FROM countries;
DELETE FROM continents;

ALTER TABLE employees AUTO_INCREMENT=1;
ALTER TABLE countries AUTO_INCREMENT=1;
ALTER TABLE continents AUTO_INCREMENT=1;

insert into continents values (null, 'América', 4); 
insert into continents values (null, 'Europa', 5); 
insert into continents values (null, 'Asia', 6); 
insert into continents values (null, 'Oceanía', 6); 
insert into continents values (null, 'Africa', 5);

insert into countries values (null, 1, 'Chile'); 
insert into countries values (null, 1, 'Argentina'); 
insert into countries values (null, 1, 'Canadá'); 
insert into countries values (null, 1, 'Colombia'); 
insert into countries values (null, 2, 'Alemania'); 
insert into countries values (null, 2, 'Francia'); 
insert into countries values (null, 2, 'España'); 
insert into countries values (null, 2, 'Grecia'); 
insert into countries values (null, 3, 'India'); 
insert into countries values (null, 3, 'Japón'); 
insert into countries values (null, 3, 'Corea del Sur'); 
insert into countries values (null, 4, 'Australia');

insert into employees values (null, 1, 'Pedro', 'Rojas', 2000); 
insert into employees values (null, 2, 'Luciano', 'Alessandri', 2100); 
insert into employees values (null, 3, 'John', 'Carter', 3050); 
insert into employees values (null, 4, 'Alejandra', 'Benavides', 2150); 
insert into employees values (null, 5, 'Moritz', 'Baring', 6000); 
insert into employees values (null, 6, 'Thierry', 'Henry', 5900); 
insert into employees values (null, 7, 'Sergio', 'Ramos', 6200); 
insert into employees values (null, 8, 'Nikoleta', 'Kyriakopulu', 7000); 
insert into employees values (null, 9, 'Aamir', 'Khan', 2000); 
insert into employees values (null, 10, 'Takumi', 'Fujiwara', 5000); 
insert into employees values (null, 11, 'Heung-min', 'Son', 5100); 
insert into employees values (null, 12, 'Peter', 'Johnson', 6100);