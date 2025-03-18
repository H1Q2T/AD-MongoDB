import os
import json
from pymongo import MongoClient
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")

# Conectar a MongoDB
client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]

# Función 1: Listar títulos y directores
def list_titles_and_directors():
    results = collection.find({}, {"title": 1, "director": 1, "_id": 0})
    return list(results)

# Función 2: Listar títulos y años ordenados por año
def list_titles_and_years_sorted():
    results = collection.find({}, {"title": 1, "year": 1, "_id": 0}).sort("year", 1)
    return list(results)

# Función corregida para buscar "professor" sin importar acentos y mayúsculas
def search_by_professor():
    query = {"summary": {"$regex": r"\bprofessor\b", "$options": "i"}}  # \b asegura que sea una palabra exacta
    results = collection.find(query, {"title": 1, "_id": 0})
    return list(results)


# Función 4: Mostrar título, año y reparto de series/películas posteriores a 2018
def list_recent_titles():
    query = {"year": {"$gt": 2018}}
    results = collection.find(query, {"title": 1, "year": 1, "cast": 1, "_id": 0})
    return list(results)

# Función 5: Añadir una nueva serie o película
def add_new_entry(title, year, director, cast, summary):
    new_entry = {
        "title": title,
        "year": int(year),
        "director": director,
        "cast": cast,  # Ya es una lista, no necesita split()
        "summary": summary
    }
    collection.insert_one(new_entry)
    return f"'{title}' added successfully!"


