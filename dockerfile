# Utiliza una imagen base de Python
FROM python:3.10.0

# Establece el directorio de trabajo
WORKDIR /app

# Copia todos los archivos del directorio actual al directorio de trabajo
COPY . .

# Instala las dependencias
RUN pip install -r requirements.txt

# Define las variables de entorno (asegúrate de que estas variables estén configuradas en tu entorno o utiliza un archivo .env)
ENV TOKEN='1984896147:AAHPlXoRiVSqN8oWkieMz4GeFYfZzFUVxOw'
ENV API_KEY='06c921750b9a82d8f5d1294e1586276f'


# Ejecuta el bot
CMD ["python", "bot.py"]
