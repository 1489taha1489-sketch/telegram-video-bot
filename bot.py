import telebot
import time

TOKEN = 8893578372:AAFBnne3EtFu8yf_cHX2eViKFIwKbbexlrs

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['video'])
def handle_video(message):
    sent = bot.copy_message(
        message.chat.id,
        message.chat.id,
        message.message_id
    )

    time.sleep(10)

    try:
        bot.delete_message(message.chat.id, sent.message_id)
    except:
        pass

bot.infinity_polling()
