import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/category/books/history_32/index.html'

response = requests.get(url)

# Ecriture de la fonction

def get_all_product_page_url(soup):
	articles = soup.find_all('div', {'class': 'image_container'})
	links = []
	for article in articles:
		product_page_url = article.find('a')['href']
		links.append('http://books.toscrape.com/catalogue/' + product_page_url.replace('../',''))
	return links

def extract_data_category(all_product_page_url):
	with open('check_prices.csv', 'w', encoding = 'utf-8-sig') as outf:
		outf.write('product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url\n\n')

	for link in all_product_page_url:
		data = []
		response = requests.get(link)
		if response.ok:
			soup = BeautifulSoup(response.content, 'html.parser')

			product_page_url = links
			data.append(product_page_url)

			upc = soup.find("table", {"class": "table table-striped"}).find_all("td")
			universal_product_code = upc[0].text
			data.append(universal_product_code)

			title = soup.find('li', {'class': 'active'})
			title = title.text
			data.append(title)

			pit = soup.find("table", {"class": "table table-striped"}).find_all("td")
			price_including_tax = pit[3].text
			data.append(price_including_tax)

			pet = soup.find("table", {"class": "table table-striped"}).find_all("td")
			price_excluding_tax = pit[2].text
			data.append(price_excluding_tax)

			na = soup.find("table", {"class": "table table-striped"}).find_all("td")
			number_available = na[5].text
			data.append(number_available)

			





if response.ok:
	soup = BeautifulSoup(response.content, 'html.parser')
	all_product_page_url = get_all_product_page_url(soup)
	print(all_product_page_url)
