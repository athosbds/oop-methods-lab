#Você vai criar um sistema simples para cadastrar alunos e suas notas, usando classes (POO), e vai
class Student():
    def __init__(self, name, age):
        self.name = str(name)
        self.age = int(age)
        self.grades = []
    def ad_grade(self, grade):
        self.grades.append(grade)
    def avarage(self):
        if len(self.grades) == 0:
            return 0 
        return sum(self.grades) / len(self.grades)
    def __str__(self):
        print(f'\nNome Aluno: {self.name}\nIdade: {self.age}\nNotas: {self.grades}\n Média: {self.avarage()}')

students = {}
