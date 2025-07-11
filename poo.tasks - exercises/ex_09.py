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
        for q in self.quests:
            if q['título'] == quest.title:
                print(f'Missão {quest.title} já aceita')
                return
        self.quests.append(quest.quest_show())
    def show_quests(self):
        if not self.quests:
            print(f'Não tem missões ativas')
        else:
            print(f'Missões ativas de {self.name}')
            for quest in self.quests:
                print(f"{quest['título']} - {quest['sobre']} - {quest['reward']}")
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

first_quest = Quest('Matar 4 Lobos', 'Mate 4 lobos e ganhe 5 ouros', 5)

athos_player = Player('Athos', 0)
athos_player.accept_quest(first_quest)
athos_player.show_quests()
athos_player.finish_quest('Matar 4 Lobos')
athos_player.status()
