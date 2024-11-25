----
- tags: #burpsuite #sql #sqli #web #sqlmap 
----

### Uso

	sqlmap -r request.req -p user --batch --dbs --dbms mysql

+ -r: Especifica un archivo. El archivo se genera a través de [[TechLexicon/Courses and Exams/Penetration Testing/Hack4U/BurpSuite]] con clic derecho sobre la petición
+ -p: Selecciona el campo de la petición sobre el que probar inyecciones (Ej: user=admin&password=admin)
+ --batch: No preguntar y proceder con la opción que [[TechLexicon/Courses and Exams/Penetration Testing/Hack4U/SQLMap]] considere conveniente.
+ --dbs:
+ --dbms: Especifica la base de datos que se está ejecutando en caso de que se conozca.
+ --proxy: En caso de querer pasar las peticiones a través de un proxy. Podemos interceptar las peticiones con [[TechLexicon/Courses and Exams/Penetration Testing/Hack4U/BurpSuite]] de la siguiente manera --proxy http://127.0.0.18080


