from fastapi import FastAPI  # Importa la clase FastAPI del módulo fastapi

app = FastAPI()  # Crea una instancia de la aplicación FastAPI

@app.get("/")  # Define una ruta GET en la raíz ("/") de la aplicación
def read_root():  # Define una función que se ejecuta cuando se accede a la ruta raíz
    return {"Hello": "World"}  # Retorna un diccionario con un mensaje de saludo

@app.get("/items/{item_id}")  # Define una ruta GET que incluye un parámetro de ruta (item_id)
def read_item(item_id: int, q: str = None):  # Define una función que se ejecuta cuando se accede a la ruta /items/{item_id}
    return {"item_id": item_id, "q": q}  # Retorna un diccionario con el item_id y el parámetro opcional q