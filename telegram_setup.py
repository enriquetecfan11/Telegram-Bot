import os
from datetime import datetime
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from dotenv import load_dotenv

load_dotenv()


from price_change import crypto_price
from timenews import noticias_economicas
from timenews import noticias
from timenews import mondejar_weather
from stonks_price import stonksPrice



# Init the bot and the updater


def init_bot():
    updater = Updater(os.getenv("TELEGRAM_TOKEN"), use_context=True)
    dispatcher = updater.dispatcher
    #print("Bot initialized!")

    # Define the commands

    def start(update: Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.message.chat_id, text="Hi! I'm a bot that will send you some things" +
                                 "\n" "I created by Enrique Rodriguez Vela." + "\n" + "If you want to see the comands type /help.")

    def help(update: Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.message.chat_id, text="/help: Show this message" + "\n" + "/crypto: Show the current price of crypto currencies" +
                                 "\n" + "/news: Show the latest news" + "\n" + "/weather: Show the current weather in Mondejar" + "\n" + "/stonks: Show the current price of Stonks")

    def stop(update: Update, context: CallbackContext):
        context.bot.send_message(
            chat_id=update.message.chat_id, text="Goodbye!")

    def crypto(update: Update, context: CallbackContext):
        context.bot.send_message(
            chat_id=update.message.chat_id, text=crypto_price())

    def weather(update: Update, context: CallbackContext):
        context.bot.send_message(
            chat_id=update.message.chat_id, text=mondejar_weather())

    def news(update: Update, context: CallbackContext):
        context.bot.send_message(
            chat_id=update.message.chat_id, text=noticias())

    def stonks(update: Update, context: CallbackContext):
        context.bot.send_message(
            chat_id=update.message.chat_id, text=stonksPrice())

    def economicas(update: Update, context: CallbackContext):
        context.bot.send_message(
            chat_id=update.message.chat_id, text=noticias_economicas())

    # Check what the user is typedn and save it in the variable command
    def typed(update: Update, context: CallbackContext):
        message = update.message.text
        #print("User said: " + message)

        if message == "hola" or message == "hello" or message == "hi" or message == "Hola":
            context.bot.send_message(
                chat_id=update.message.chat_id, text="Hola!")
        elif message == "adios" or message == "Adios" or message == "bye":
            context.bot.send_message(
                chat_id=update.message.chat_id, text="Adios!")
        elif message == "que hora es":
            context.bot.send_message(
                chat_id=update.message.chat_id, text="Son las " + datetime.now().strftime("%H:%M:%S"))
        elif message == "que dia es hoy":
            context.bot.send_message(
                chat_id=update.message.chat_id, text="Es " + datetime.now().strftime("%A"))
        elif message == "que dia es mañana":
            context.bot.send_message(chat_id=update.message.chat_id, text="Es " + (
                datetime.now() + timedelta(days=1)).strftime("%A"))
        elif message == "que puedes hacer":
            context.bot.send_message(
                chat_id=update.message.chat_id, text="Puedes hacer lo siguiente: /help")
        elif message == "que es esto":
            context.bot.send_message(
                chat_id=update.message.chat_id, text="Esto es un bot hecho por Enrique Rodriguez Vela")

        # If user post a message

    # Add the commands to the dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('stop', stop))
    dispatcher.add_handler(CommandHandler('crypto', crypto))
    dispatcher.add_handler(CommandHandler('weather', weather))
    dispatcher.add_handler(CommandHandler('news', news))
    dispatcher.add_handler(CommandHandler('stonks', stonks))
    dispatcher.add_handler(CommandHandler('economicas', economicas))
    dispatcher.add_handler(MessageHandler(Filters.text, typed))

    # Start the bot
    updater.start_polling()

    # Run the bot
    updater.idle()
