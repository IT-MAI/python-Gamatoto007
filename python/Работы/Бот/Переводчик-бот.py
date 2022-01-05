import telebot
from googletrans import Translator
translator = Translator()
bot = telebot.TeleBot("5095394120:AAFvLfwODN5YIAwRqX9z9ep3b4Tl8yVl-KQ")
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, "Отправьте мне что-либо на английском и я это переведу на русский")
def word2(word1):
    word1 = input()
    word2 = translator.translate(word1, src='en', dest='ru')
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, word2)
bot.polling(none_stop=True, interval=0)