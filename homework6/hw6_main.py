# Создать веб-приложение на FastAPI, которое будет предоставлять API для
# работы с базой данных пользователей. Пользователь должен иметь
# следующие поля:
# ○ ID (автоматически генерируется при создании пользователя)
# ○ Имя (строка, не менее 2 символов)
# ○ Фамилия (строка, не менее 2 символов)
# ○ Дата рождения (строка в формате "YYYY-MM-DD")
# ○ Email (строка, валидный email)
# ○ Адрес (строка, не менее 5 символов)
# API должен поддерживать следующие операции:
# ○ Добавление пользователя в базу данных
# ○ Получение списка всех пользователей в базе данных
# ○ Получение пользователя по ID
# ○ Обновление пользователя по ID
# ○ Удаление пользователя по ID
# Приложение должно использовать базу данных SQLite3 для хранения
# пользователей.

import sqlalchemy
import databases
from fastapi import FastAPI
from .models import UserIn, UserOut

DATABASE_URL = "sqlite:///homework6.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("surname", sqlalchemy.String(32)),
    sqlalchemy.Column("birthday", sqlalchemy.String(16)),
    sqlalchemy.Column("email", sqlalchemy.String(256)),
    sqlalchemy.Column("address", sqlalchemy.String(256))
)

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/fake_users/{count}")
async def fake_users(count: int):
    for i in range(count):
        query = users.insert().values(
            name=f'Имя{i}',
            surname=f'Фамилия{i}',
            birthday=f'2000-01-{i}',
            email=f'mail{i}@mail.ru',
            address=f'Адрес{i}'
        )
        await database.execute(query)
    return {"message": f"Добавлено {count} записей"}


@app.get("/")
async def root():
    return {"message": "Привет всем"}


@app.get("/users/")
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get("/users/{user_id}", response_model=UserIn)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.post("/users/", response_model=UserOut)
async def create_user(user: UserIn):
    query = users.insert().values(**user.model_dump())
    last_record_id = await database.execute(query)
    return {"id": last_record_id, **user.model_dump()}


@app.put("/users/{user_id}", response_model=UserIn)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {"message": "User deleted"}
