#Crie uma list comprehension que gere uma lista com os quadrados dos números pares de 1 a 20 (inclusive).

numbers = [1, 2, 3, 4, 5, 6 , 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
numbers_pairs = [number **2 for number in numbers if number % 2 == 0]
print(numbers_pairs)