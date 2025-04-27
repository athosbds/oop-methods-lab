#Você deve desenvolver um sistema em Python com Programação Orientada a Objetos para gerenciar uma turma de alunos. O sistema deve funcionar de forma interativa, utilizando um laço while que continuará rodando até que o professor deseje encerrar.

class Student():
    def __init__(self, name, grades):
        self.name = str(name)
        self.grades = grades
    def avarage(self):
        return sum(self.grades) / len(self.grades)
class ClassesStudents():
    def __init__(self):
        self.class_students =[]
    def adc_student(self, student):
        self.class_students.append(student)
    def clear_students(self):
        self.class_students.clear()
    def show_details(self):
        if not self.class_students:
            print('\nNenhum Aluno')
        for student in self.class_students:
            print(f'Aluno: {student.name}\nNotas: {student.grades}')
        
def options():
    class_01 = ClassesStudents()
    while True:
        print(""" Registro De Classe
1 - Adicionar Estudante
2 - Listar Alunos
3 - Limpar Cache
4 - Sair""")
        try:
            choose = int(input('\nOpção: '))
            if choose == 1:
                name = str(input('Nome: '))
                grade = [float(input('Nota: ')) for x in range(3)]
                student = Student(name, grade)
                class_01.adc_student(student)
            if choose == 2:
                print(f'\nREGISTRO DA TURMA\n')
                class_01.show_details()
            if choose == 3:
                class_01.clear_students()
            if choose == 4:
                print('Finalizando.')
                break
        except (ValueError, IndexError):
            print('ERRO! OPÇÃO OU VALOR ERRADO.')
options()