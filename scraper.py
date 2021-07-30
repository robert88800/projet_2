import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html'

response = requests.get(url)

# Ecriture des fonctions

def get_product_page_url():
	return response.url

def get_upc(soup):
	upc = soup.find("table", {"class": "table table-striped"}).find_all("td")
	return upc[0].text

def get_title(soup):
	title = soup.find('li', {'class': 'active'})
	return title.text

def get_price_including_tax(soup):
	pit = soup.find("table", {"class": "table table-striped"}).find_all("td")
	return pit[3].text

def get_price_excluding_tax(soup):
	pet = soup.find("table", {"class": "table table-striped"}).find_all("td")
	return pet[2].text

def get_number_available(soup):
	na = soup.find("table", {"class": "table table-striped"}).find_all("td")
	return na[5].text

def get_product_description(soup):
	if soup.find("div", {"id": "product_description"}):
		pd = soup.find("div", {"id": "product_description"}).find_next("p")
		return pd.text
	else:
		return "No description available"

def get_category(soup):
	cat = soup.find("li", {"class": "active"}).find_previous("a")
	return cat.text

def get_review_rating(soup):
	if soup.find("div", {"class": "col-sm-6 product_main"}).find("p", {"class": "star-rating One"}):
		review_rating = "1 Etoile"
	elif soup.find("div", {"class": "col-sm-6 product_main"}).find("p", {"class": "star-rating Two"}):
		review_rating = "2 Etoiles"
	elif soup.find("div", {"class": "col-sm-6 product_main"}).find("p", {"class": "star-rating Three"}):
		review_rating = "3 Etoiles"
	elif soup.find("div", {"class": "col-sm-6 product_main"}).find("p", {"class": "star-rating Four"}):
		review_rating = "4 Etoiles"
	elif soup.find("div", {"class": "col-sm-6 product_main"}).find("p", {"class": "star-rating Five"}):
		review_rating = "5 Etoiles"
	else:
		review_rating = "Il n'y a pas de note"
	return review_rating

def get_image_url(soup):
	img = soup.find("div", {"class": "item active"}).find("img")
	img_url = img["src"]
	cleaner = img_url.replace("../../", "")
	img_url = "http://books.toscrape.com/" + cleaner
	return img_url

if response.ok:
	product_page_url = get_product_page_url()
	soup = BeautifulSoup(response.content, 'html.parser')
	upc = get_upc(soup)
	title = get_title(soup)
	price_including_tax = get_price_including_tax(soup)
	price_excluding_tax = get_price_excluding_tax(soup)
	number_available = get_number_available(soup)
	product_description = get_product_description(soup)
	category = get_category(soup)
	review_rating = get_review_rating(soup)
	image_url = get_image_url(soup)
	with open('check_prices.csv', 'w', encoding = 'utf-8-sig') as outf:
		outf.write('product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url\n\n')
		outf.write(product_page_url + "," + upc + "," + title + "," + price_including_tax + "," + price_excluding_tax + "," + number_available + "," + product_description + "," + category + "," + review_rating + "," + image_url)

	'''
	print(product_page_url)
	print(upc)
	print(title)
	print(price_including_tax)
	print(price_excluding_tax)
	print(number_available)
	print(product_description)
	print(category)
	print(review_rating)
	print(image_url)
	'''
	

