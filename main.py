import telebot
import webbrowser

from telebot import types

token = '6304461184:AAEzHvqspNqLD_7NeY883Q5Zs_z7BC31a_E'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Go to the site')
    btn2 = types.KeyboardButton('Delete photo')
    btn3 = types.KeyboardButton('Edit Text')

    markup.row(btn1)
    markup.row(btn2, btn3)

    file = open('default_profile_pic.png', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    # bot.send_message(message.chat.id, 'Hello!', reply_markup=markup)

    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'Go to the site':
        bot.send_message(message.chat.id, 'website open cap')
    elif message.text == 'Delete photo':
        bot.send_message(message.chat.id, 'Delete photo cap')
    elif message.text == 'Edit Text':
        bot.send_message(message.chat.id, 'Edit Text cap')


# @bot.message_handler(content_types=['photo'])
# def get_photo(message):
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton('Go to the site', url='google.com')
#     btn2 = types.InlineKeyboardButton('Delete photo', callback_data='delete')
#     btn3 = types.InlineKeyboardButton('Edit Text', callback_data='edit')
#
#     markup.row(btn1)
#     markup.row(btn2, btn3)
#
#     # markup.add(types.InlineKeyboardButton('Go to the site', url='google.com'))
#     bot.reply_to(message, 'Nice!', reply_markup=markup)
#
#
# @bot.callback_query_handler(func=lambda callback: True)
# def callback_message(callback):
#     if callback.data == 'delete':
#         bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
#     elif callback.data == 'edit':
#         bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)




@bot.message_handler(commands=['MyName'])
def myName(message):
    bot.send_message(message.chat.id, message.from_user.first_name)


@bot.message_handler(commands=['google', 'Google', 'Goog'])
def google(message):
    webbrowser.open('google.com')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '<b>Help!</b>', parse_mode='html')


# @bot.message_handler()
# def info(message):
#     if message.text.lower() == 'hello':
#         main(message)
#     elif message.text.lower() == 'id':
#         bot.reply_to(message, message.from_user.id)


bot.polling(none_stop=True)
# bot.infinity_polling()