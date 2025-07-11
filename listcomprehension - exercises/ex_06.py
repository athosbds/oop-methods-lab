## Crie um dicionário com cada palavra e sua quantidade de consoantes (sem contar vogais)
words = ["banana", "apple", "grape", "orange", "kiwi", "avocado"]
vowels = 'aeiou'
new_vowels = {word: sum(1 for letter in word if letter not in vowels )for word in words}
print(new_vowels)