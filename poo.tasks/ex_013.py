# Sistema de Cursos Online: criar/cadastrar cursos e alunos, matricular alunos, adicionar notas, calcular médias e listar alunos por curso.
class Student():
    def __init__(self, name: str, registration: str):
        self.name = name
        self.registration = registration
        self.grades = {}
    def add_grade(self, course_code: str, grade: float ):
            self.grades[course_code] = grade
    def __str__(self):
        return f'{self.name} ({self.registration})'
class Course():
    def __init__(self, name: str, code: str, teacher: str):
        self.name = name
        self.code = code
        self.teacher = teacher
        self.students = {}
    def registration_student(self, student: Student):
        if self.registratration not in self.students:
             self.students[student.registration] = student
        else:
             print(f'Matriculado')


