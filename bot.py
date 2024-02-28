import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import os
from datetime import datetime, time
import base64
# import time
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import schedule
import pytz
from pytz import timezone


load_dotenv()

# Configura el token de tu bot proporcionado por BotFather
TOKEN = os.getenv("TOKEN")

api_key = os.getenv("API_KEY")

# Configura el nivel de registro (puedes ajustarlo según tus necesidades)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Crea un objeto logger
logger = logging.getLogger(__name__)

# Crea un objeto Updater para interactuar con el bot
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# ------------------------------
# Funciones Externas
# ------------------------------

# Importa funciones relacionadas con el clima desde el archivo weather_functions.py
from scripts.weather_functions import get_weather_data, create_weather_image

# Importa funciones relacionadas con criptomonedas desde el archivo crypto_functions.py
from scripts.crypto_functions import get_crypto_data, create_crypto_image, get_crypto

# Importa funciones relacionadas con el Metro desde el archivo metro_functions.py
from scripts.metro_functions import scrape_metro_status

# Importa funciones relacionadas con los precios de las acciones desde el archivo stonks.py
from scripts.stonks import allPrice


# Importa funciones relacionadas con las noticias desde el archivo news.py
from scripts.news import noticias_economicas_español


# ------------------------------
# Funciones de Comandos y Manejadores de Comandos
# ------------------------------

# Función para el comando /start
def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="¡Hola! Soy tu bot de Telegram. ¡Envíame un mensaje!")
    print(f"Chat ID: {chat_id}")  # Imprime el Chat ID
    logging.info(f"User {update.effective_user['username']} started the conversation")

# Función para el comando /crypto
def crypto(update, context):
    # Obtener el nombre o nombres de las criptomonedas
    crypto = context.args[0]
    # Obtener los datos de las criptomonedas
    crypto_data = get_crypto(crypto)
    # Enviar los datos de las criptomonedas al usuario
    context.bot.send_message(chat_id=update.effective_chat.id, text=crypto_data)
    # Log the message
    logger.info(f"User {update.effective_user['username']} asked for crypto data")

# Función para el comando /weather
def weather(update, context):
    # Obtener el nombre de la ciudad
    city = context.args[0]
    # Obtener los datos del tiempo
    weather_data = get_weather_data(city)
    # Crear una imagen con los datos del tiempo
    image = create_weather_image(city)
    # Enviar la imagen al usuario
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(image, 'rb'))
    # Eliminar la imagen creada
    os.remove(image)
    # Log the message
    logger.info(f"User {update.effective_user['username']} asked for weather data")

# Función para el comando /metro
def metro(update, context):
    line_statuses = scrape_metro_status()
    
    # Create a string with the status of each line
    message = ''
    for line, status in line_statuses.items():
        message += f'{line}: {status}\n'
    
    # Send the message to the user
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    
    # Log the message
    logger.info(f"User {update.effective_user['username']} asked for Metro status")

# Función para el comando /hora
def hora(update, context):
    # Obtener la hora actual
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    # Enviar la hora actual al usuario
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Son las {current_time}")

    # Log the message
    logger.info(f"User {update.effective_user['username']} asked for the time")

# Función para el comando /stonks
def stonksPrice(update, context):
    # Enviar mensaje de espera al usuario
    context.bot.send_message(chat_id=update.effective_chat.id, text="Enviando precios de las acciones... (esto puede tardar unos segundos)")
    
    logger.info("Stonks Prices Sent!!")
    logger.info(allPrice())

    # Obtener los precios de las acciones
    output = allPrice()

    # Enviar los precios de las acciones al usuario
    context.bot.send_message(chat_id=update.effective_chat.id, text=output)
    
    # Log the message
    logger.info(f"User {update.effective_user['username']} asked for stonks prices")

# Función para el comando /noticias
def noticias(update, context):
    print("Noticias enviadas!!")
    print(noticias_economicas_español())
    # Obtener las noticias
    output = noticias_economicas_español()

    # Enviar las noticias al usuario
    context.bot.send_message(chat_id=update.effective_chat.id, text=output)
    # Log the message
    logger.info(f"User {update.effective_user['username']} asked for news")

def bolsaOpen(update, context):
    # Mensajes
    output = """ 
    La bolsa de Madrid abre a las 9:00 y cierra a las 17:30 (hora de Madrid)
    La bolsa de Nueva York abre a las 15:30 y cierra a las 22:00 (hora de Madrid)
    La bolsa de Tokio abre a las 23:00 y cierra a las 7:00 (hora de Madrid)
    """
    # Enviar los horarios de apertura de las bolsas al usuario
    context.bot.send_message(chat_id=update.effective_chat.id, text=output)

def miestacion(update, context):
  weather_status = miestacion()
  
  context.bot.send_message(chat_id=update.effective_chat.id, text=weather_status)
  
  logger.info(f"User {update.effective_user['username']} asked for mi estacion data")


