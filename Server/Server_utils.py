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
        self.dur = int(duration)
        self.market_lvl = 3
        self.ip_to_name = dict()
        self.game_status = 'Running'
        self.players_ready = 0

    def connect(self, user: str(), ip_addr: str()):
        self.players[user] = {
            'currency': 10000,
            'material': 4,
            'planes': 2,
            'all_buildings': 2,
            'active_buildings': 0,
            'status': 'NR',
            'build_process': '-',
            'BR': None,
            'SP': None,
            'will_done': 0
        }
        self.ip_to_name[ip_addr] = user

    def collect_info(self):
        return update_market(self.market_lvl, self.P)

    def collect_player_info(self, ip):
        return self.players[self.ip_to_name[ip]]

    def update_player_BR(self, ip, BR):
        market = update_market(self.market_lvl, self.P)
        user = self.ip_to_name[ip]
        if BR[0] > 0 and BR[0] <= market['material_quantity'] and BR[-1] >= market['material_cost'] and BR[-1] * BR[0] <= self.players[user]['currency']:
            self.players[user]['BR'] = BR
            return 'ok'
        else: return 'error'

    def update_player_SP(self, ip, SP):
        market = update_market(self.market_lvl, self.P)
        user = self.ip_to_name[ip]
        if SP[0] > 0 and SP[0] <= market['plane_quantity'] and SP[-1] <= market['plane_cost'] and SP[0] <= self.players[user]['planes']:
            self.players[user]['SP'] = SP
            return 'ok'
        else: return 'error'

    def get_game_status(self):
        return self.game_status
    
    def produce_plane(self, ip, q):
        user = self.ip_to_name[ip]
        if q >= 0 and q <= self.players[user]['material'] and q * 2000 <= self.players[user]['currency'] and self.players[user]['active_buildings'] + q <= self.players[user]['all_buildings']:
            self.players[user]['material'] -= q
            self.players[user]['currency'] -= q * 2000
            self.players[user]['will_done'] += q
            self.players[user]['active_buildings'] += q
            return 'ok'
        else: return 'error'

    def build(self, ip, ask):
        user = self.ip_to_name[ip]
        if ask == 'N': return 'ok'
        elif ask == 'Y':
            self.players[user]['build_process'] = 4
            self.players[user]['currency'] -= 2500
            return 'ok'
        else: return 'error'

    def player_status(self, ip):
        user = self.ip_to_name[ip]
        return self.players[user]['status']

    def change_player_status(self, ip):
        user = self.ip_to_name[ip]
        self.players[user]['status'] = 'R'
        self.players_ready += 1
        if self.players_ready == self.P:
            self.update_month()

    def update_month(self):
        (market_buy, market_sell) = (dict(), dict())
        for user in self.players:
            if self.players[user]['BR'] is not None and self.players[user]['BR'] != 'B':
                market_buy[user] = self.players[user]['BR']
            if self.players[user]['SP'] is not None and self.players[user]['BR'] != 'B':
                market_sell[user] = self.players[user]['SP']
        result = buing(update_market(self.market_lvl, self.P), market_buy)
        for user in result.keys():
            self.players[user]['material'] += result[user][0]
            self.players[user]['currency'] -= result[user][0] * result[user][-1]
        result2 = selling(update_market(self.market_lvl, self.P), market_sell)
        for user in result2.keys():
            self.players[user]['currency'] += result2[user][0] * result2[user][-1]
            self.players[user]['planes'] -= result2[user][0]
        for player in self.players.keys():
            if self.players[user]['BR'] == 'B': continue
            money = self.players[player]['all_buildings'] * 1000 + self.players[player]['planes'] * 500 + self.players[player]['material'] * 300
            self.players[player]['currency'] -= money
            self.players[player]['planes'] += self.players[player]['will_done']
            self.players[player]['will_done'] = 0
            self.players[player]['active_buildings'] = 0
            self.players[player]['BR'] = None
            self.players[player]['SP'] = None
            self.players[player]['status'] = 'NR'
            if self.players[player]['build_process'] != '-':
                self.players[player]['build_process'] -= 1
            if self.players[player]['build_process'] == 0:
                self.players[player]['build_process'] = '-'
                self.players[player]['all_buildings'] += 1
                self.players[player]['currency'] -= 2500
            if self.players[player]['currency'] <= 0:
                self.P -= 1
                self.players[player]['status'] = 'B'
        if self.P == 0:
            self.game_status = 'End'   



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


def buing(market, asks):
    quantity = market['material_quantity']
    asks = sorted(asks.items(), key=lambda x: x[-1][-1], reverse=True)
    asks = {k: v for k, v in asks}
    temp = dict()
    for user in asks.keys():
        if quantity > 0:
            if quantity > asks[user][0]:
                temp[user] = asks[user]
                quantity -= asks[user][0]
            elif asks[user][0] > quantity:
                temp[user] = asks[user]
                temp[user][0] = quantity
                break
        else: break
    return temp


def selling(market, asks):
    quantity = market['material_quantity']
    asks = sorted(asks.items(), key=lambda x: x[-1][-1])
    asks = {k: v for k, v in asks}
    temp = dict()
    for user in asks.keys():
        if quantity > 0:
            if quantity > asks[user][0]:
                temp[user] = asks[user]
                quantity -= asks[user][0]
            elif asks[user][0] > quantity:
                temp[user] = asks[user]
                temp[user][0] = quantity
                break
        else: break
    return temp
