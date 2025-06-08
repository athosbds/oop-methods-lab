# Exercício: simule um banco de dados com POO usando dicionários para cadastrar, buscar, atualizar e remover usuários.
class User():
    def __init__(self):
        self.users = {}
        self.id = 1
    def adc_user(self, name, email):
        self.users[self.id] = {
            'nome': name,
            'email': email
        }
        print(f'Usuário adicionado {self.name}')
        self.id += 1
    def del_user(self, id_user):
        if id_user in self.users:
            del self.users(id_user)
            print(f'Usuário {self.id_user} deletado')
        else:
            print(f'Usuário não encontrado.')
