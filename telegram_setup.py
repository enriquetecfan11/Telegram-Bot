import logging
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Application, ContextTypes, MessageHandler
import os

from dotenv import load_dotenv
load_dotenv()

import tracemalloc
tracemalloc.start()

from price_change import crypto_price
from timenews import noticias_economicas
from timenews import noticias
from timenews import mondejar_weather
from stonks_price import stonksPrice
from amazonprice import cetus_price

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# ---------------------------------------------
# Start commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """Send a message when the command /start is issued."""
  await update.message.reply_text(f"Hi I`m TecfanBot! Welcome {update.effective_user.first_name}")

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """Send a message when the command /price is issued."""
  await update.message.reply_text(cetus_price())

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """Echo the user message."""
  await update.message.reply_text(update.message.text)

async def crypto(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """Send a message when the command /crypto is issued."""
  await update.message.reply_text(crypto_price())

async def stonks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """Send a message when the command /stonks is issued."""
  await update.message.reply_text(stonksPrice())

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """Send a message when the command /news is issued."""
  await update.message.reply_text(noticias())

async def news_economicas(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """Send a message when the command /news is issued."""
  await update.message.reply_text(noticias_economicas())

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """Send a message when the command /weather is issued."""
  await update.message.reply_text(mondejar_weather())

# Now make a help show all the commands available
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """Send a message when the command /help is issued."""
  await update.message.reply_text("Los comandos de este bot son: \n /start \n /price \n /crypto \n /stonks \n /noticias \n /economicas \n /weather")

# ---------------------------------------------
def init_bot():
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    app = Application.builder().token(os.getenv('TELEGRAM_TOKEN')).build()


    # ---------------------------------------------
    # All commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("price", price))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("echo", echo))
    app.add_handler(CommandHandler("crypto", crypto))
    app.add_handler(CommandHandler("stonks", stonks))
    app.add_handler(CommandHandler("news", news))
    app.add_handler(CommandHandler("news_economicas", news_economicas))
    app.add_handler(CommandHandler("weather", weather))

    # ---------------------------------------------


    # ---------------------------------------------
    # Start the Bot
    app.run_polling()

