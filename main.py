import telebot
import webbrowser

token = '6304461184:AAEzHvqspNqLD_7NeY883Q5Zs_z7BC31a_E'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Hello!')


@bot.message_handler(commands=['MyName'])
def myName(message):
    bot.send_message(message.chat.id, message.from_user.first_name)


@bot.message_handler(commands=['google', 'Google', 'Goog'])
def google(message):
    webbrowser.open('google.com')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '<b>Help!</b>', parse_mode='html')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'hello':
        main(message)
    elif message.text.lower() == 'id':
        bot.reply_to(message, message.from_user.id)


bot.polling(none_stop=True)
# bot.infinity_polling()