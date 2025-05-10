#Crie uma lambda que multiplica cada número da lista abaixo por 5 e, em seguida, filtra os resultados para manter apenas os números maiores que 20. Use map para multiplicar e filter para filtrar os resultados.

numbers = [2, 4, 6, 8, 10, 12]
multiplied_numbers = list(map(lambda x: x * 5, numbers ))
filtered_numbers = list(filter(lambda x: x > 20, multiplied_numbers))
print(filtered_numbers)