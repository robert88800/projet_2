import requests
from bs4 import BeautifulSoup

# Ecriture des fonctions

def get_product_page_url():
	return response.url

def get_product_informations(soup):
	for tr_tag in soup.find("table", {"class": "table table-striped"}).find_all("tr"):
		if tr_tag.find("th").text == "UPC":
			upc = tr_tag.find("td").text
		elif tr_tag.find("th").text == "Price (incl. tax)":
			pit = tr_tag.find("td").text
		elif tr_tag.find("th").text == "Price (excl. tax)":
			pet = tr_tag.find("td").text
		elif tr_tag.find("th").text == "Availability":
			na = tr_tag.find("td").text
		else :
			continue
	return upc, pit, pet, na

def get_product_title(soup):
	title = soup.title.string
	title = title.replace("\n","").replace(',','.')
	title = title.replace(" | Books to Scrape - Sandbox","")
	title = title.strip()
	return title

def get_product_description(soup):
	if soup.find("div", {"id": "product_description"}):
		pd = soup.find("div", {"id": "product_description"}).find_next("p")
		return pd.text.replace(',','.').replace('"','').replace("'",'')
	else:
		return "No description available"

def get_product_category(soup):
	cat = soup.find("li", {"class": "active"}).find_previous("a")
	return cat.text

def get_product_review_rating(soup):
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

def get_product_image_url(soup):
	img = soup.find("div", {"class": "item active"}).find("img")
	img_url = img["src"]
	img_url = "http://books.toscrape.com/" + img_url.replace("../../", "")
	return img_url

def extract_product_data(url):
	response = requests.get(url)
	if response.ok:
		soup = BeautifulSoup(response.content, 'html.parser')
	return response, soup 

def transform_product_data(response, soup):
	product_page_url = get_product_page_url()
	title = get_product_title(soup)
	upc, price_including_tax, price_excluding_tax, number_available = get_product_informations(soup)
	product_description = get_product_description(soup)
	category = get_product_category(soup)
	review_rating = get_product_review_rating(soup)
	image_url = get_product_image_url(soup)
	return product_page_url, upc, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url

def load_product_data(product_page_url, upc, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url):
	with open('check_product_price.csv', 'w', encoding="utf-8-sig") as outf:
		outf.write('product_page_url,universal_product_code,title,price_including_tax,price_excluding_tax,number_available,product_description,category,review_rating,image_url\n')
		outf.write(product_page_url + ',' + upc + ',' + title + ',' + price_including_tax + ',' + price_excluding_tax + ',' + number_available + ',' + product_description + ',' + category + ',' + review_rating + ',' + image_url)

'''
url = 'http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html'

response, soup = extract_product_data(url)

product_page_url, upc, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url = transform_product_data(response, soup)

load_product_data(product_page_url, upc, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url)
'''




	
