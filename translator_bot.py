import telegram

# Replace with your Telegram bot token
BOT_TOKEN = "5756347206:AAE-8TD1qV8bDGM1w8djLG2woIHzqv6k_U0"

# Basic translation rules (modify for your desired languages and rules)
translations = {
    "hello": {"es": "hola", "fr": "bonjour"},
    "goodbye": {"es": "adiós", "fr": "au revoir"},
    "thank you": {"es": "gracias", "fr": "merci"},
}

def translate(text, source_lang="en", target_lang="es"):
    """
    Attempts to translate text using basic rules (limited functionality).
    """
    translation = translations.get(text.lower())
    if translation and target_lang in translation:
        return translation[target_lang]
    else:
        return "Sorry, I cannot translate that yet."

def handle_message(update, context):
    """
    Handles incoming messages, attempting translation based on limited rules.
    """
    chat_id = update.effective_chat.id
    text = update.message.text
    translated_text = translate(text)
    context.bot.send_message(chat_id=chat_id, text=translated_text)

def main():
    """
    Initializes and starts the bot.
    """
    updater = telegram.Updater(token=BOT_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
