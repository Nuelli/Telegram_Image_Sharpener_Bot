import os
import telebot
from PIL import Image, ImageFilter

# Replace with your Telegram bot token (get from BotFather)
BOT_TOKEN = "6962643767:AAGhDTqFYt2rI_9OVWtGxGOdSr4I0uKsof8"

# Create a Telegram bot instance
bot = telebot.TeleBot(BOT_TOKEN)

def enhance_image(image_path):
    """Applies artistic filters to an image."""
    try:
        img = Image.open(image_path)

        # Apply artistic filters (customize these or add more)
        img = img.filter(ImageFilter.SHARPEN)
        img = img.filter(ImageFilter.EDGE_ENHANCE)

        # Save the enhanced image
        enhanced_path = os.path.splitext(image_path)[0] + '_enhanced.jpg'
        img.save(enhanced_path, 'JPEG', quality=90)
        return enhanced_path
    except Exception as e:
        print(f"Error enhancing image: {e}")
        return None

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    """Receives photos, applies filters, and sends back the enhanced version."""
    try:
        # Download the photo
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        # Generate a unique filename
        filename = f'images/{message.chat.id}_{message.message_id}.jpg'
        with open(filename, 'wb') as f:
            f.write(downloaded_file)

        # Enhance the image
        enhanced_path = enhance_image(filename)
        if enhanced_path:
            with open(enhanced_path, 'rb') as f:
                bot.send_photo(message.chat.id, f)
            os.remove(enhanced_path)  # Clean up temporary file
        else:
            bot.send_message(message.chat.id, "An error occurred while enhancing your image.")

        os.remove(filename)  # Clean up downloaded file
    except Exception as e:
        print(f"Error handling photo: {e}")
        bot.send_message(message.chat.id, "An error occurred. Please try again.")

# Start the bot
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi! Send me a photo and I'll enhance it with some artistic flair.")

bot.polling()
