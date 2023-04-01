#тут мы создаем бота
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

#импорт конфигурации
from data import config

#импорт ДБ
# from utils.db_api.db_users_config import db

#создаем переменную бота и диспетчера сообщений
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)

__all__ = ['bot', 'storage', 'dp']




