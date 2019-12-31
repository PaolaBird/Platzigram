***** Para el proyecto de platzigram los datos del superusuario son:
***** user = paola, pass = 05042018


Crear un entorno virtual de python:
* virtualenv nombre_entorno

Comando de ayuda para comandos de Django:
django-admin

Creación del proyecto:
*django-admin startproject platzigram .  "con el punto decimos que lo cree en el directorio donde estamos parados"

Con el comando "python manage.py" me imprimirá en pantalla aquellos comandos que puedo relizar de las diferentes aplicaciones que hay en Django por default

Para correr el servidor:
python manage.py runserver

Para crear una app:
python manage.py startapp users

Cada app que yo cree va a tener un archivo de admin, este archivo admin permite que yo pueda definir la forma en como va aprecer ese modelo en la vista de admin ("phpmyadmin")

Agregar las migraciones realizadas:
python manage.py migrate
(Con esta le decimos a django que busque los cambios que hay en los modelos definidos)

Para hacer las migraciones:
python manage.py makemigrations
(COn esto aplica los cambios a la BD)

Para acceder a la consola pero que tiene cargada las funcionalidades de django:

python manage.py shell

