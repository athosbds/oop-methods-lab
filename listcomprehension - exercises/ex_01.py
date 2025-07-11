## Crie um sistema com cadastro de alunos (nome, 3 notas), método para média e use list comprehension para listar aprovados (média ≥ 7).
students = []
class Student():
    def __init__(self, student, grades):
        self.student = str(student)
        self.grades = grades
    def average(self):
        return sum(self.grades) / len(self.grades)
    def __str__(self):
        return f'{self.student} - Média: {self.average():.2f}'
    
students.append(Student('Athos', [4, 5, 3]))
students.append(Student('Bruna', [8, 9, 7]))
students.append(Student('Carlos', [6, 7, 8]))


approved_students = [student for student in students if student.average() >= 7]
disapprove_students = [student for student in students if student.average() < 7]
print('Aprovados:')
for student in approved_students:
    print(student)
print('\nReprovados:')
for student in disapprove_students:
    print(student)