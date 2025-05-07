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

class Bank():
    def __init__(self, title_name):
        self.title_name = str(title_name)
        self.cards = []