import telebot
import datetime
from telebot import types
bot = telebot.TeleBot('5458982539:AAG8cbIih0MsrUAS-HYC1FOKK4ielhEu7bw')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Привет', 'Пока', 'Дата')
dt_now = datetime.datetime.now()
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)


@bot.message_handler(content_types='text')
def message_reply(message):
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


bot.infinity_polling()