import os
import requests
from bs4 import BeautifulSoup
from lib_product import get_product_informations, get_product_title, get_product_description, get_product_category, get_product_review_rating, get_product_image_url

def get_category_name(soup):
	cat_name = soup.find("div", {"class": "page-header action"}).find('h1')
	return cat_name.text

def extract_category_url_page(url):
	recup_url = [url]
	response = requests.get(url)
	soup = BeautifulSoup(response.content, 'html.parser')
	cat_name = get_category_name(soup)
	next_presence = soup.find("li", {"class": "next"})
	while next_presence:
		link = next_presence.find('a')['href']
		recup_url.append(recup_url[0].replace('index.html','/' + link))
		next_url = recup_url[0].replace('index.html','/' + link)
		response = requests.get(next_url)
		soup = BeautifulSoup(response.content, 'html.parser')
		next_presence = soup.find("li", {"class": "next"})
	return cat_name, recup_url

def get_category_product_url_page(soup):
	links = []
	articles = soup.find_all('div', {'class': 'image_container'})
	for article in articles:
		product_page_url = article.find('a')['href']
		links.append('http://books.toscrape.com/catalogue/' + product_page_url.replace('../',''))
	return links

def get_category_product_data(category_product_url_page, cat_data, list_url_img, list_product_title):
	for url_page in category_product_url_page:
		response = requests.get(url_page)
		if response.ok:
			product_page_url = url_page
			soup = BeautifulSoup(response.content, 'html.parser')
			title = get_product_title(soup)
			title = title.replace('/','')
			upc, price_including_tax, price_excluding_tax, number_available = get_product_informations(soup)
			product_description = get_product_description(soup)
			category = get_product_category(soup)
			review_rating = get_product_review_rating(soup)
			image_url = get_product_image_url(soup)
			results = [product_page_url,upc,title,price_including_tax,price_excluding_tax,number_available,product_description,category,review_rating,image_url]
			cat_data.append(results)
			list_url_img.append(image_url)
			list_product_title.append(title)

def transform_category_data(list_category_url_page):
	cat_data = []
	list_url_img = []
	list_product_title = []
	for elt_list in list_category_url_page:
		response = requests.get(elt_list)
		if response.ok:
			soup = BeautifulSoup(response.content, 'html.parser')
			category_product_url_page = get_category_product_url_page(soup)
			get_category_product_data(category_product_url_page, cat_data, list_url_img, list_product_title)		
	return list_product_title, list_url_img, cat_data

def load_category_data(lis_prod_title, list_prod_url_img, cat_name, cat_data):
	os.mkdir('./data/' + cat_name)
	with open('./data/' + cat_name + '/' + cat_name + '.csv', 'w', encoding="utf-8-sig") as outf:
		outf.write('product_page_url~~universal_product_code~~title~~price_including_tax~~price_excluding_tax~~number_available~~product_description~~category~~review_rating~~image_url\n')
		for i in range(len(cat_data)):
			response = requests.get(list_prod_url_img[i])
			if response.ok:
				img_data = response.content
				with open('./data/' + cat_name + '/' + lis_prod_title[i] + '.jpg', 'wb') as handler:
					handler.write(img_data)
			for j in range(len(cat_data[i])):
				outf.write(cat_data[i][j] + '~~')
			outf.write('\n')
