# Crie classes Livro e Biblioteca; Biblioteca deve adicionar livros e listar títulos com ano >= 2000 e avaliação > 8 usando list comprehension.
class Book():
    def __init__(self, title, author, year, grade):
       self.title = str(title)
       self.author = str(author)
       self.year = int(year)
       self.grade = float(grade)
    def __str__(self):
        return f'{self.title} - {self.author} - {self.year} - {self.grade}'
class BookStore():
    def __init__(self):
        self.bookstore = []
    def add_book(self, book):
        self.bookstore.append(book)
    def show_well_grades(self):
        return [book.title for book in self.bookstore if book.year >= 2000 and book.grade > 8]
    def __iter__(self):
        return iter(self.bookstore)
shakespeare_book = Book('Hamlet', 'Shakespeare', 1623, 8.5)
rocambole = Book('Rocam', 'Otávio', 2002, 8.5)
bookstore = BookStore()
bookstore.add_book(shakespeare_book)
bookstore.add_book(rocambole)
print('\nLivros')
for book in bookstore:
    print(book)
print('Livros Bons:')
print(bookstore.show_well_grades())