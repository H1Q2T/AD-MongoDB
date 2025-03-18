import json
import os
from pymongo import MongoClient
from dotenv import load_dotenv


# Cargar variables del archivo .env
load_dotenv()

# Obtener valores de las variables de entorno
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")

# Conectar a MongoDB Atlas
client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]

# Leer el archivo JSON y limpiar el campo "_id"
with open("datosAD.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Eliminar o convertir el campo "_id" incorrecto
for doc in data:
    if "_id" in doc:
        doc.pop("_id")  # Elimina el campo "_id" para que MongoDB genere uno automáticamente

# Insertar los datos en MongoDB
if isinstance(data, list):
    collection.insert_many(data)
else:
    collection.insert_one(data)

print("Datos insertados correctamente en MongoDB Atlas.")
