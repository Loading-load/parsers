import telebot
import os

from telebot import types
token = os.getenv('1016738432:AAFAqnEHkjCUtFQVyY29f7g4nCZfvxCmbX8')
bot = telebot.TeleBot(token)

# start command handler
@bot.message_handler(commands=['start'])
def command_start_handler(message):
    cid = message.chat.id
    bot.send_chat_action(cid, 'typing')
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text='send location', request_location=True)
    markup.add(button_geo)
    bot.send_message(cid, 'Hello stranger, please choose commands from the menu', reply_markup=markup)


# application entry point
if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)