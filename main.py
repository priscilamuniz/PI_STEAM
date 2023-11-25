import pandas as pd
import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq
from sklearn.metrics.pairwise import cosine_similarity
from fastapi import FastAPI
from sklearn.feature_extraction.text import TfidfVectorizer

app = FastAPI()

# Carga los datos parquet en un dataframe de pandas
df_PlaytimeGenre = pd.read_parquet('datos_parquet/df_PlayTimeGenre.parquet')
df = pd.read_parquet('datos_parquet/df_UserForGenre.parquet')
df_UsersRecommend = pd.read_parquet('datos_parquet/df_UsersRecommend.parquet')
df_UsersWorstDeveloper = pd.read_parquet('datos_parquet/df_UsersWorstDeveloper.parquet')
df_SentimentAnalysis = pd.read_parquet('datos_parquet/df_SentimentAnalysis.parquet')
df_recomendacion_juego = pd.read_parquet('')



@app.get('/PlayTimeGenre')
def PlayTimeGenre(genero:str):

    mascara = (df_PlaytimeGenre['genres'] == genero)
    df_PlayTimeGenre_sorted = df_PlaytimeGenre[mascara].sort_values(by='Total_horas_jugadas', ascending=False).head(1)                       

    year = df_PlayTimeGenre_sorted['released_year'].values[0]
    genre = df_PlayTimeGenre_sorted['genres'].values[0]

    return {f'Año de lanzamiento con más horas jugadas para el género {genre}': year}


@app.get('/UserForGenre')
def UserForGenre(genero: str):                     
    mascara = (df['genres'] == genero)
    df_UserForGenre = df[mascara]

    df_UserForGenre_sorted = df_UserForGenre.groupby('user_id')['Total_horas_jugadas'].sum().reset_index()                        
    user_max_playtime = df_UserForGenre_sorted.sort_values(by='Total_horas_jugadas', ascending=False).iloc[0]['user_id']

    df_UserGenreUser = df_UserForGenre[df_UserForGenre['user_id'] == user_max_playtime]                                           

    df_UserGenreUserByYear = df_UserGenreUser.groupby('released_year')['Total_horas_jugadas'].sum().reset_index()                 

    horas_por_anio = df_UserGenreUserByYear.to_dict(orient='records')                                                             

    return {f"Usuario con más horas jugadas para Género {genero}": user_max_playtime,"Horas jugadas": horas_por_anio}


@app.get('/UsersRecommend')
def UsersRecommend(anio:int):

    mascara = (df_UsersRecommend['year_posted'] == anio)   
    df_best_reviews_3 = df_UsersRecommend[mascara]

   # if df_best_reviews_3.empty:
   #     return 'No hay datos para el género especificado.'

    name_counts = df_best_reviews_3['app_name'].value_counts().head(3)
 
    resultados = []
    for puesto, (name, count) in enumerate(name_counts.items(), start=1):                            # Crear una lista de diccionarios con el formato solicitado
        resultados.append({f"Puesto {puesto}": name})

    return resultados


@app.get('/UsersWorstDeveloper')
def UsersWorstDeveloper(anio:int):

    mascara = (df_UsersWorstDeveloper['year_posted'] == anio)   
    df_worst_reviews_3 = df_UsersWorstDeveloper[mascara]
    developer_counts = df_worst_reviews_3['developer'].value_counts().head(3)
 
    resultados = []
    for puesto, (developer, count) in enumerate(developer_counts.items(), start=1):                            # Crear una lista de diccionarios con el formato solicitado
        resultados.append({f"Puesto {puesto}": developer})

    return resultados


@app.get('/SentimentAnalysis')
def SentimentAnalysis(developer:str):
    
    mascara = (df_SentimentAnalysis['developer'] == developer)
    df1 = df_SentimentAnalysis[mascara]

    pos = df1[df1['score'] == 2]['score'].sum()
    neu = df1[df1['score'] == 1]['score'].sum()
    neg = df1[df1['score'] == 0]['score'].sum()

    final = {f'{developer}:[Negative = {neg}, Neutral = {neu}, Positive = {pos}]'}

    return final


@app.get('/recomendacion_juego')
def recomendacion_juego(juego):
    '''
    Muestra una lista de juegos similares a un juego dado.

    Args:
        game (str): El nombre del juego para el cual se desean encontrar juegos similares.

    Returns:
        None: Esta función imprime una lista de juegos 5 similares al dado.

    '''
    similares = df_i_sim_cos.sort_values(by=juego, ascending=False).index[1:6]
    print(f'Los 5 juegos más similares a {juego} son:\n')
    for count, item in enumerate(similares, start=1):
        print(f'No. {count}: {item}')
