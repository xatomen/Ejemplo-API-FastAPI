from fastapi import FastAPI, Depends, HTTPException  # Importa FastAPI, Depends y HTTPException del módulo fastapi
from sqlalchemy import create_engine  # Importa la función create_engine del módulo sqlalchemy
from sqlalchemy.orm import sessionmaker, Session  # Importa sessionmaker y Session del módulo sqlalchemy
from db import SessionLocal, Item  # Importa la clase Item y la función SessionLocal del módulo db

app = FastAPI()  # Crea una instancia de la aplicación FastAPI

def get_db():  # Define una función que retorna una sesión de la base de datos
    db = SessionLocal()  # Crea una sesión de la base de datos
    try:
        yield db  # Retorna la sesión de la base de datos
    finally:
        db.close()  # Cierra la sesión de la base de datos

@app.get("/")  # Define una ruta GET en la raíz ("/") de la aplicación
def read_root():  # Define una función que se ejecuta cuando se accede a la ruta raíz
    return {"Hello": "World"}  # Retorna un diccionario con un mensaje de saludo

@app.get("/items/{item_id}")  # Define una ruta GET que incluye un parámetro de ruta (item_id)
def read_item(item_id: int, db: Session = Depends(get_db)):  # Define una función que se ejecuta cuando se accede a la ruta /items/{item_id}
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item.id, "name": item.name}  # Retorna un diccionario con el item_id y el nombre del item