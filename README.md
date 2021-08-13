<div style="border: 1px solid RGB(155, 95, 240);">
<h1 style="margin: auto; padding: 30px; color: RGB(155, 95, 240);">Utilisation d'un scraper pour le suivi des prix des livres d'occasion</h1>
</div>   
<div style="border: 1px solid RGB(155, 95, 240);">
<h1 style="margin: auto; padding: 20px; color: RGB(155, 95, 240);">Git</h1>              
</div>   
> Nous ferons appel à Git pour accéder au dépôt distant du scraper et le copier en local, nous nous assurons qu'il est installé sur la <br/> <br/> machine avec : <br/> <br/> __git config --list__, <br/> <br/> nous clonons ensuite le repository distant dans un répertoire local avec : <br/> <br/> __https://github.com/robert88800/projet_2__.
<div style="border: 1px solid RGB(155, 95, 240);">
<h1 style="margin: auto; padding: 20px; color: RGB(155, 95, 240);">Python</h1>             
</div>  
> Nous nous assurons que l'interpréteur Python est installé sur la machine, on peut le vérifier avec : <br/> <br/> __python3 -V__ pour Ubuntu, <br/> <br/> __py -3 -V__ pour Windows.
<div style="border: 1px solid RGB(155, 95, 240);">
<h1 style="margin: auto; padding: 20px; color: RGB(155, 95, 240);">Environnement virtuel</h1>    
</div>  
>Avant d'installer l'environnement virtuel des futurs scripts, on vérifie l'existence du module Python venv, qui permet de créer et gérer des <br/> <br/> environnements virtuels avec : <br/> <br/> __python3 -m venv --help__ pour Ubuntu, <br/> <br/> __py -3 -m venv --help__ pour Windows. <br/> <br/>
Nous créons l'environnement virtuel du projet avec : <br/> <br/>
__python3 -m venv env__, <br/> <br/> nous l'activons avec : <br/> <br/> __source env/bin/activate__ pour Ubuntu, <br/> <br/> __env\scripts\activate__ pour Windows.
<div style="border: 1px solid RGB(155, 95, 240);">
<h1 style="margin: auto; padding: 20px; color: RGB(155, 95, 240);">Paquets utiles</h1>           
</div>
> Nous installons les paquets Python répertoriés dans le fichier __requirements.txt__ avec : <br/> <br/> __pip3 install -r requirements.txt__.
<div style="border: 1px solid RGB(155, 95, 240);">
<h1 style="margin: auto; padding: 20px; color: RGB(155, 95, 240);">Exécution des scripts de scraping</h1>                                     
</div>
> Le script __scraper_product.py__ permet de scraper un livre, il suffit d'affecter l'url visée à la variable url et de le lancer dans un terminal. <br/> <br/>  Il en est de même pour les scripts __scraper_category.py__ et __scraper_site.py__, qui respectivement permettent de scraper une catégorie de livres <br/> <br/> et toutes les scatégories de livres du site __http://books.toscrape.com__.    

# Dillinger
## _The Last Markdown Editor, Ever_

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Dillinger is a cloud-enabled, mobile-ready, offline-storage compatible,
AngularJS-powered HTML5 Markdown editor.

- Type some Markdown on the left
- See HTML in the right
- ✨Magic ✨                                                                                       
