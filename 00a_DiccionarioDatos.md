## Diccionario de datos

### Steam_games.gz.json

| Columna | Descripción | Ejemplo |
| --- | --- | --- |
| publisher | Empresa publicadora del contenido | [Ubisoft,Dovetail Games - Trains,Degica]  
| genres | Género del contenido | [Action, Adventure, Racing, Simulation, Strategy] |  
| app_name | Nombre del contenido | [Warzone, Soundtrack, Puzzle Blocks] |  
| title | Título del contenido | [The Dream Machine: Chapter 4 , Fate/EXTELLA - Sweet Room Dream, Fate/EXTELLA - Charming Bunny] |  
| url | URL de publicación del contenido | http://store.steampowered.com/app/761140/Lost_Summoner_Kitty/ |  
| release_date | Fecha de lanzamiento | [2018-01-04] |
| tags | Etiquetas de contenido | [Simulation, Indie, Action, Adventure, Funny, Open World, First-Person, Sandbox, Free to Play] | 
| reviews_url | Reviews de contenido | http://steamcommunity.com/app/681550/reviews/?browsefilter=mostrecent&p=1 |  
| specs | Especificaciones | [Multi-player, Co-op, Cross-Platform Multiplayer, Downloadable Content] |  
| price | Precio del contenido | [4.99, 9.99, Free to Use, Free to Play] |  
| early_access | Acceso temprano | [False, True]  
| id | Identificador único de contenido | [761140, 643980, 670290] | 
|developer | Desarrollador | [Kotoshiro, Secret Level SRL, Poolians.com] |  


### User_reviews.gz.json

| Columna | Descripción | Ejemplo |
| --- | --- | --- |
|user_id | Identificador único de usuario | [76561197970982479, evcentric, maplemage]  
| user_url | URL perfil de usuario | http://steamcommunity.com/id/evcentric | 
| reviews | Esta columna tiene anidadas varias columnas: | funny, posted,last_edited, item_id, helpful, recommend, review. | 
| funny | Indica si otros usuarios encontraron gracioso ese review | 
| posted | Fecha en que se posteó el review |Posted September 8, 2013 |
| last_edited | Fecha de última edición | Edited September 10, 2013 | 
| item_id | Identificador único de usuario | 227300 | 
| helpful | Indica si el review fue útil o no | 0 of 1 people (0%) found this review helpful | 
| recommend | Indica si el usuario recomienda o no el videojuego | [False, True]
| review | Comentario que hace el usuario al videojuego | "For a simple (it's actually not all that simple but it can be!) truck driving Simulator, it is quite a fun and relaxing game. Playing on simple (or easy?) its just the basic WASD keys for driving but (if you want) the game can be much harder and realistic with having to manually change gears, much harder turning, etc. And reversing in this game is a ♥♥♥♥♥, as I imagine it would be with an actual truck. Luckily, you don't have to reverse park it but you get extra points if you do cause it is bloody hard. But this is suprisingly a nice truck driving game and I had a bit of fun with it." | 


### User_items.gz.json

| Columna | Descripción | Ejemplo |
| --- | --- | --- |
| user_id | Identificador único de usuario | [76561197970982479, evcentric, maplemage] | 
| user_url | URL perfil del usuario | http://steamcommunity.com/id/evcentric | 
| items | Items de usuario en formato Json. Esta columna tiene anidadas varias columnas: | item_id, item_name, playtime_forever, playtime_2weeks |
| item_id | Identificador único de contenido | 273350|
| item_name| Nombre del contenido | 'Evolve Stage 2'|
| playtime_forever| Tiempo de juego del usuario desde que se inscribió | 58 |
| playtime_2weeks'| Tiempo de juego del usuario en las últimas 2 semanas | 0 | 

