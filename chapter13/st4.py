# 运行时弹出密码输入提示
import getpass


def svc_login(user, passwd):
    passwd

user = getpass.getuser()
user = input('Enter your username:')
passwd = getpass.getpass()

if svc_login(user, passwd):
    print('Yay!')
else:
    print('Boo!')