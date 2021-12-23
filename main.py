import telebot
from telebot import types
import urllib
import logging

url='https://mimigram.ru/wp-content/uploads/2020/07/%D0%A7%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%84%D0%BE%D1%82%D0%BE.jpeg'
f = open('out.jpg', 'wb')
f.write(urllib.request.urlopen(url).read())
f.close()


token = '5019806016:AAFod4Cy9FyFCxPlktH3IdgR0D1NYR2UdMY'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет ✌️ ")


@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Кнопка")
    markup.add(item1)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Кнопка":
        bot.send_chat_action(message.chat.id, 'upload_photo')
        img = open('out.jpg', 'rb')
        bot.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)
        img.close()


bot.infinity_polling()
