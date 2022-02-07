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