from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from models import MovieRequest, MovieResponse
from fetcher import fetch_omdb, fetch_tmdb_reviews
import asyncio

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API de agregação de filmes"}

@app.post("/movie", response_model=MovieResponse)
async def get_movie_info(request: MovieRequest):
    omdb_task = fetch_omdb(request.title, request.year)     
    result, = await asyncio.gather(omdb_task)  # Desempacota a tupla para pegar o dicionário

        
    formatted_response = f"Título: {result['titulo']}\nAno: {result['ano']}\nSinopse: {result['sinopse']}"
    return PlainTextResponse(formatted_response)
    #return MovieResponse(
    #    titulo=result["titulo"],  # Usa os dados do dicionário retornado
    #    ano=result["ano"],
    #    sinopse=result["sinopse"]
    #) 

"""
@app.post("/movie", response_model=MovieResponse)
async def get_movie_info(request: MovieRequest):
    omdb_task = fetch_omdb(request.title, request.year)
    tmdb_task = fetch_tmdb_reviews(request.title)
     
    sinopse, reviews = await asyncio.gather(omdb_task, tmdb_task)

    return MovieResponse(
        titulo=request.title,
        ano=request.year,
        sinopse=sinopse,
        reviews=reviews
    )
"""
