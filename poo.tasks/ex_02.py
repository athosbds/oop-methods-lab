# Crie uma classe Carro com atributos marca, modelo, ano e velocidade (inicia em 0), métodos acelerar() (aumenta 10), frear() (diminui 10 sem ficar abaixo de 0) e exibir_dados() (mostra os dados do carro).
from time import sleep
class Car():
    def __init__(self, brand, model, year, velocity): 
        self.brand = str(brand)
        self.model = str(model)
        self.year = int(year)
        self.velocity = int(velocity)
    def accelerate(self):
        self.velocity += 10
    def brake(self):
        if self.velocity > 0:
            self.velocity -= 10
        else:
            self.velocity = 0
        return self.velocity
    def details(self):
        print(f'\nMarca: {self.brand}\nModelo: {self.model}\nAno: {self.year}\nVelocidade: {self.velocity} Km/h')

carro_1 = Car('Toyota', 'Corolla', 2020, 0)
carro_1.accelerate()
carro_1.details()
print('Dirigindo...')
sleep(2)
carro_1.brake()
carro_1.details()
