from os import system
import items_for_client

SERVER_IP = '192.168.0.18'
SERVER_URL = f'http://{SERVER_IP}:5000/'





def lobby_waiting(username):
    (cur_state_ready, phrase) = (False, '')
    system('CLS')
    while items_for_client.Lobby_show(username):
        if not cur_state_ready:
            phrase = items_for_client.Lobby_coms(input(f'{username}: '))
        print(phrase)


        
        
def main():
    username = input('Как вас зовут: ')

    print('Приветсвуем в игре', username)
    print('Посмотреть лобби - 1')
    print('Создать лобби - 2' + '\n')

    if input(f'{username}: ')  == '2':
        system('CLS')
        items_for_client.Lobby_creation(username)
        lobby_waiting(username)
    else:
        system('CLS')
        items_for_client.Lobby_connection(username)
        lobby_waiting(username)




if __name__ == '__main__':
    main()
