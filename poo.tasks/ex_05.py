#Construir um sistema para gerenciar alunos de uma turma, registrando seus nomes, notas e calculando médias individuais e da turma.

class Student():
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    def avarage(self):
        return sum(self.grades) / len(self.grades)
class Class():
    def __init__(self):
        self.students = []
    def add_student(self, user):
        self.students.append(user)
    def show_details(self):
        for student in self.students:
            print(f'Aluno: {student.name}\nNotas: {student.grades}')
student_01 = Student('Athos', [6.5, 7.6, 8.8])
class_01 = Class()
class_01.add_student(student_01)
class_01.show_details()