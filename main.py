import telebot
from telebot import types
import logging
import datetime
from camera_manipulations import  make_photo

logging.basicConfig(format="%(asctime)s %(filename)s:%(lineno)s %(name)s::%(funcName)s: %(message)s",
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)
LOGGER = logging.getLogger("main")

token = '5019806016:AAFod4Cy9FyFCxPlktH3IdgR0D1NYR2UdMY'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def photo_button_message_handler(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    photo_button = types.KeyboardButton("Фото")
    markup.add(photo_button)
    LOGGER.debug("User being offered with an action.")
    bot.send_message(message.chat.id, 'Выберите необходимое', reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Фото":
        LOGGER.debug("Executing photo making query.")
        make_photo()
        bot.send_chat_action(message.chat.id, 'upload_photo')
        img = open('out.png', 'rb')
        bot.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)
        img.close()


bot.infinity_polling()
