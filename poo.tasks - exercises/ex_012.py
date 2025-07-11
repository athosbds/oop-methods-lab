# Sistema de tarefas com POO: crie classes para adicionar, listar, concluir e filtrar tarefas por status e prioridade.
class Work():
    def __init__(self, title, priority, completed=False):
        self.title = str(title)
        self.priority = int(priority)
        self.completed = bool(completed)
    def conclude(self, completed):
        self.completed = True
    def __str__(self):
        status = 'Concluída' if self.completed else 'Pendente'
        return f'Tarefa: {self.title} - Prioridade: {self.priority} Status: {status}'
class TaskManager():
    def __init__(self):
        self.works = []
    def ad_work(self, title, priority):
        new_work = Work(title, priority)
        self.works.append(new_work)
    def display_works(self):
        for work in self.works:
           status =  "✅" if work.completed else "⏳"
           print(f'Status: {status} - Tarefa: {work.title} - Prioridade: {work.priority} - ')
    def filter_by_status(self, completed=True):
        return [work for work in self.works if work.completed == completed]
manager = TaskManager()
manager.ad_work("Estudar Python", 1)
manager.ad_work("Lavar a louça", 3)
manager.ad_work("Fazer exercícios", 2)
print("=== Tarefas antes de concluir ===")
manager.display_works()
manager.works[0].conclude(True)
manager.works[1].conclude(True)
# Mostrar as tarefas depois de concluir
print("\n=== Tarefas depois de concluir uma ===")
manager.display_works()
print()
for t in manager.filter_by_status(completed=False):
    print(t)
for t in manager.filter_by_status(completed=True):
    print(t)
