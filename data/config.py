import os#библиотека функций для работы с операционной системой
from dotenv import load_dotenv#нужно также в окружение поставить библиотеку pip install python-dotenv. Скорее всего для работы с файлами

load_dotenv()#функцию load_dotenv нужно вызвать пустой


BOT_TOKEN = str(os.getenv("BOT_TOKEN"))#это скорее всего считывание файла .env , файл этот нужно сохранить в корне проекта и там прописать токен бота без кавычек в переменную BOT_TOKEN

admins_id = {str(os.getenv('admins'))}#тут прописаны айди всех администраторов бота.

#подключение базы данных postgresql
ip = os.getenv('ip')
PGUSER = str(os.getenv('PGUSER'))#его смотреть в pgadimn в разделе Login/Group Roles, самая последняя строка
PGPASSWORD = str(os.getenv('PGPASSWORD'))#это пароль к юзеру, не к самой ДБ
DATABASE = str(os.getenv('DATABASE'))#название ДБ
#все эти данные берутся из файла .env . Там нужно все прописать
#PGUSER - это юзер posgre обычно он называется postgres. PGPASSWORD - это пароль который создавали при установке пгадмина. DATABASE это имя базы данных, которую мы создадим в пгадмин. ip это ip устройства где лежит дб. Если лежит на нашем пк, то локалхост

POSTGRES_URI = f'postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}'#это ссылка на базу




