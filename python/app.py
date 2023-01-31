
import os
from ebooklib import epub
from bs4 import BeautifulSoup
import model
import view
import controller

# class Controller:
#     def __init__(self, model, view):
#         self.model = model
#         self.view = view
#
#     def bind_events(self):
#         self.view.some_button.bind("<Button-1>", self.on_some_button_clicked)
#         self.view.some_menu_item.bind("<Button-1>", self.on_some_menu_item_clicked)
#
#     def on_some_button_clicked(self, event):
#         # code to handle the button click event
#         pass
#
#     def on_some_menu_item_clicked(self, event):
#         # code to handle the menu item click event
#         pass



def lire_livre(rep):
    rep = "livres"
    """Fonction pour lire un livre ePub"""
    # Récupérer la liste des livres ePub dans le répertoire
    livres = [f for f in os.listdir(rep) if f.endswith('.epub')]

    # Demander à l'utilisateur de choisir un livre
    for i, livre in enumerate(livres):
        print(i + 1, livre)

    livre_choisi = int(input("Choisir un livre (1 - " + str(len(livres)) + ") :")) - 1

    # Ouvrir le livre choisi
    book = epub.read_epub(rep + livres[livre_choisi])

    # Récupérer les informations sur le livre
    print("Titre :", book.get_metadata('DC', 'title')[0][0])
    print("Auteur :", book.get_metadata('DC', 'creator')[0][0])

    # Récupérer la table des matières
    toc = book.get_toc()

    # Afficher la table des matières
    for item in toc:
        print(item[0])

    # Demander à l'utilisateur de choisir un chapitre
    chapitre = int(input("Choisir un chapitre (1 - " + str(len(toc)) + ") :"))

    # Récupérer le contenu du chapitre choisi
    chapitre_item = book.get_item_with_href(toc[chapitre - 1][1])
    content = chapitre_item.get_content()

    # Formater le contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')

    # Ajouter du CSS pour la mise en forme
    style = """
    <style>
    body {
        font-family: Arial, sans-serif;
        font-size: 16px;
        line-height: 1.5;
        margin: 0;
        padding: 0;
    }

    h1, h2, h3 {
        font-weight: bold;
        margin-top: 1em;
    }

    p {
        margin-top: 0.5em;
        margin-bottom: 0.5em;
    }

    img {
        max-width: 100%;
        height: auto;
    }
    </style>
    """
    soup.head.append(style)

    # Afficher le contenu formaté
    print(soup.prettify())

# Répertoire contenant les livres ePub
rep = "livres/"

# Lire le livre ePub
lire_livre(rep)

