
palavras = ["casa", "computador", "livro", "inteligência", "sol", "mesa", "python"]
five_words = [word.upper()if len(word) > 5 else word for word in palavras]
print(five_words)