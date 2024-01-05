# API Tareas

## Instrucciones

##### Habilitar entorno virtual para terminal
Windows: `.\venv\Scripts\activate`
* Si la terminal no permite ejecutar script:

`Set-ExecutionPolicy RemoteSigned -Scope Process`

`.\venv\Scripts\activate`

Mac: `source venv/bin/activate`

##### Instalar librerias necesarias
`pip install -r requirements.txt`

##### Modificar archivo .env-template
Revisar instrucciones dentro de .env-template (omitir si no se cuenta con una openai api key)

##### Iniciar servidor
entrar a carpeta core `cd core`

`python manage.py runserver`

Usar VSCode Thunder Client Extension o Navegador a "http://localhost:8000/api/movies"

### Visualizar todas las peliculas en la Base de datos
GET a http://localhost:8000/api/movies


### Insertar pelicula en la Base de datos
POST a http://localhost:8000/api/movies
Ejemplo:
```
{
  "title": "The Shawshank Redemption",
  "director": "Frank Darabont",
  "year": 1994,
  "run_time_min": 142, 
  "imdb_rating": 9.3,
  "on_streaming": true,
  "box_office_world_usd": 28884716
}
```
Al insertar una pelicula, el programa intentará acceder a un modelo de openai con la api key en el archivo .env para generar un pequeño resumen.

### Visualizar pelicula especifica en la Base de datos
GET a http://localhost:8000/api/movies/{movie_id}
*Reemplazar {movie_id} con el id de la pelicula

### Eliminar pelicula especifica en la Base de datos
DELETE a http://localhost:8000/api/movies/{movie_id}
*Reemplazar {movie_id} con el id de la pelicula

### Visualizar los User Ratings de una pelicula en la Base de datos
GET a http://localhost:8000/api/movies/{movie_id}/ratings
*Reemplazar {movie_id} con el id de la pelicula

### Crear un User Rating de una pelicula en la Base de datos
POST a http://localhost:8000/api/movies/{movie_id}/ratings
*Reemplazar {movie_id} con el id de la tarea principal
Ejemplo:
```
{
  "user_name": "Eduardo",
  "user_rating": 9
}
```
Al mandar un User Rating, el programa calculará un promedio de todos los User Ratings para la pelicula y actualizará el campo 'user_rating'