import telebot
from translate import Translator

# Telegram Bot Token
TOKEN = '5756347206:AAE-8TD1qV8bDGM1w8djLG2woIHzqv6k_U0'

# Creating bot instance
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to Language Translator Bot!\n\n"
                          "Send me a message to translate it to another language.")

@bot.message_handler(func=lambda message: True)
def translate_message(message):
    try:
        translator = Translator(from_lang='auto', to_lang='en')  # Translate to English by default
        translated_text = translator.translate(message.text)
        bot.reply_to(message, f"Translated Text: {translated_text}")
    except Exception as e:
        bot.reply_to(message, f"Sorry, an error occurred: {str(e)}")

# Start the bot
bot.polling()
