# Import des modules nécessaires
import os
import requests
from bs4 import BeautifulSoup
from lib_category import extract_category_url_page, transform_category_data, load_category_data

# Obtention des URL pour chaque catégorie du site
def extract_site_categories_url(url):
	site_cat_url = []
	response = requests.get(url)
	soup = BeautifulSoup(response.content, 'html.parser')
	arts = soup.find('ul', {'class': 'nav nav-list'}).find_all('li')
	for art in arts:
		cat_page_url = art.find('a')['href']
		site_cat_url.append('http://books.toscrape.com/' + cat_page_url.replace('../',''))
	del(site_cat_url[0])
	return site_cat_url

# Transformation de la donnée et chargement de celle-ci dans un fichier csv
def transform_site_data(list_url):
	os.mkdir('data')
	for url in list_url:
		print(url)
		cat_name, list_category_url_page = extract_category_url_page(url)		
		list_product_title, list_product_url_img, category_data = transform_category_data(list_category_url_page)
		load_category_data(list_product_title, list_product_url_img, cat_name, category_data)
