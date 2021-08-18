# Affectation de la variable "choice"
choice = ""

# Dire bonjour à l'utilisateur et demander ce qu'il veut scraper 
print("")
print("Bonjour, vous allez pouvoir scraper sur le site 'Books to Scrape'!!!")
print("")
while choice not in ("produit", "catégorie", "site"):
    print("Voulez-vous scraper un produit, une catégorie ou le site ?")
    print("")
    choice = input()

# Lancer le script 
if choice == "produit":
    print("")
    print("Pouvez-vous renseigner l'URL d'un produit, merci !")
    print("")
    url = input()
    from lib_product import extract_product_data, transform_product_data, load_product_data
    response, soup = extract_product_data(url)
    product_page_url, upc, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url = transform_product_data(response, soup)
    load_product_data(product_page_url, upc, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url)
elif choice == "catégorie":
    print("")
    print("Pouvez-vous renseigner l'URL d'une catégorie, merci !")
    print("")
    url = input()
    import os
    from lib_category import extract_category_url_page, transform_category_data, load_category_data
    cat_name, list_category_url_page = extract_category_url_page(url)
    list_product_title, list_product_url_img, category_data = transform_category_data(list_category_url_page)
    os.mkdir('data')
    load_category_data(list_product_title, list_product_url_img, cat_name, category_data)
else :
    print("")
    print("Traitement en cours des URL suivants :")
    print("")
    from lib_site import extract_site_categories_url, transform_site_data
    list_site_categories_url = extract_site_categories_url('http://books.toscrape.com')
    transform_site_data(list_site_categories_url)

# Dire "au revoir !"
print("")
print("Le traitement est terminé !")
print("")
print("A bientôt !")
print("")
