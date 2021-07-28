import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html'

response = requests.get(url)

def get_product_page_url():
	return response.url

def get_upc(soup):
	upc = soup.find('td')
	return upc.text

def get_title(soup):
	title = soup.find('h1')
	return title.text

def get_price_including_tax(soup):
	price_including_tax = soup.find('td')
	return price_including_tax.text



if response.ok:
	soup = BeautifulSoup(response.text, 'html.parser')
	product_page_url = get_product_page_url()
	upc = get_upc(soup)
	title = get_title(soup)
	price_including_tax = get_price_including_tax(soup)
	print(product_page_url)
	print(upc)
	print(title)
	print(price_including_tax)
	