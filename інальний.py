import telebot
bot = telebot.TeleBot('5851283875:AAHYYrTfWW9duSPtVzg_uxcklkWvJPzospk')
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привет Пупсик')
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
bot.polling( none_stop=True, interval=0)
