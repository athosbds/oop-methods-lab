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
        if student.registration not in self.students:
             self.students[student.registration] = student
        else:
             print(f'Matriculado')
    def add_grade(self, student: str, grade: float):
        if student in self.students:
            self.students[student].add_grade(self.code, grade)
        else:
             print('Aluno Não Encontrado nesse Curso.')
    def list_students(self):
         for student in self.students.values():
              print(student)
student1 = Student('Athos', '96564')
student2 = Student('Bianca', '12345')
english_course = Course('Inglês', '001', 'Carlos')
english_course.registration_student(student1)
english_course.registration_student(student2)
english_course.add_grade('96564', 8.5)
english_course.add_grade('12345', 9.0)
print("\nAlunos matriculados no curso de Inglês:")
english_course.list_students()
