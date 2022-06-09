from aiogram import types, Dispatcher
from bot_telegram import Bot_, ID_GROUP
from manager import *

# if you need to send message on private messages 
# need change 'ID_GROUP' to 'message.from_user.id'


# start\help commands for bot
async def command_start(message: types.Message):
    await Bot_.send_message(ID_GROUP, "For information type /info")
    pass


# info command for bot
async def info_command(message: types.Message):
    await Bot_.send_message(ID_GROUP, "Wait, collecting data")
    for item in convertor_list_str(take_reviews()):
        await Bot_.send_message(ID_GROUP, item)
    await Bot_.send_message(ID_GROUP, "Here's everything we found")
    pass


# Registering commands for a bot
def handlers_client(Dispatcher_: Dispatcher):
    Dispatcher_.register_message_handler(command_start, commands=["start", "help"])
    Dispatcher_.register_message_handler(info_command, commands=["info"])
    pass
