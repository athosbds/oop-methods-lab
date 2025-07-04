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
    de
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
# Criar medicamentos
med1 = Medicine(101, "Paracetamol", "Medley", 10.00, 50)
med2 = Medicine(102, "Ibuprofeno", "Neo Química", 15.00, 30)

# Criar cliente
cliente1 = Customer("Athos", 12345678900)

# Cliente faz compras
cliente1.make_purchase(med1, 2)
cliente1.make_purchase(med2, 1)

# Atualizar estoque manualmente após a compra
med1.update_stock(101, -2)
med2.update_stock(102, -1)

# Mostrar histórico de compras
print("\nHistórico de compras da cliente:")
cliente1.show_history()

# Verificar disponibilidade
print("\nDisponibilidade dos medicamentos:")
print(f"{med1.name}: {'Disponível' if med1.availability() else 'Indisponível'} (Estoque: {med1.quantity})")
print(f"{med2.name}: {'Disponível' if med2.availability() else 'Indisponível'} (Estoque: {med2.quantity})")
