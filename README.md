"Utilisation d'un scraper pour le suivi des prix des livres d'occasion"

> Pour accéder au dépôt distant du scraper et le copier en local,
nous utiliserons Git.
Nous nous assurons que Git est installé sur la machine avec : git config --list, nous clonons ensuite le repository distant dans un répertoire local avec : https://github.com/robert88800/projet_2.

Nous nous assurons que l'interpréteur Python est installé sur la machine,on peut le vérifier avec : python3 -V pour Ubuntu et py -3 -V pour Windows. 
'''
Avant d'installer l'environnement virtuel des futurs scripts, on vérifier l'existence du module Python venv, qui permet de créer et gérer des environnements virtuels avec : python3 -m venv --help pour Ubuntu et py -3 -m venv --help pour W. 
Nous créons l'environnement virtuel du projet avec : python3 -m venv env et nous l'activons avec source env/bin/activate pour Ubuntu et env\scripts\avtivate pour Windows.
'''
Nous installons les paquets Python répertoriés dans le fichier requirements.txt avec : pip3 install -r requirements.txt.

Le script scraper_product.py permet de scraper un livre, il suffit d'affecter l'url visée à la variable url, de supprimer les guillemets et de lancer le script dans un terminal. Il en est de même pour les scripts scraper_category.py et scraper_site.py, qui respectivement permettent de scrapper une catégorie de livres et toutes les scatégories de livres.
