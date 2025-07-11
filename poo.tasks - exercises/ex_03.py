#Criar um sistema para gerenciar funcionários de uma empresa. Cada tipo de funcionário (como gerente, assistente e desenvolvedor) terá características específicas e métodos para calcular salários, com a possibilidade de implementar bônus e descontos específicos de cada cargo.

class Employee():
    def __init__(self, name, age, base_salary):
        self.name = str(name)
        self.age = int(age)
        self.base_salary = float(base_salary)
    def employee_salary(self):
        return self.base_salary
    def show_info(self):
        print(f'\nNome do Funcionário: {self.name}\nIdade: {self.age}\nSalário: R$ {self.employee_salary()}') 
class Manager(Employee):
    def __init__(self, name, age, base_salary, bonus):
        super().__init__(name, age, base_salary)
        self.bonus = float(bonus)
    def managing_salary(self):
        return self.base_salary + self.bonus
    def managing_info(self):
        print(f'\nNome do Gerente: {self.name}\nIdade: {self.age}\nSalário: R${self.managing_salary()}')
class Developer(Employee):
    def __init__(self, name, age, base_salary, discount):
        super().__init__(name, age, base_salary)
        self.discount = float(discount)
    def developer_salary(self):
        return self.base_salary + self.discount
    def developer_info(self):
        print(f'\nNome do Desenvolvedor: {self.name}\nIdade: {self.age}\nSalário: R$ {self.developer_salary()}')

employee_1 = Employee('Pedro', 18, 1250)
employee_1.show_info()
manager_1 = Manager('Lucas', 30, 2500, 1000)
manager_1.managing_info()
developer_1 = Developer('David', 33, 4000, 1000)
developer_1.developer_info()