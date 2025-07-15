# Sistema simples para gerenciar estudantes: adicionar, excluir e listar.

class Student():
    def __init__(self, name: str, age: int, registration: str, course: str):
        self.name = name
        self.age = age
        self.registration = registration
        self.course = course
    def show_information(self):
        return f'Aluno: {self.name} - Idade: {self.age} - Matrícula: {self.registration} - Curso: {self.course}'
    def __str__(self):
        return f'Aluno: {self.name} - Idade: {self.age} - Matrícula: {self.registration} - Curso: {self.course}'
class StudentSystem():
    def __init__(self):
        self.students = {}
    def add_students(self, name, age, registration, course):
        if registration in self.students:
            print('Estudante  já Cadastrado.')
        else:
            self.students[registration] = Student(name, age, registration, course)
    def delete_student(self, registration):
        if registration in self.students:
            del self.students[registration]
        else:
            print(f'Estudante não encontrado.')
    def update_registration(self, registration, new_name=None, new_age=None, new_course=None):
        if registration in self.students:
            student = self.students[registration]
            if new_name is not None:
                student.name = new_name
            if new_age is not None:
                student.age = new_age
            if new_course is not None:
                student.course = new_course
        else:
            print(f'Estudante não encontrado.')
    def show_students(self):
        for idx, student in enumerate(self.students.values(), start=1):
            print(f'{idx}. {student.show_information()}')
system = StudentSystem()
while True:
    print("""
1 - Adicionar Estudante
2 - Deletar Estudante
3 - Atualizar Registro
4 - Mostrar Estudantes
5 - Sair""")
    choose = str(input('Escolha: '))
    if choose == '1':
        print('\n-------Adicionando Estudante-------')
        name = str(input('Nome: '))
        age = int(input('Idade: '))
        registration = str(input('Matrícula: '))
        course = str(input('Curso: '))
        system.add_students(name, age, registration, course)
    if choose == '2':
        print('-------Deletando Estudante-------')
        registration = str(input('Matrícula Estudante: '))
        system.delete_student(registration)
    if choose == '3':
        print('-------Atualizando Dados-------')
        registration = str(input('Matrícula: '))
        new_name = str(input('Nome: '))
        new_age = int(input('Idade: '))
        new_course = str(input('Curso: '))
        system.update_registration(registration, new_name, new_age, new_course)
    if choose == '4':
        system.show_students()
    if choose == '5':
        break

        
