# enviame-backend-test
Backend Test: Desafío Envíame


### Ejercicio 1: Docker
Se creó un ambiente docker con python (3.7-alpine). Docker compose es el encargado de levantar los servicios de aplicación web (web) y base de datos (postgres:10-alpine)

### Ejercicio 2: API REST + CRUD
Utilice el ambiente creado en el ejercicio 1 para desarrollar la API. En esta api no solo se implementó CRUD para el modelo Empresas, también se creó un manejo básico de usuarios (crear, editar y generación de token). Para las pruebas se integró con Travis-CI. La metodología utilizada fue TDD (personalmente me gusta mucho), por lo tanto encontrarán, en las librerías de tests, pruebas que fueron creadas con anticipación a las implementación de las nuevas funciones.
* http://0.0.0.0:8000/api/empresa/ - Empresas
* http://0.0.0.0:8000/api/empresa/empresas/ - Listado/Creacion de Empresas
* http://0.0.0.0:8000/api/user/create/ - Crear usuarios
* http://0.0.0.0:8000/api/user/me/ - Perfil Usuario
* http://0.0.0.0:8000/api/user/token/ - Solicitar token

### Ejercicio 3: Análisis + Desarrollo
Para realizar este AD utilice python (jupyter notebook y pipenv) para implementar las funciones solicitadas. Para dar vuelta el texto utilice herramientas propias del python (slicing and indexing) y también desarrollé un función propia.

### Ejercicio 4: Consumo API Envíame para la creación de un envío
Utilicé el ambiente creado en el ejercicio 1 para consumir la API Enviame. Para esto desarrollé una aplicación web que crea, lista y revisa envíos. El formulario de creación de envío está respaldado en un modelo (base de datos) que antes de salvar consume la API Enviame, espera respuesta y la salva en la tabla junto al formulario.
* http://0.0.0.0:8000/enviame/ - Lista de envios
* http://0.0.0.0:8000/enviame/envios/'slug'/ - Revisa envio
* http://0.0.0.0:8000/enviame/crear - Crea envio

### Ejercicio 5: Análisis + Desarrollo
Para realizar este AD utilice python (jupyter notebook y pipenv) para implementar las funciones solicitadas.
Se crearon dos funciones
num_div: determina el número de divisores para numero ingresado retornando la cantidad encontrada
create_fibonacci_list: creador de serie de fibonacci desde 0 al numero limite entregado como parámetro de entrada para la búsqueda de divisores
Lamentablemente este algoritmo demora mucho en buscar 1000 divisores para un número de la serie fibonacci. Por lo tanto deje el límite en 100.

### Ejercicio 6: Análisis + Desarrollo Aplicado a Negocio
Para realizar este AD utilice python (jupyter notebook) para implementar las funciones solicitadas.
Para calcular el tiempo de entrega por sobre los 500 se utilizó una función recursiva (tiempo_entrega_entrega_dias).

### Ejercicio 7: SQL
Para realizar este ejercicio se utilizó mysql y mysql workbench. Se creó una base de datos (schema) llamada “enviame”.
Descripción de archivos:
* LOAD statement.sql: Limpia tablas, define inicio de índices en 1 y carga datos.
* SELECT statement.sql: Consulta global de las tablas (se utilizó para crear archivos antes.csv y despues.csv).
* TABLES statement.sql: Creación de tablas.
* UPDATE statement.sql: Aplica los cambio solicitados en el ejercicio.
* antes.csv: Descarga global de las tablas antes de los cambios.
* despues.csv: Descarga global de las tablas después de los cambios.
