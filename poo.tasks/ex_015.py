# Crie um sistema com classes Cliente, Plano e Pagamento para gerenciar cadastro, planos contratados e histórico de pagamentos em uma academia.
from datetime import datetime
class Client():
    def __init__(self, name: str, cpf: int, contact: str):
        self.name = name
        self.cpf = cpf
        self.contact = contact
        self.history_payment = []
        self.frequency = []
    def register_payment(self, value: float, day: None):
        if day is None:
            day = datetime.now()
        else:
            self.history_payment.append({
                "valor": value,
                "dia": day
            })
    def register_frequency(self, data):
        if data not in self.frequency:
            self.frequency.append(data)
        else:
            print(f'Presenção já Registrada')
        