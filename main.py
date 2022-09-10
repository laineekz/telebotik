import telebot
import datetime
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from telebot import types
bot = telebot.TeleBot('5458982539:AAG8cbIih0MsrUAS-HYC1FOKK4ielhEu7bw')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Привет 👋', "Пока 💤")
keyboard1.row('Функции ⚙')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row("Пока 💤")
keyboard2.row('Функции ⚙')
classes_nums = telebot.types.ReplyKeyboardMarkup(True)



dt_now = datetime.datetime.now()



check = False
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Спасибо, что зашел ко мне)', reply_markup=keyboard1)
    pass

@bot.message_handler(content_types='text')
def send_text(message):
    if message.text == 'Привет 👋':
        bot.send_message(message.chat.id, 'Привет! Я бот-расписание для Гимназии №1 г.Бреста. Выбери "функции", чтобы посмотреть что я могу', reply_markup=keyboard2)
    if message.text == 'Пока 💤':
        bot.send_message(message.chat.id, 'Надеюсь, я смог тебе помочь. Возвращайся поскорее!', reply_markup=types.ReplyKeyboardRemove())
    if message.text == 'Функции ⚙':
        bot.send_message(message.chat.id, 'Как я заметил ты впервые зашел ко мне) Выбери свой класс', reply_markup=classes_nums)
bot.infinity_polling()


































