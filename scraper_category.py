import os
from lib_category import extract_category_url_page, transform_category_data, load_category_data

url = 'http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html'

cat_name, list_category_url_page = extract_category_url_page(url)	

list_product_title, list_product_url_img, category_data = transform_category_data(list_category_url_page)

os.mkdir('data')

load_category_data(list_product_title, list_product_url_img, cat_name, category_data)








			
