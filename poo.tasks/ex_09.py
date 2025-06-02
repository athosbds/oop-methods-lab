# Crie um sistema de RPG com classes Jogador e Missao, usando listas e dicionários para aceitar e concluir missões.

class Quest():
    def __init__(self, title, about, reward):
        self.title = str(title)
        self.about = str(about)
        self.reward = float(reward)
    def quest_show(self):
        return {
            'título': self.title,
            'sobre': self.about,
            'reward': self.reward
        }
class Player():
    def __init__(self, name , gold=0.0):
        self.name = str(name)
        self.quests = []
        self.gold = float(gold)
    def accept_quest(self, quest):
        for querue in self.quests:
            if querue['título'] == quest.title:
                print(f'Missão {querue.title} já aceita')
                return
        self.quests.append(quest.quests.quest.show())
    def show_quests(self):
        if not self.quests:
            print(f'Não tem missões ativas')
        else:
            print(f'Missões ativas de {self.name}')
            for quest in self.quests:
                print(f'{quest['título']} - {quest['sobre']} - {quest['reward']}')
    def status(self):
        print(f'Jogador: {self.name}')
        print(f'Ouro: {self.gold}')
        self.show_quests()
    def finish_quest(self, title_quest):
        for quest in self.quests:
            if quest['título'] == title_quest:
                self.quests.remove(quest)
                self.gold += quest['reward']
                print(f'{self.name} concluiu a missão e recebeu a recompensa.')
