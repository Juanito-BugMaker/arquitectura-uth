# 1. Una versión oficial y ligera de Python
FROM python:3.12-slim

# 2. Le decimos a Docker en qué carpeta interna trabajará
WORKDIR /app

# 3. Copiamos el requirements y lo instalamos
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiamos el resto del código del proyecto
COPY . /app/

# 5. Comando para encender el servidor de Django en el puerto 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]