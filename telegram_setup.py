import os   
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from dotenv import load_dotenv
load_dotenv()

from price_change import crypto_price
from timenews import noticias
from timenews import mondejar_weather
from stonks_price import stonksPrice


# Init the bot and the updater

def init_bot():
    updater = Updater(os.getenv("TELEGRAM_TOKEN"), use_context=True)
    dispatcher = updater.dispatcher
    print("Bot initialized!")

    # Define the commands

    def start(update: Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.message.chat_id, text="Hi! I'm a bot that will send you some things" + "\n" "I created by Enrique Rodriguez Vela." + "\n" +"If you want to see the comands type /help.")

    def help(update: Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.message.chat_id, text="/help: Show this message" + "\n" + "/crypto: Show the current price of crypto currencies" + "\n" + "/news: Show the latest news" + "\n" + "/weather: Show the current weather in Mondejar" + "\n" + "/stonks: Show the current price of Stonks") 

    def stop(update: Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.message.chat_id, text="Goodbye!")

    def crypto(update: Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.message.chat_id, text=crypto_price())

    def weather(update: Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.message.chat_id, text=mondejar_weather())

    def news(update: Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.message.chat_id, text=noticias())

    def stonks(update: Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.message.chat_id, text=stonksPrice())

    # Add the commands to the dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('crypto', crypto))
    dispatcher.add_handler(CommandHandler('weather', weather))
    dispatcher.add_handler(CommandHandler('news', news))
    dispatcher.add_handler(CommandHandler('stonks', stonks))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

