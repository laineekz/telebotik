import telebot
import datetime
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from telebot import types
bot = telebot.TeleBot('5458982539:AAG8cbIih0MsrUAS-HYC1FOKK4ielhEu7bw')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Привет', 'Пока')
keyboard1.row('Дата', 'Погода')
dt_now = datetime.datetime.now()

language = get_default_config()
language['language'] = 'ru'
owm = OWM('23232775d430e5fe2ac9a9c2cbdb8410', language)
mgr = owm.weather_manager()


check = False
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)
# @bot.message_handler(content_types='text')
# def check_message(message):
#     if message.text == 'погода':
#         global check
#         check = True
@bot.message_handler(content_types='text')
def send_text(message):
    global check
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'И тебе привет!)')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'И тебе пока!(')
    elif message.text.lower() == 'дата':
        bot.send_message(message.chat.id, dt_now.date())
        wd = dt_now.isoweekday()
        if wd == 1:
            bot.send_message(message.chat.id, 'Понедельник')
        elif wd == 2:
            bot.send_message(message.chat.id, 'Вторник')
        elif wd == 3:
            bot.send_message(message.chat.id, 'Среда')
        elif wd == 4:
            bot.send_message(message.chat.id, 'Четверг')
        elif wd == 5:
            bot.send_message(message.chat.id, 'Пятница')
        elif wd == 6:
            bot.send_message(message.chat.id, 'Суббота')
        else:
            bot.send_message(message.chat.id, 'Воскресенье')
    elif message.text.lower() == 'погода':
        check = True
        bot.send_message(message.chat.id, 'введи пж город')
    elif check == True:

        city = message

        observation = mgr.weather_at_place(city.text)
   ######################

        weather = observation.weather
        bot.send_message(message.chat.id, f"Погода в городе: {city.text}")
        bot.send_message(message.chat.id, f"Сейчас на улице: {weather.detailed_status}")
        bot.send_message(message.chat.id, f"Облачность: {weather.clouds}%")
        bot.send_message(message.chat.id, f"Текущая температура: {weather.temperature('celsius').get('temp')} градусов")
        bot.send_message(message.chat.id,
                         f"Максимальная температура: {weather.temperature('celsius').get('temp_max')} градусов")
        bot.send_message(message.chat.id,
                         f"Минимальная температура: {weather.temperature('celsius').get('temp_min')} градусов")
        bot.send_message(message.chat.id,
                         f"Сейчас ощущается: {weather.temperature('celsius').get('feels_like')} градусов")
        if weather.rain.get('1h'):
            rain = weather.rain.get('1h')
        else:
            rain = 0
        bot.send_message(message.chat.id, f"За последний час выпало осадков: {rain} мм")
        bot.send_message(message.chat.id, f"Текущая влажность: {weather.humidity}%")
        if weather.heat_index:
            index = weather.heat_index
        else:
            index = 0
        bot.send_message(message.chat.id, f"Тепловой индекс: {index}")
        bot.send_message(message.chat.id, f"Скорость ветра: {weather.wind().get('speed')} м/с")
        check = False


bot.infinity_polling()


































