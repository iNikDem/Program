import time
import Commands
import Auth

user_login = Auth.Auth_user()
while True:
    string = input()
    if string == 'exit':
        print('Досвидания ',user_login)
        time.sleep(1)
        exit()
    try:
        print(Commands.List[string]())
    except KeyError:
        print('Комманда не найдена')
    time.sleep(1)
