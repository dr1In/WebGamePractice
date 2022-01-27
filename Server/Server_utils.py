class Game:
    def __init__(self):
        self.players = list()

    def connection(self, pl):
        if len(self.players) < 8:
            self.players.append(pl)
            return 'Вы подключились'
        else: return 'Игра переполненна ожидайте'


class Player:
    def __init__(self, name: str()):
        self.player_name = name
        self.money = 0
        self.workshop = 0
        self.material = 0
        self.planes = 0
        self.ready_to_play = False

    
    def default_setter(self):
        self.money = 10000
        self.planes = 2
        self.workshop = 2
        self.material = 4