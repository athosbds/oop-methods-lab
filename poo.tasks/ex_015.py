# Crie um sistema com classes Cliente, Plano e Pagamento para gerenciar cadastro, planos contratados e histórico de pagamentos em uma academia.
from datetime import datetime
class Payment:
    def __init__(self, value: float, data: datetime = None):
        self.value = value
        self.data = data or datetime.now()
    def __str__(self):
        return f"R$: {self.value:.2f} em {self.data.strftime('%d/%m/%Y')}"
class Plan:
    def __init__(self, choice: str, value: float, duration: int, benefits=""):
        self.choice = choice
        self.value = value
        self.duration = duration
        self.benefits = benefits

    def show_info(self):
        info = f'Escolha: {self.choice} - Valor: R$ {self.value:.2f} - Duração: {self.duration} dias'
        if self.benefits:
            info += f'\nBenefícios: {self.benefits}'
        return info
    def __str__(self):
        return self.show_info()
class Client:
    def __init__(self, name: str, cpf: str, contact: str):
        self.name = name
        self.cpf = cpf
        self.contact = contact
        self.plan = None
        self.history_payment = []
        self.frequency = []
    def hire_plan(self, plan: Plan):
        self.plan = plan
        print(f"{self.name} contratou o plano {plan.choice}.")
    def register_payment(self, value: float, day: datetime = None):
        payment = Payment(value, day)
        self.history_payment.append(payment)
    def register_frequency(self, data: datetime):
        if data not in self.frequency:
            self.frequency.append(data)
            print(f'Presença registrada em {data.strftime("%d/%m/%Y")}')
        else:
            print('Presença já registrada.')
    def __str__(self):
        return f"Nome: {self.name} | CPF: {self.cpf} | Contato: {self.contact}" + \
               (f"\nPlano atual: {self.plan.choice}" if self.plan else "\nSem plano contratado")
cliente = Client("João", "12345678900", "11999999999")
plano = Plan("Mensal", 100.0, 30, "Acesso livre a todas as áreas")
cliente.hire_plan(plano)
cliente.register_payment(100.0)
cliente.register_frequency(datetime.now())

print("\n--- DADOS DO CLIENTE ---")
print(cliente)
print("\n--- INFORMAÇÕES DO PLANO ---")
print(cliente.plan.show_info())
print("\n--- HISTÓRICO DE PAGAMENTOS ---")
for pagamento in cliente.history_payment:
    print(pagamento)
