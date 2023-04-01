from aiogram.dispatcher.filters.state import StatesGroup, State
#далее в хендлерах мы создали файл register. В ините конечно имортировали класс

class registerT(StatesGroup):
    name = State()
    gender = State()
    date_of_birth = State()


