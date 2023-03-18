#тут мы создаем бота
from aiogram import Bot, Dispatcher, types

from data import config

#создаем переменную бота и диспетчера сообщений
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)





