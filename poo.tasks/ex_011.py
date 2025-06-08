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
        print(f'Usuário adicionado {name}')
        self.id += 1
    def del_user(self, id_user):
        if id_user in self.users:
            name = self.users[id_user]['nome']
            del self.users[id_user]
            print(f'{name} deletado.')
        else:
            print(f'Usuário não encontrado.')
    def list_users(self):
        if not self.users:
            print(f'Nenhuma usuário cadastrado.')
        else:
            for user, data in self.users.items():
                print(f'ID: {user} | Nome: {data['nome']} | Email: {data['email']}')
database = User()
database.adc_user('Athos', 'athosbds@gmail.com')
database.list_users()