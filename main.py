import telebot


bot = telebot.TeleBot('6361885667:AAGtY5WW64n7Qm-r5PX2TH-pCGZ0qeAZohE')


@bot.message_handler(commands=['/start'])
def main(message):
    bot.send_message(message.chat.id,'Приветствую тебя, друг!',parse_mode='Markdown')


bot.infinity_polling()