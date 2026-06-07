
class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    
    def read(self):
        print(f"I am reading a book called {self.title} by {self.author}")
        
        
    def describe(self):
        print(f"The book is called {self.title} by {self.author} and has {self.pages} pages")