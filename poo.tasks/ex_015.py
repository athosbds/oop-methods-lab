# Crie um sistema com classes Cliente, Plano e Pagamento para gerenciar cadastro, planos contratados e histórico de pagamentos em uma academia.
from datetime import datetime
class Payment():
    def __init__(self, value: float, data: datetime = None):
        self.value = value
        self.data = data or datetime.now()
    def __str__(self):
        return f"R$: {self.value} em {self.data.strftime('%d/%m/%Y')}"
        
class Plan():
    def __init__(self, choice: str, value: float, duration: int, benefits=""):
        self.choice = choice
        self.value = value
        self.duration = duration
        self.benefits = benefits
    def show_info(self):
        info = f'Escolha: {self.choice} - Valor: {self.value} - Duração: {self.duration}'
        if self.benefits:
            info += f'\nBenefícios: {self.benefits}'
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

