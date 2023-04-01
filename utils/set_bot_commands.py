from aiogram import types
#тут кнопки для основных команд меню, которое внизу слева
async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запустить бота'),
        types.BotCommand('help', 'Помощь'),
        types.BotCommand('register', 'Регистрация'),
        types.BotCommand('profile', 'Получить данные из БД')
    ])
