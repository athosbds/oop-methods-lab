#Você vai criar um sistema simples de carrinho de compras que guarda os produtos em um dicionário dentro da classe.

class ShoppingCart():
    def __init__(self):
        self.itens = {}
    def ad_item(self, name, amount):
        if name in self.itens:
            self.itens[name] += amount 
        else:
            self.itens[name] = amount
    def del_item(self, name):
        if name not in self.itens:
            print('Item não encontrado.')
        else:
            del self.itens[name]
    def show_shoppingcar(self):
        if not self.itens:
            print('Carrinho vazio.')
        else:
            print('-------- Produtos do carrinhio --------\n')
            for product, amount in self.itens.items():
                print(f'Produto: {product} - Quantidade: {amount}')
    def clear_shoppingcart(self):
        self.itens.clear()
        print('Carrinho vazio.')

cart = ShoppingCart()
cart.ad_item('Feijão', 2)
cart.ad_item('Arroz', 3)
cart.show_shoppingcar()