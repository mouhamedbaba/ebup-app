from tkinter import *


class BookViewer:
    def __init__(self, master, book):
        self.master = master
        self.book = book
        self.title_label = Label(master, text=book.title)
        self.author_label = Label(master, text=book.author)
        self.content_text = Text(master, height=20, width=50)
        self.content_text.insert(END, book.content)

        self.title_label.pack()
        self.author_label.pack()
        self.content_text.pack()

    def show(self):
        self.master.mainloop()
