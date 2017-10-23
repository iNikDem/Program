# -*- coding: utf-8 -*-
from os import getcwd,mkdir,remove
from YaDiskClient.YaDiskClient import YaDisk
import time

def Auth_user():
    try:
        f = open(getcwd()+'/Info/file.txt', 'r+')
    except FileNotFoundError:
        mkdir(getcwd()+'/Info')
        f = open(getcwd()+'/Info/file.txt', 'w+')
        login = input('Информация о пользователе не найдена\n'
                      'Авторизация Нового Пользователя\n'
                      'Login:')+'\n'
        password = input('Password:')
        f.write(login)
        f.write(password)
    f.seek(0)
    path = getcwd()+'/Info/Users.txt'
    disk = YaDisk(input('Ya_Login:'), input('Ya_Password:'))
    disk.download('Logs/Users.txt',path)
    g = open(path,'r')
    s = g.read()
    g.close()
    if s!=(login+'\n'+password):
        print('Такого пользователя в базе данных нет, exit')
        exit()
    #remove(path)
    print('\nВыполняется вход...\n')
    time.sleep(1)
    user_login =  f.readline().replace('Login:','')
    print('Добро пожаловать ', user_login)
    print('Для справки пропишите .help\n'
          'Для выхода из программы, используйте exit')
    f.close()
    return user_login,disk