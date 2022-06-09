from aiogram.utils import executor
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from client import *
import os

# Create a bot, get local variables
Bot_ = Bot(token=os.getenv("TOKEN")) # take telegram bot token from start.bat
ID_GROUP = os.getenv("ID_GROUP") # take telegram group id from start.bat
Dispatcher_ = Dispatcher(Bot_)

# function to be executed when the bot is successfully launched
async def on_startup(_):
    print("Бот вышел в онлан")

    pass


handlers_client(Dispatcher_)  # Registering commands for a bot

executor.start_polling(
    Dispatcher_, skip_updates=True, on_startup=on_startup
)  # Bot initialization
