import requests
from bs4 import BeautifulSoup
import os
from scraper_category import get_category_url_page, transform_category_data, load_category_data
# Ecriture des fonctions

def get_site_categories_url(url):
	site_cat_url = []
	response = requests.get(url)
	soup = BeautifulSoup(response.content, 'html.parser')
	arts = soup.find('ul', {'class': 'nav nav-list'}).find_all('li')
	for art in arts:
		cat_page_url = art.find('a')['href']
		site_cat_url.append('http://books.toscrape.com/' + cat_page_url.replace('../',''))
	del(site_cat_url[0])
	return site_cat_url

def transform_site_data(list_url):
	os.mkdir('data')
	for url in list_url:
		#print(url)
		cat_name, list_category_url_page = get_category_url_page(url)		
		list_product_title, list_product_url_img, category_data = transform_category_data(list_category_url_page)
		load_category_data(list_product_title, list_product_url_img, cat_name, category_data)


url = 'http://books.toscrape.com'

list_site_categories_url = get_site_categories_url(url)

transform_site_data(list_site_categories_url)