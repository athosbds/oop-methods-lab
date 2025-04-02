#Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

# Programa principal
import coin
price = int(input('Digite um preço: '))
half = coin.half(price)
double = coin.double(price)
increase = coin.increase(price)
print(f'A metade é {half} \n O dobro é {double} \n Aumentando 10% é {increase}')