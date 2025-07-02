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