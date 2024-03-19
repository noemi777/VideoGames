## Endpoint VideoJuegos
Este ejercicio tecnico se compone de 5 endpoints: <br>
- Crear un objeto compuesto por un nombre del videojuego, la compañia de origen y la fecha de publicación. <br>
- Mostrar una lista de todos los videojuegos registrados. <br>
- Mostrar un solo elementro de la lista de videojuegos. <br>
- Editar los datos de un elemento de la lista de videojuegos. <br>
- Eliminar un elemento de la lista de videojuegos. <br> <br>

## Instalación
- Clonar el repositorio: <br>
git clone https://github.com/noemi777/VideoGames.git <br>
- Crear el ambiente virtual para python<br>
- Instalar los requirements <br>
pip install -r requirements.txt <br>
<br>

- Crear un archivo .env, con datos similares:<br>
SECRET_KEY = 'vidoejaus29ekk1isao43m20sdja1k23japs9d'<br> 
DEBUG = True  <br>
ALLOWED_HOSTS = *  <br>
DATABASE_URL= 'postgres://gamestest:43W0N1KUZp0pZuIP1LlzBH6A6eOlTDE5@dpg-cnqfg6la73kc739uogv0-a.oregon-postgres.render.com/demo_games' <br>
<br>
La conexión actual de la base de datos es remota, sin embargo, puede hacerse una configuración en el archivo settings.py para cambiar las propiedades de la DATABASES a una base de datos local<br>
<br>
Los datos anteriores pueden ser sustituidos de acuerdo a las necesidades. La base de datos es temporal, despues de un mes no estará disponible. <br>
<br>
- JSON<br>
<br>
{
"title":"MarioBross",
"company":"Nintendoo",
"release_date":"2021-03-01"
}
  
