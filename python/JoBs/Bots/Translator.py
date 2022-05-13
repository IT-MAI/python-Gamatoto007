from googletrans import Translator
import telebot
from telebot import types
translator = Translator()
bot = telebot.TeleBot("5095394120:AAFvLfwODN5YIAwRqX9z9ep3b4Tl8yVl-KQ")
@bot.message_handler(commands=["start"])
def start(m, res=False):
    f = open("D:/T4EooJBpawI.jpg", 'rb')
    bot.send_photo(m.chat.id, f)
    bot.send_message(m.chat.id, "Отправьте мне любое сообщение, и я его переведу на английский",)
@bot.message_handler(content_types=["text"])
def handle_text(m):
    result = translator.translate(m.text)
    bot.send_message(m.chat.id, result)
bot.polling(none_stop=True, interval=0)