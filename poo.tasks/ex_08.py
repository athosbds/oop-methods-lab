#Esse exercício é interessante porque exige que você trabalhe com um cenário mais próximo do mundo real, onde as compras impactam o saldo do cartão e as interações entre objetos são mais dinâmicas.

class Credit_Card():
    def __init__(self, number, title, limit, balance=0.0):
        self.number = str(number)
        self.title = str(title)
        self.limit = float(limit)
        self.balance = float(balance)
    def make_purchase(self, value):
        if self.balance + value <= self.limit:
            self.balance += value
            print(f'Compra de R${value} EFETUADA.')
        else:
            print(f'Compra negada: LIMITE.')
    def show_limit(self):
        return self.limit - self.balance
    def pay_balance(self, value):
        if value <= self.balance:
            self.balance -= value
            print(f'Pagamento: R$ {value} EFETUADO.')
        else:
            print('Pagamento mais alto que o saldo. NEGADO.')
    def show_balance(self):
        print(f'Fatura: R$: {self.balance}')
class Bank():
    def __init__(self, title_name):
        self.title_name = str(title_name)
        self.cards = []