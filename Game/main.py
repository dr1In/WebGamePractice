from os import system
import items_for_client

SERVER_IP = '127.0.0.1'
SERVER_URL = f'http://{SERVER_IP}:5000/'
USERNAME = input('Как вас зовут: ')




def lobby_waiting():
    (cur_state_ready, phrase) = (False, '')
    system('CLS')
    while items_for_client.Lobby_show(USERNAME):
        if not cur_state_ready:
            phrase = items_for_client.Lobby_coms(input(f'{USERNAME}: '))
        print(phrase)


        
        
def main():
    

    print('Приветсвуем в игре', USERNAME)
    print('Посмотреть лобби - 1')
    print('Создать лобби - 2' + '\n')

    if input(f'{USERNAME}: ')  == '2':
        system('CLS')
        items_for_client.Lobby_creation(USERNAME)
        lobby_waiting()
    else:
        system('CLS')
        items_for_client.Lobby_connection(USERNAME)
        lobby_waiting()




if __name__ == '__main__':
    main()
