class Lobby():
    def __init__(self, lobby_name: str(), max_players: int(), duration: str()):
        self.name = lobby_name
        self.players_status = {}
        self.players_ip_to_name = {}
        self.max = max_players
        self.duration = duration


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

    def get_dur(self):
        if int(self.duration) == 0:
            return f'без огр.'
        else:
            return f'огр. в {self.duration}'

class Game:
    def __init__(self):
        self.players = list()