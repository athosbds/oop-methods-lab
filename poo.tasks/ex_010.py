## Classe Produto: nome, preco, quantidade; métodos: adicionar_estoque(qtd), remover_estoque(qtd), mostrar_produto(); desafio: calcular valor total (preco * quantidade)

class Product():
    def __init__(self, name, price, quantity):
        self.name = str(name)
        self.price = float(price)
        self.quantity = float(quantity)
    def adc_stock(self, value):
        self.quantity += value
    def remove_stock(self, value):
        if self.quantity >= value:
            self.quantity -= value
        else:
            return 'Insuficiente'
    def value_total(self):
        return self.price * self.quantity
    def show_product(self):
        return f'Produto: {self.name}\nPreço: {self.price}\nQuantidade: {self.quantity}'
        
product = Product("Caneta", 2.5, 10)
print(product.show_product())
product.adc_stock(5)
print(product.show_product())
product.remove_stock(3)
print(product.show_product())
print("Valor total do estoque:", product.value_total())
