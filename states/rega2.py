from aiogram.dispatcher.filters.state import StatesGroup, State
#далее в хендлерах мы создали файл register. В ините конечно имортировали класс

class reg(StatesGroup):
    food = State()
    sleep = State()
    toilet = State()


