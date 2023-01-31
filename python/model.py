class Book:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Content: {self.content[:100]}...")
