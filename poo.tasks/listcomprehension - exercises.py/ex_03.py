#Dada a lista de palavras abaixo, crie uma nova lista contendo apenas as palavras que têm mais de 5 letras, usando list comprehension.

words = ['Cachorro', 'Sol', 'Avestruz', ' Cuscuz', 'Rocambole', 'Novo', 'Deus']
new_words = [word for word in words if len(word) > 5]
print(f'Todas as Palavras:\n{words}')
print(f'Palavras com 5+ letras\n{new_words}')