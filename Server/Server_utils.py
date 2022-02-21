from math import floor

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
    def __init__(self, game_id: str(), duration: str(), max_pl: str()):
        self.players = dict()
        self.max_players = max_pl
        self.P = int(self.max_players)
        self.id = game_id
        self.dur = duration
        self.market_lvl = 3
        self.market = update_market(self.market_lvl, self.P)
        self.ip_to_name = dict()
        self.game_status = 'Running'

    def connect(self, user: str(), ip_addr: str()):
        self.players[user] = {
            'currency': 10000,
            'material': 4,
            'planes': 2,
            'buildings': 2,
            'status': 0,
            'build_process': '-',
            'BR': None
        }
        self.ip_to_name[ip_addr] = user

    def collect_info(self):
        return update_market(self.market_lvl, self.P)

    def collect_player_info(self, ip):
        return self.players[self.ip_to_name[ip]]

    def update_player_BR(self, ip, BR):
        user = self.ip_to_name[ip]
        if BR[0] > 0 and BR[0] <= self.market['material_quantity'] and BR[-1] >= self.market['material_cost'] and BR[-1] <= self.players[user]['currency']:
            self.players[user]['BR'] = BR
            return 'ok'
        else: return 'error'

    def get_game_status(self):
        return self.game_status


def update_market(lvl, P):
    markets = {
            1: {
                'material_cost': 800,
                'material_quantity': P * 1,
                'plane_cost': 6500,
                'plane_quantity': P * 3,
            },
            2: {
                'material_cost': 650,
                'material_quantity': floor(P * 1.5),
                'plane_cost': 6000,
                'plane_quantity': floor(P * 2.5),
            },
            3: {
                'material_cost': 500,
                'material_quantity': P * 2,
                'plane_cost': 5500,
                'plane_quantity': P * 2,
            },
            4: {
                'material_cost': 400,
                'material_quantity': floor(P * 2.5),
                'plane_cost': 5000,
                'plane_quantity': floor(P * 1.5),
            },
            5: {
                'material_cost': 300,
                'material_quantity': P * 3,
                'plane_cost': 4500,
                'plane_quantity': P * 1,
            }
        }
    return markets[lvl]

def market_change():
    market = {
        1: [1,1,1,1,2,2,2,2,3,3,4,5],
        2: [1,1,1,2,2,2,2,3,3,3,4,5],
        3: [1,2,2,2,3,3,3,3,4,4,4,5],
        4: [1,2,3,3,3,4,4,4,4,5,5,5],
        5: [1,2,3,3,4,4,4,4,5,5,5,5]
    }