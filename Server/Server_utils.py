class Lobby():
    def __init__(self, size: int(), host_ip_addr: str(), name: str()):
        self.name = name
        self.host = host_ip_addr
        self.size = size
        self.players = dict()


    def connect(self, name: str(), ip: str()):
        self.players[name] = ip

    def get_players_names(self):
        return 1
