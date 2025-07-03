# Sistema de farmácia com POO: cadastre clientes/medicamentos, controle vendas, estoque e compras por CPF
class Customer():
    def __init__(self, name: str, cpf: int):
        self.name = name
        self.cpf = cpf
        self.history = []
    def make_purchase(self, medicine, quantity):
        buy = {
            "medicamento": medicine,
            "quantidade": quantity
        }
        self.history.append(buy)
    def show_history(self):
        if not self.history:
            print('NENHUM MEDICAMENTO CADASTRADO.')
        else:
            for i, buy in enumerate(self.history, start=1):
                print(f"{i} {buy['quantidade']}x {buy['medicamento']}")
class Medicine():
    def __init__(self, code: int, name: str, manufacturer: str, price: float, quantity: int):
        self.code = code
        self.name = name
        self.manufacturer = manufacturer
        self.price = price
        self.quantity = quantity
    def update_stock(self, code, quantity):
        if code == self.code:
            if self.quantity + quantity >= 0:
                self.quantity += quantity
            else:
                print('Estoque Insuficiente.')
        else:
            print(f'Medicamento Não Encontrado.')
    def availability(self):
        return self.quantity > 0