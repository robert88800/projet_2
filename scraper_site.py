from lib_site import extract_site_categories_url, transform_site_data, load_category_data

url = 'http://books.toscrape.com'

list_site_categories_url = extract_site_categories_url(url)

transform_site_data(list_site_categories_url)

