import requests
from bs4 import BeautifulSoup
from lib_product import extract_product_data, transform_product_data, load_product_data

url = 'http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html'

response, soup = extract_product_data(url)

product_page_url, upc, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url = transform_product_data(response, soup)

load_product_data(product_page_url, upc, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url)





	

