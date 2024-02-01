# Создать API для получения списка фильмов по жанру. Приложение должно
# иметь возможность получать список фильмов по заданному жанру.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Movie с полями id, title, description и genre.
# Создайте список movies для хранения фильмов.
# Создайте маршрут для получения списка фильмов по жанру (метод GET).
# Реализуйте валидацию данных запроса и ответа.

import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
async def root():
    logger.info('Отработал GET запрос.')
    return {"message": "Hello World"}


class Movie(BaseModel):
    id: int
    title: str
    description: str
    genre: str


movies = [
    {'id': 1, 'title': 'title1', 'description': 'description1', 'genre': 'genre1'},
    {'id': 2, 'title': 'title2', 'description': 'description2', 'genre': 'genre2'},
    {'id': 3, 'title': 'title3', 'description': 'description3', 'genre': 'genre3'},
    {'id': 4, 'title': 'title4', 'description': 'description4', 'genre': 'genre4'},
    {'id': 5, 'title': 'title5', 'description': 'description5', 'genre': 'genre5'},
    {'id': 6, 'title': 'title6', 'description': 'description6', 'genre': 'genre6'},
    {'id': 7, 'title': 'title7', 'description': 'description7', 'genre': 'genre5'},
    {'id': 8, 'title': 'title8', 'description': 'description8', 'genre': 'genre8'},
]


@app.get("/movies/", response_model=list[Movie])
async def get_movies():
    logger.info('Отработал GET запрос.')
    return movies


@app.get("/movies/{genre}", response_model=Movie)
async def get_movies_by_genre(genre: str):
    for i in range(len(movies)):
        if movies[i]['genre'] == genre:
            logger.info('Отработал GET запрос.')
            return movies[i]
    raise HTTPException(status_code=404, detail="Movie not found")


@app.post("/movies/", response_model=list[Movie])
async def create_movie(movie: Movie):
    logger.info('Отработал POST запрос.')
    movies.append(movie)
    return movie


@app.put("/movies/{id}", response_model=Movie)
async def update_task(id: int, movie: Movie):
    for i in range(len(movies)):
        if movies[i]['id'] == id:
            movies[i] = movie
            logger.info(f'Отработал PUT запрос для movie id = {id}.')
            return movie
    return HTTPException(status_code=404, detail="Movie not found")


@app.delete("/movies/{id}")
async def delete_movie(id: int):
    for i in range(len(movies)):
        if movies[i]['id'] == id:
            del movies[i]
            logger.info('Отработал DELETE запрос.')
            return {'message': 'Movie deleted'}
            break
    raise HTTPException(status_code=404, detail="Movie not found")























