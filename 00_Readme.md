<h2 align=center>  Proyecto Individual I STEAM</h2>
# Proyecto de Sistema de Recomendación de Videojuegos para Steam

El presente proyecto se basa en la creación de APIs y un Sistema de recomendación de videojuegos para usuarios de la plataforma Steam. El objetivo es lograr un Producto Mínimo Viable (MVP) que permita ofrecer recomendaciones precisas y útiles a los usuarios, através de los .


## Descripción del Problema

Steam, una plataforma multinacional de videojuegos, carece de datos maduros para crear un sistema de recomendación efectivo. Los datos existentes son crudos, anidados y no automatizados, lo que hace que el trabajo del Data Scientist sea desafiante. El objetivo principal es desarrollar un sistema de recomendación que ofrezca sugerencias relevantes a los usuarios basadas en sus preferencias y reseñas de juegos.

## Propuesta de Trabajo

Para este proyecto se proporcionaron 3 datasets:
* _output_steam_games_ en que se almacena información de los videojuegos que hay en su plataforma, y contiene datos como fecha de lanzamiento, precio, desarollador, entre otros. 
* _australian_users_items_ en el que se almacena información del tiempo de juego de cada usuario para los diferentes juegos que ha jugado. 
* _australian_user_reviews_ en el que se almacena información de los usuarios e información de los reviews de los videojuegos que han jugado. 


### Transformaciones y Feature Engineering
- Se preparó cada dataset previo al Análisis Exploratorio, logrando la lectura de los mismos desanidando algunas columnas que se encontraban como listas de diccionarios o listas; así mismo eliminando columnas innecesarias, inputando con métodos estadísticos y/o eliminando valores nulos.
- Se creó la columna 'score' aplicando análisis de sentimiento a las reseñas de juegos mediante VADER (Valence Aware Dictionary and sEntiment Reasoner) que es una herramienta del NLP para categorizar la emoción detrás de un texto.
Posterior al trabajo con VADER, se definió una ponderación en la que derivado del resultado del análisis de sentimientos, se calificaba el review de la siguiente manera:  
    * 0 es para un review malo
    * 1 es para un review neutral
    * 2 es para un review bueno

    Puede consultar los notebooks de cada uno aqui:  
   [ETL_games](01a_ETL_games.ipynb), [ETL_items](01b_ETL_items.ipynb), [ETL_reviews_VADER](01c_ETL_reviews.ipynb) 

- Se crea el entorno virtual con el framework de FastApi para probar con consultas sencillas.

### Análisis Exploratorio de Datos (EDA)

- Se realizó el Análisis Exploratorio para explorar relaciones, outliers y patrones interesantes en los datos.

    Puede consultar el EDA [aqui](02_EDA.ipynb).


### Funciones de la API Realizadas
- `PlayTimeGenre(genero : str)`: Devuelve el año con más horas jugadas para un género específico.
- `UserForGenre(genero : str)`: Retorna el usuario con más horas jugadas para un género y la acumulación de horas por año.
- `UsersRecommend(anio : int)`: Ofrece el top 3 de juegos más recomendados por usuarios para un año dado.
- `UsersWorstDeveloper(anio : int)`: Proporciona el top 3 de desarrolladoras con juegos menos recomendados por usuarios para un año dado.
- `sentiment_analysis(developer : str)`: Analiza las reseñas de usuarios según la empresa desarrolladora y devuelve la cantidad total de registros categorizados por análisis de sentimiento.

Para cada consulta, se realizó un dataframe específico y se exportó en un parquet, esto para minimizar al máximo el peso de cada archivo y facilitar el deploy en render.

Puede consultar el notebook en los que se desarrolla a detalle estas funciones a continuación: [Funciones](03_dfAuxiliares.ipynb).


### Modelo de Aprendizaje Automático
- Se creó un sistema de recomendación ítem-ítem para ofrecer sugerencias de juegos similares basados en ítems o usuarios similares, para este punto se utilizó la similaridad del coseno y de igual manera, se creó un dataframe específico para esta consulta, buscando minimizar el peso de cada archivo. Para esto, primeramente se unificaron criterios de reommend y review en uno solo "calificación" en el que se dio la siguiente ponderación:  



Puede consultar el notebook en el que se desarrolla a detalle esta función a continuación: [Sistema_Recomendacion](04_SistemaDeRecomendacion.ipynb).


### Deployment 
- Se desarrolló la API con el framework FastAPI para ofrecer consultas específicas sobre los datos, para esto nos apoyamos del archivo [main.py](main.py) en donde se especifica cada consulta.

- Se deployó en Render para permitir la accesibilidad a la API, para esto se creó el documento [requirements.txt](requirements.txt) en el que se especifican los paquetes y librerias utlizados en el proyecto.

- Para el deploy de la API se seleccionó la plataforma Render que es una nube unificada para crear y ejecutar aplicaciones y sitios web, permitiendo el despliegue automático desde GitHub. Para esto se siguieron estos pasos:

    * Se generó un servicio nuevo en render.com, conectado al presente repositorio y utilizando requirements.txt como Runtime.
    * E l servicio queda corriendo [aqui](https://steam-pi-4c9l.onrender.com/docs). 

Como se indicó anteriormente, para el despliegue automático, Render utiliza GitHub y dado que el servicio gratuito cuenta con una limitada capacidad de almacenamiento, se realizó un repositorio exclusivo para el deploy.


### Video

- En el siguiente enlace pueden enconrtar el video, el cual proporciona un breve resumen con lo más imporante del proyecto [Video](https://youtu.be/3FRkXWo55Yw).


### Áreas de oportunidad

- El ETL fue realizado de una forma poco profunda, por lo que es probable que los resultados finales no sean 100% certeros o precisos; se recomienda en una segunda fase ahondar más en esta parte del proceso e incluso, complementar con datasets adicionales a los proporcionados para complementar 

- Se consideró que todos los reviews están en inglés ya que este idioma representa el 85% de los los idiomas en que se escriben opiniones; por lo que para una segunda fase del proyecto se tomarían en cuenta los demás idiomas.
