#Crie um sistema de gerenciamento de times de futebol usando Programação Orientada a Objetos (POO) em Python.

class Player():
    def __init__(self, name, football_position, shirt_number):
        self.name = str(name)
        self.football_position = str(football_position)
        self.shirt_number = int(shirt_number)
    def __str__(self):
        return f'{self.name} - {self.football_position} - Camisa {self.shirt_number}'
class Team():
    def __init__(self, name):
        self.name = str(name)
        self.team = []
    def holders(self, player):
        self.team.append(player)
    def show_details(self):
        if not self.team:
            print(f'O time {self.name} não tem jogadores ainda.')
        else:
            for player in self.team:
                print(player)
teams = {}
while True:
    print("""GERENCIAMENTO TIME DE FUTEBOL
1 - Criar Time
2 - Adicionar Jogador
3 - Mostrar Times
4 - Sair""")
    choose = int(input('Opção: '))
    if choose == 1:
        name = str(input('Nome Do Time: '))
        if name not in teams:
            teams[name] = Team(name)
            print('Time criado.')
        else:
            print('Time Existente.')
    elif choose == 2:
        print('ADICIONANDO JOGADOR')
        player_name = str(input('Nome do Jogador'))
        position = str(input('Posição: '))
        shirt_number = int(input('Número Da Camisa: '))
        name_team = input('Time Escolhido: ')
        if name_team in teams:
            player = Player(player_name, position, shirt_number)
            teams[name_team].holders(player)
        else:
            print('Time não Encontrado.')
    elif choose == 3:
        if not teams:
            print('\nNenhum Time Encontrado')
        else:
            for team in teams.values():
                print(f'Time {team.name}')
                team.show_details()
    elif choose == 4:
        break
    else:
        print('Inválido.')
