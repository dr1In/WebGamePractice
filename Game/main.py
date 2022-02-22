from os import system
import items_for_client

SERVER_IP = '172.20.10.3'
SERVER_URL = f'http://{SERVER_IP}:5000/'



def lobby_waiting(username):
    (cur_state_ready, phrase) = (False, '')
    system('CLS')
    while items_for_client.Lobby_show(username):
        print('enter - для обновления')
        if not cur_state_ready:
            phrase = items_for_client.Lobby_coms(input(f'{username}: '))
        print(phrase)


def game_process(user, g_id):
    items_for_client.game_connect(user, g_id)
    while items_for_client.game_status() == 'Running':
        while True:
            system('CLS')
            items_for_client.info()
            match input(f'{user}: '):
                case '1':
                    items_for_client.buy_raw()
                case '2':
                    pass
                case '3':
                    pass
                case '4':
                    pass
                case '5':
                    pass


        
        
def main():
    username = input('Как вас зовут: ')
    system('CLS')

    print('Приветсвуем в игре', username)
    print('Посмотреть лобби - 1')
    print('Создать лобби - 2' + '\n')

    if input(f'{username}: ')  == '2':
        system('CLS')
        game_id = items_for_client.Lobby_creation(username)
        lobby_waiting(username)
    else:
        system('CLS')
        game_id = items_for_client.Lobby_connection(username)
        lobby_waiting(username)
    
    game_process(username, game_id)




if __name__ == '__main__':
    main()