# Hacer una peticion a la API que genera una imagen http://localhost:8000/generate?prompt= || prompt es texto que escribe el usuario
def generate_image(update, context):
    logger.info(f"User {update.effective_user['username']} asked for image generation")
    # Send the message to the user
    context.bot.send_message(chat_id=update.effective_chat.id, text="Generando imagen...")
    # Obtenemos el texto completo después del comando
    prompt = ' '.join(context.args)
    print("User prompt: ", prompt)
    response = requests.get(f"http://localhost:8000/generate?prompt={prompt}")
    # Si la respuesta es correcta y el codigo de estado es 200
    if response.status_code == 200:

    # hacemos una peticion a la API para obtener la imagen
      response = requests.get("http://localhost:8000/image")
      response_data = response.json()

      if response_data['image']:
        # Decodificamos la imagen
        image = base64.b64decode(response_data['image'])
        # Creamos una imagen
        image = Image.open(BytesIO(image))
        # Guardamos la imagen
        image.save("image.png")
        # Enviamos la imagen al usuario
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open("image.png", 'rb'))
        # Eliminamos la imagen
        os.remove("image.png")
      else:
        # Si no hay imagen
        context.bot.send_message(chat_id=update.effective_chat.id, text="No se ha podido enviar la imagen")
    else:
      # Si no hay respuesta
      context.bot.send_message(chat_id=update.effective_chat.id, text="No se ha podido generar la imagen")


# Función para el comando /help
def help(update, context):
    #Comandos disponibles
    output = """
    Comandos disponibles:
    - /start: Inicia el bot
    - /price <nombre crypto>: Muestra el precio de una criptomoneda
    - /weather <nombre ciudad> : Muestra el tiempo de una ciudad
    - /metro: Muestra el estado de las líneas de Metro de Madrid
    - /hora: Muestra la hora actual
    - /stonks: Muestra los precios de las acciones
    - /noticias: Muestra las noticias económicas
    - /bolsa: Muestra los horarios de apertura de las bolsas
    - /miestacion: Muestra los datos de mi estación de temperatura
    - /auto: Inicia el envio de mensajes automaticos
    - /stop: Para el envio de mensajes automaticos
    - /generate <texto>: Genera una imagen con el texto que le pasemos
    """
    # Enviar los comandos disponibles al usuario
    context.bot.send_message(chat_id=update.effective_chat.id, text=output)
    # Log the message
    logger.info(f"User {update.effective_user['username']} asked for help")



# ------------------------------
# Manejadores de Comandos
# ------------------------------

# Agregar un manejador para el comando /start
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
logger.info("Bot started")

# Agregar un manejador para el comando /crypto
crypto_handler = CommandHandler('price', crypto)
dispatcher.add_handler(crypto_handler)
logger.info("Crypto handler added")

# Agregar un manejador para el comando /weather
weather_handler = CommandHandler('weather', weather)
dispatcher.add_handler(weather_handler)
logger.info("Weather handler added")

# Agregar un manejador para el comando /help
help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)
logger.info("Help handler added")

# Agregar un manejador para el comando /metro
metro_handler = CommandHandler('metro', metro)
dispatcher.add_handler(metro_handler)
logger.info("Metro handler added")

# Agregar un manejador para el comando /hora
hora_handler = CommandHandler('hora', hora)
dispatcher.add_handler(hora_handler)
logger.info("Hora handler added")

# Agregar un manejador para el comando /stonks
stonks_handler = CommandHandler('stonks', stonksPrice)
dispatcher.add_handler(stonks_handler)
logger.info("Stonks handler added")

# Agregar un manejador para el comando /noticias
noticias_handler = CommandHandler('noticias', noticias)
dispatcher.add_handler(noticias_handler)
logger.info("Noticias handler added")

# Agregar un manejador para el comando /bolsa
bolsa_handler = CommandHandler('bolsa', bolsaOpen)
dispatcher.add_handler(bolsa_handler)
logger.info("Bolsa handler added")

# Agregar un manejador para el comando /miestacion
miestacion_handler = CommandHandler('miestacion', miestacion)
dispatcher.add_handler(miestacion_handler)
logger.info("Miestacion handler added")

# Agregar un manejador para el comando /generate
generate_handler = CommandHandler('generate', generate_image)
dispatcher.add_handler(generate_handler)
logger.info("Image Generate handler added")

# ------------------------------
# Iniciar el bot
# ------------------------------

while True:
    try:
        # Comprueba si hay tareas programadas y ejecútalas
        schedule.run_pending()

        # Mantener el bot en ejecución
        updater.start_polling()
        logger.info("Bot Started")

        # Print schedule status
        print(schedule.get_jobs())
        
        # Mantener el bot en ejecución
        updater.idle()
        logger.info("Bot stopped")

    
    except Exception as e:
        # Maneja cualquier excepción que pueda ocurrir durante la ejecución
        print(f"Error: {e}")
        logger.error(f"Error: {e}")
