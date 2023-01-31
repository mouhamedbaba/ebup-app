import os
import tkinter as tk
from tkinter import ttk
from ebooklib import epub
from bs4 import BeautifulSoup
from flask import Flask, render_template
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.select_book_label = tk.Label(self, text="Select a book:")
        self.select_book_label.pack()

        self.books_combobox = ttk.Combobox(self)
        self.books_combobox.pack()

        self.select_chapter_label = tk.Label(self, text="Select a chapter:")
        self.select_chapter_label.pack()

        self.chapters_combobox = ttk.Combobox(self)
        self.chapters_combobox.pack()

        self.show_content_button = tk.Button(self, text="Show Content", command=self.show_content)
        self.show_content_button.pack()

        self.content_text = tk.Text(self, height=20, width=50)
        self.content_text.pack()

    def show_content(self):
        book_file = self.books_combobox.get()
        chapter_number = self.chapters_combobox.get()
        
        # Répertoire contenant les livres ePub
        rep = "livres"

        # Lire le livre ePub
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



        self.content_text.insert("1.0", content)

def lire_livre(rep):
    """Fonction pour lire un livre ePub"""
    # Récupérer la liste des livres ePub dans le répertoire
    livres = [f for f in os.listdir(rep) if f.endswith('.epub')]

    return livres

rep = "livres"
livres = lire_livre(rep)

root = tk.Tk()
app = Application(master=root)
app.books_combobox['values'] = livres
app.mainloop()
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
print(soup.prettify())

