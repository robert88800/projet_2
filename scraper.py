import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html'

response = requests.get(url)

def get_title(soup):
	title = soup.find('title')
	return title.text

def get_upc(soup):
	upc = soup.find('title')
	return title.text

if response.ok:
	soup = BeautifulSoup(response.text, 'html.parser')
	title = get_title(soup)
	print(title)