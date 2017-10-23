import os

def helpp():
    return 'Доступные комманды:\n' \
           'К командам можно обращаться по индексу в списке\n' \
           '1)Вывести текущее местоположение\n' \
           '2)Сменить текущую директорию\n' \
           '3)Вывести список файлов и директорий в дириктории\n' \
           '4)Создать Заметку и быстрый путь к папке в формате: Name-->Path\n' \
           'exit --> выйти из программы'

def path():
    print('Текущая дириктория ')
    return os.getcwd()

def chdir():
    try:
        os.chdir(input('Переход в...'))
        return os.getcwd()
    except FileNotFoundError:
        return 'Неправильный путь, или такой папки не существует'

def listdir():
    return os.listdir()

def Favorite():
    f = open('file.txt', 'r+')
    n =f.read().count('\n')
    f.seek(0,2)
    Name = str(n) + ')' + input('Введите Имя заметки:')
    f.write(Name+'-->'+os.getcwd()+'\n')
    f.close()
    return 'Готово'

List = {'.help':helpp,'1':path,'2':chdir,'3':listdir, '4':Favorite}