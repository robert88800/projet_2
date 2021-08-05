import requests
from bs4 import BeautifulSoup
from scraper_product import get_product_informations, get_product_title, get_product_description, get_product_category, get_product_review_rating, get_product_image_url

# Ecriture de la fonction

def get_category_url_page(url):
	url_page = [url]
	response = requests.get(url)
	soup = BeautifulSoup(response.content, 'html.parser')
	next_presence = soup.find("li", {"class": "next"})
	while next_presence:
		link = next_presence.find('a')['href']
		url_page.append(url_page[0].replace('index.html','/' + link))
		url_search = url_page[0].replace('index.html','/' + link)
		response = requests.get(url_search)
		soup = BeautifulSoup(response.content, 'html.parser')
		next_presence = soup.find("li", {"class": "next"})
	return(url_page)

def get_category_product_url_page(soup):
	articles = soup.find_all('div', {'class': 'image_container'})
	links = []
	for article in articles:
		product_page_url = article.find('a')['href']
		links.append('http://books.toscrape.com/catalogue/' + product_page_url.replace('../',''))
	return links

def get_category_product_data(category_product_url_page):
	for url_page in category_product_url_page:
		response = requests.get(url_page)
		if response.ok:
			product_page_url = url_page
			soup = BeautifulSoup(response.content, 'html.parser')
			title = get_product_title(soup)
			upc, price_including_tax, price_excluding_tax, number_available = get_product_informations(soup)
			product_description = get_product_description(soup)
			category = get_product_category(soup)
			review_rating = get_product_review_rating(soup)
			image_url = get_product_image_url(soup)
			results = [product_page_url,upc,title,price_including_tax,price_excluding_tax,number_available,product_description,category,review_rating,image_url]
			data.append(results)
	

data = [['product_page_url,universal_product_code,title,price_including_tax,price_excluding_tax,number_available,product_description,category,review_rating,image_url']]

url = 'http://books.toscrape.com/catalogue/category/books/default_15/index.html'

list_url = get_category_url_page(url)	

for elt in list_url:
	response = requests.get(elt)
	if response.ok:
		soup = BeautifulSoup(response.content, 'html.parser')
		category_product_url_page = get_category_product_url_page(soup)
		get_category_product_data(category_product_url_page)
		
with open('check_category_price.csv', 'w', encoding="utf-8-sig") as outf:
	for i in range(len(data)):
	    for j in range(len(data[i])):
	        outf.write(data[i][j] + ',')
	    outf.write('\n')






			
