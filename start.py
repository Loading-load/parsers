# Imports
import telebot
import requests
import time
from telebot import types
import requests
from bs4 import BeautifulSoup as BS
# Config
bot = telebot.TeleBot("1016738432:AAFAqnEHkjCUtFQVyY29f7g4nCZfvxCmbX8") # Bot key
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Загружаю 📱")  #
    url = 'https://city.com.ua/catalog/smartphones/'  # Сылка
    r = requests.get(url)
    html = BS(r.content, 'html.parser')
    for el in html.select('.catalog_goods_cover'):  # блок
        title = el.select('.catalog_goods_title > a')  # Заголовок
        price = el.select('.catalog_goods_price > span')  # Цена
        buy = el.select('.catalog_goods_title > a')  # Сылка
        img_news = el.find('div', {'class': 'catalog_goods_photo'}).find('img').get('src') # фото
        info = el.select('.goods_descr')
        bot.send_photo(message.chat.id, 'https://city.com.ua' + img_news)
        markup = types.InlineKeyboardMarkup()  # Создаем кнопку
        step1 = types.InlineKeyboardButton("Купить за " + price[0].text + " грн.", url='https://city.com.ua' + buy[0].get('href'))
        markup.add(step1)
        bot.send_message(message.chat.id, title[0].text + '\n' + info[0].text.replace('.', '\n'), reply_markup=markup, parse_mode='html')
# To be continued
if __name__ == '__main__':
    bot.polling(none_stop=True) # цикл