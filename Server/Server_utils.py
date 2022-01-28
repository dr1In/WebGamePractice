class Lobby():
    def __init__(self, lobby_name: str(), max_players: int()):
        self.name = lobby_name
        self.players_status = {}
        self.players_ip_to_name = {}
        self.max = max_players

    def connect(self, user: str(), user_addr: str()):
        if len(self.players_ip_to_name) < int(self.max):
            self.players_ip_to_name[user_addr] = user
            self.players_status[user] = 'Not ready'
            return True
        else:
            return False

    def get_players_status(self):
        return self.players_status

    def get_emptiness(self):
        return f'{len(self.players_status)}/{self.max}'
    
    def get_max(self):
        return f'{self.max}'

    def player_ready(self, ip: str()):
        self.players_status[self.players_ip_to_name[ip]] = 'Ready'


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