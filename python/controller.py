from tkinter import Tk
import model
import view


class BookController:
    def __init__(self, book_file):
        self.book_model = model.BookModel(book_file)
        self.root = Tk()
        self.book_view = view.BookViewer(self.root, self.book_model)

    def show_book(self):
        self.book_view.show()
