import requests
from bs4 import BeautifulSoup as BS
url = 'https://city.com.ua/catalog/smartphones/' # Сылка

r = requests.get(url)

html = BS(r.content, 'html.parser')

for el in html.select('.catalog_goods_cover'):  # блок
	# title = el.select('.catalog_goods_photo > img')  # Заголовок
	img_news = html.find('div', {'class': 'catalog_goods_photo'}).find('img').get('src')
	print(img_news)