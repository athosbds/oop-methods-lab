## Crie um sistema com cadastro de alunos (nome, 3 notas), método para média e use list comprehension para listar aprovados (média ≥ 7).
students = []
class Student():
    def __init__(self, student):
        self.student = str(student)
        self.grades = []
    def average(self):
        return sum(self.grades) / len(self.grades)
    
caio_ribeiro = Student('Caio Ribeiro')
caio_ribeiro.grades = [4, 3, 5]
students.append(caio_ribeiro)
print(students)