import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html'

response = requests.get(url)

# Ecriture des fonctions

def get_product_page_url():
	return response.url

def get_tds(soup):
	tds = soup.findAll('td')
	list_tds = list()
	for td in tds:
		list_tds.append(str(td.text))
	return list_tds

def get_upc(tds):
	return tds[0]

def get_title(soup):
	title = soup.find('div', {'class': 'col-sm-6 product_main'}).find('h1')
	return title.text

def get_price_including_tax(tds):
	return tds[3]

def get_price_excluding_tax(tds):
	return tds[2]

def get_number_available(tds):
	return tds[5]

def get_product_description(soup):
	product_description = soup.find('article', {'class': 'product_page'}).find('p')	
	return product_description.text


'''
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
	

if response.ok:
	soup = BeautifulSoup(response.text, 'html.parser')
	tds = soup.findAll('td')
	[print(str(td.text)) for td in tds]


if response.ok:
	soup = BeautifulSoup(response.text, 'html.parser')
	product_page_url = get_product_page_url()
	upc = get_upc(soup)
	print(product_page_url)
'''

if response.ok:
	product_page_url = get_product_page_url()
	soup = BeautifulSoup(response.text, 'html.parser')
	tds = get_tds(soup)
	upc = get_upc(tds)
	title = get_title(soup)
	price_including_tax = get_price_including_tax(tds)
	price_excluding_tax = get_price_excluding_tax(tds)
	number_available = get_number_available(tds)
	product_description = get_product_description(soup)
	print(product_page_url)
	print(upc)
	print(title)
	print(price_including_tax)
	print(price_excluding_tax)
	print(number_available)
	print(product_description)
	print(tds)