#Crie uma classe chamada Livro com os atributos titulo, autor e paginas, um método __init__ para inicializar esses atributos, um método exibir_detalhes() que imprime os detalhes do livro e um método eh_grande() que retorna True se o livro tiver mais de 300 páginas, senão retorna False.

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def details_book(self):
        print(f'Título: {self.title}\nAutor: {self.author}\nPáginas: {self.pages}')
    def big_book(self):
        if self.pages >= 300:
            print('Livro: Grande')
        else:
            print('Livro: Pequeno')
book1 = Book('Pequeno Príncipe', 'Antoine de Saint-Exupéry', 100)
book1.details_book()
book1.big_book()
print()
book2 = Book('Hamlet', 'Shakeaspere', 300)
book2.details_book()
book2.big_book()