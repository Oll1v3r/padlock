import time
import argparse
import os

from src.conf.remove import *
from src import conf
from src.conf.verifyTest import *
from src.conf.setup import *

parser = argparse.ArgumentParser(description='Sistema de login para linux')

parser.add_argument('--test', action='store_true', help='Testa o sistema sem aplicar configuraçôes ao sistema')
parser.add_argument('--setup', '-s', metavar='distro' ,help='Aplica configuração a um sistema operacional linux definido')
parser.add_argument('--undo', '-u', metavar='distro',help='Desfaz as configuraçôes aplicadas anteriormente a uma distribuição definida')

args = parser.parse_args()

#print(args)

distros = ['termux', 'ubuntu']


" test "
if args.test:
    def firstUser():
        global userTest
        userTest = input('User Name de teste : ')
        while userTest == '':
            print('[!] Insira um user qualquer')
            firstUser()
        else:
            def firstPass():
                global passTest
                passTest = input('Pass Word de teste : ')
                while passTest == '':
                    print('[!] Insira um pass qualquer')
                    firstPass()
                else:
                    " Chamar a função de teste "
                    verifyTest(userTest, passTest)

            firstPass()
    firstUser()

" setup "
if args.setup:
    if args.setup not in distros:
        print('[+] Configurando ')
        time.sleep(1)
        print('[!] Não está disponível configuração para este sistema')
        exit(0)
    elif args.setup in distros:
        if args.setup == 'termux':
            print('[+] Configurando para {}'.format(args.setup))
            time.sleep(1)
            checkConf()
            setup()
            exit(0)
        elif args.setup == 'ubuntu':
            print('[+] Configurando para derivado')
            time.sleep(1)
            print('[!] Derivados em breve')
            exit(0)

" undo "
if args.undo:
    if args.undo not in distros:
        print('[+] Desfazendo configuração')
        time.sleep(1)
        print('[!] Não está disponível remoção para este sistema')
        exit(0)
    elif args.undo in distros:
        if args.undo == 'termux':
            " Chamar função de remoção "
            removePadlock()
        elif args.undo == 'ubuntu':
            print('[+] Defazendo configuração para derivado')
            time.sleep(1)
            print('[!] Derivados em breve')
            exit(0)

else:
    os.system('figlet -f src/padlock/Remo773.flf Padlock')
    print("""
About auhtor:

CodeName    : Padlock https://github.com/Oll1v3r/padlock
Author      : Oliver
Website     : https://tecnospeed.000webhostapp.com
Version     : 2.0

Social Network:

Fanpage      : https://www.facebook.com/oliveobom
Instagram   : https://www.instagram.com/laboratoriohacker
Group t.m   : https://t.me/joinchat/O7iNwhsiTssYrN5NoNtHTw

Contribe:

Author font : https://github.com/remo7777

[!] erro de execução, tente -h/--help para saber mais detalhes sobre padlock""")
    exit(0)


