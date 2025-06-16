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