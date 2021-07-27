import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/category/books/history_32/index.html'

response = requests.get(url)

if response.ok:
	soup = BeautifulSoup(response.text, 'html.parser')
	title = soup.find('title')
	print(title.text)