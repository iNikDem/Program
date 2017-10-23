from os import getcwd
from YaDiskClient.YaDiskClient import YaDisk
def Auth():
    disk = YaDisk(input('Login:'), input('Password:'))
    f = open(os.getcwd()+'\Info\disk.txt','w')
    s = 'disk:'+str(disk)
    f.write(s)
    f.close()
    return 'OK'