FROM python:3.8

# Actualiza pip
RUN pip install --upgrade pip

# Instala las dependencias necesarias
RUN pip install uvicorn fastapi mysql-connector-python sqlalchemy

# Copia el código de la aplicación al contenedor
COPY . /app

# Establece el directorio de trabajo
WORKDIR /app

# Expone el puerto 8000
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["sh", "-c", "python db.py && python add_items.py && uvicorn app:app --host 0.0.0.0 --port 8000"]