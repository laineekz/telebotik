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























#
#
#
#
#
# import telebot
# bot = telebot.TeleBot('5682784377:AAHYsq_ZPICwsSXFnt1YjqX46iSW2xDg3yg')
#
# keybord1 = telebot.types.InlineKeyboardMarkup()
# keybord1.add(
#     telebot.types.InlineKeyboardButton(text='привет 👋', callback_data='hello'),
#     telebot.types.InlineKeyboardButton(text='пока 💤', callback_data='bye'))
# keybord1.add(telebot.types.InlineKeyboardButton(text='поиск транспорта 🔍', callback_data='search'))
# #
#
# keybord2 = telebot.types.InlineKeyboardMarkup()
# keybord2.add(
#     telebot.types.InlineKeyboardButton(text='такси 🚕', callback_data='taxi'),
#     telebot.types.InlineKeyboardButton(text='общественный\nтранспорт 🚌', callback_data='all'),
#     telebot.types.InlineKeyboardButton(text='вернуться назад 🔙', callback_data='back'))
#
# #
# # keybord3 = telebot.types.ReplyKeyboardMarkup(True)
# # keybord3.row('автобус 🚌', 'метро 🚈')
# # keybord3.row('трамвай 🚋', 'троллейбус 🚎')
# # keybord3.row('вернуться назад 🔙')
# #
# # key = 0
# # weat = 0
#
# @bot.message_handler(commands=['start'])
# def send_start(message):
#     bot.send_message(message.chat.id, 'привет, ты запустил меня', reply_markup = keybord1)
#
# @bot.callback_query_handler(func=lambda call: True)
# def answer(start):
#     global weat
#     global key
#     if start.data == 'hello':
#         keybord_h = telebot.types.InlineKeyboardMarkup()
#         keybord_h.add(
#             telebot.types.InlineKeyboardButton(text='да ✅', callback_data='yes'),
#             telebot.types.InlineKeyboardButton(text='нет ❌', callback_data='no'))
#         bot.send_message(start.message.chat.id, 'привет, ты запустил меня', reply_markup=keybord_h)
#         bot.delete_message(start.message.chat.id, start.message_id)
#     elif start.data == 'bye':
#         pass
#
#
#     elif start.data == 'search':
#         weat = 1
#         bot.delete_message(start.message.chat.id, start.message_id)
#     if start.data == 'yes':
#         weat = 1
#         bot.delete_message(start.message.chat.id, start.message_id)
# #     if message.text.lower() == 'привет 👋':
# #         keybordy = telebot.types.InlineKeyboardMarkup()
# #         keybordy.row('да ✅', 'нет ❌')
# #         bot.send_message(message.chat.id, 'и тебе привет! начнём?', reply_markup=keybordy)
# #     if message.text.lower() == 'да ✅':
# #         weat = 1
# # #
# #
# #
#     if weat == 1:
#         bot.send_message(start.message.chat.id, 'выберите тип транспорта', reply_markup=keybord2)
#         key = 1
#         weat = 0
#         bot.delete_message(start.message.chat.id, start.message_id)
# #
# #
# #     if message.text.lower() == 'общественный транспорт 🚌':
# #         bot.send_message(message.chat.id, 'выберите подходящий транспорт', reply_markup=keybord3)
# #         key = 2
# #         weat = 0
# #
# #     elif message.text.lower() == 'вернуться назад 🔙' and key == 2:
# #         bot.send_message(message.chat.id, 'выберите тип транспорта', reply_markup=keybord2)
# #         key = 0
# #         weat = 1
# #
#     elif start.data == 'back' and key == 1:
#         bot.send_message(start.message.chat.id, 'привет, ты запустил меня', reply_markup=keybord1)
#         key = 0
#         bot.delete_message(start.message.chat.id, start.message_id)
#
# bot.polling()
#




