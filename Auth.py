import time

def Auth_user():
    try:
        f = open('file.txt', 'r+')
    except FileNotFoundError:
        f = open('file.txt', 'w+')
        s = 'Login: ' + input('Информация о пользователе не найдена\n'
                              'Авторизация Нового Пользователя\n'
                              'Введите свой логин:')+'\n'
        f.write(s)
    f.seek(0)
    print('\nВыполняется вход...\n')
    time.sleep(1)
    user_login =  f.readline().replace('Login: ','')
    print('Добро пожаловать ', user_login)
    print('Для справки пропишите .help\nДля выхода из программы, используйте exit')
    f.close()
    return user_login