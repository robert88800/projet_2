# Utilisation d'un scraper pour le suivi des prix des livres d'occasion

## Git

Nous ferons appel à Git pour accéder au dépôt distant du scraper et le copier en local, nous nous assurons qu'il est installé sur la machine avec : 

```sh
git config --list
 ```

Nous clonons ensuite le repository distant dans un répertoire local avec :

__https://github.com/robert88800/projet_2__

## Python

Nous nous assurons que l'interpréteur Python est installé sur la machine, on peut le vérfier avec pour Ubuntu :

```sh
python3 -V
```

pour Windows :

```sh
py -3 -V
```

## Environnement virtuel

Avant d'installer l'environnement virtuel des futurs scripts, on vérifie l'existence du module Python venv, qui permet de créer et gérer des environnements virtuels avec pour Ubuntu :

```sh
python3 -m venv --help 
```

pour Windows:

```sh
py -3 -m venv --help
```

Nous créons l'environnement virtuel du projet avec pour Ubuntu :

```sh
python3 -m venv env
```

pour Windows :

```sh
py -3 -m venv env
```

Nous l'activons avec pour Ubuntu :

```sh
source env/bin/activate
```

pour Windows : 

```sh
env\scripts\activate
```

## Paquets utiles

Nous installons les paquets Python répertoriés dans le fichier __requirements.txt__ avec :

```sh
pip3 install -r requirements.txt
```

## Exécution des scripts de scraping

Le script __lancer_le_scraper__ permet de scraper un livre, une catégorie ou l'ensemble du site  __'Books to Scrape'__, il suffit de répondre à la 1ère question par : __produit__ ou __catégorie__ ou __site__, à la 2ème question on renseigne l'URL voulue, le traitement va ensuite avoir lieu. Le résultat sera sous format d'un fichier __csv__ dans le cas d'un produit, sinon un dossier __'data'__ sera généré contenant l'ensemble des images et des fichiers CSV dans le répertoire où nous nous trouvons.