
palavras = ["casa", "computador", "livro", "inteligência", "sol", "mesa", "python"]
five_words = [word.upper() for word in palavras if len(word) > 5 else word for word in palavras]
print(five_words)