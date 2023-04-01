# from .start import dp#убрали импорт старого файла для старта, он без регистрации БД
from .bot_start import dp
from .help import dp
from .menu import dp
from .inline_menu import dp
# from .register import dp
from .add_food import dp

__all__ = ['dp']#это список параметров, которые можно импортировать из папки users
