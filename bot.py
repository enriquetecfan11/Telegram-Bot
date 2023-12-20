import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import os
from datetime import datetime, time

# import time
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import schedule
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

# Función para el comando /stonks
def stonksPrice(update, context):
    # Enviar mensaje de espera al usuario
    context.bot.send_message(chat_id=update.effective_chat.id, text="Enviando precios de las acciones...")
    
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
    
# Función para el comando /help
def help(update, context):
    # Scrape the Metro Madrid "La red en tiempo real" status
    context.bot.send_message(chat_id=update.effective_chat.id, text="Estos son los comandos que puedes utilizar:")
    context.bot.send_message(chat_id=update.effective_chat.id, text="/start - Inicia el bot")
    context.bot.send_message(chat_id=update.effective_chat.id, text="/price <nombre crypto> - Muestra los precios de las criptomonedas")
    context.bot.send_message(chat_id=update.effective_chat.id, text="/weather <nombre ciudad> - Muestra el tiempo en una ciudad")
    context.bot.send_message(chat_id=update.effective_chat.id, text="/metro - Muestra el estado del Metro de Madrid")
    context.bot.send_message(chat_id=update.effective_chat.id, text="/hora - Muestra la hora actual")
    context.bot.send_message(chat_id=update.effective_chat.id, text="/stonks - Muestra los precios de las acciones")
    context.bot.send_message(chat_id=update.effective_chat.id, text="/noticias - Muestra las noticias")
    context.bot.send_message(chat_id=update.effective_chat.id, text="/noticias_economicas - Muestra las noticias economicas")
    context.bot.send_message(chat_id=update.effective_chat.id, text="/auto - Inicia el envio de mensajes automaticos")
    context.bot.send_message(chat_id=update.effective_chat.id, text="/stop - Para el envio de mensajes automaticos")
    context.bot.send_message(chat_id=update.effective_chat.id, text="/help - Muestra esta ayuda")
    context.bot.send_message(chat_id=update.effective_chat.id, text="/bolsa - Muestra los horarios de apertura de las bolsas")
    # Log the message
    logger.info(f"User {update.effective_user['username']} asked for help")

# ------------------------------
# Comandos programados
# ------------------------------
    
def callback_auto_message(update, context):
  now = datetime.now(timezone('Europe/Madrid'))
  current_time = now.strftime("%H:%M:%S")

  if current_time == "09:00:00":
    # Enviar mensaje de espera al usuario
    context.bot.send_message(chat_id='207196532', text="Buenos Dias! Son las 9:00")
    context.bot.send_message(chat_id='207196532', text="Buenos Dias! Bolsa de Madrid abierta.")
  elif current_time == "15:30:00":
    # Enviar mensaje de espera al usuario
    context.bot.send_message(chat_id='207196532', text="Buenas Tardes! Son las 15:30")
    context.bot.send_message(chat_id='207196532', text="Buenas Tardes! Bolsa de Nueva York abierta.")
  elif current_time == "17:30:00":
    # Enviar mensaje de espera al usuario
    context.bot.send_message(chat_id='207196532', text="Buenas Tardes! Son las 17:30")
    context.bot.send_message(chat_id='207196532', text="Buenas Tardes! Bolsa de Madrid cerrada.")
  elif current_time == "22:00:00":
    # Enviar mensaje de espera al usuario
    context.bot.send_message(chat_id='207196532', text="Buenas Noches! Son las 22:00")
    context.bot.send_message(chat_id='207196532', text="Buenas Noches! Bolsa de Nueva York cerrada.")
  else:
    context.bot.send_message(chat_id='207196532', text="No hay mensajes programados para esta hora")

# Funcion para iniciar el envio de mensajes automaticos
def start_auto_messaging(update, context):
    chat_id = update.message.chat_id

    context.bot.send_message(chat_id=chat_id, text='Mensajes automaticos iniciados!')

    # Send data every 5 minutes
    # context.job_queue.run_repeating(callback_auto_message, 300, context=chat_id, name=str(chat_id))

    # Sen data all days at 9:00 madrid timezone
    context.job_queue.run_daily(callback_auto_message, time(hour=9, minute=0, tzinfo=pytz.timezone('Europe/Madrid')), context=chat_id, name=str(chat_id))

    # Send data all days at 15:30 madrid timezone
    context.job_queue.run_daily(callback_auto_message, time(hour=15, minute=30, tzinfo=pytz.timezone('Europe/Madrid')), context=chat_id, name=str(chat_id))

    # Send data all days at 17:30 madrid timezone
    context.job_queue.run_daily(callback_auto_message, time(hour=17, minute=30, tzinfo=pytz.timezone('Europe/Madrid')), context=chat_id, name=str(chat_id))

    # Send data all days at 22:00 madrid timezone
    context.job_queue.run_daily(callback_auto_message, time(hour=22, minute=0, tzinfo=pytz.timezone('Europe/Madrid')), context=chat_id, name=str(chat_id))


# Funcion para parar el envio de mensajes automaticos
def stop_notify(update, context):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text='Mensajes automaticos parados!')
    job = context.job_queue.get_jobs_by_name(str(chat_id))
    job[0].schedule_removal()


dispatcher.add_handler(CommandHandler("auto", start_auto_messaging))
logger.info("Auto handler added")

dispatcher.add_handler(CommandHandler("stop", stop_notify))
logger.info("Stop handler added")


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
