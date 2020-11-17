#!/usr/bin/env python3
# Describe: Desfaz configuração aplicada
# License: MIT License
# Version: 2.1
# Author: Oliver

from os import path, system
from time import sleep
from shutil import rmtree
from os import remove

def removePadlock():
    padlockPath = '/data/data/com.termux/files/usr/lib/python3.9/'
    home = '/data/data/com.termux/files/home/'
    if path.exists(padlockPath+'padlock') == True and path.exists(home+'.bash_login') == True and path.exists(home+'padlock/.log') == True and path.exists(home+'.padlock') == True and path.exists(home+'padlock/.env') == True and path.exists(home+'padlock/src/conf/.env') == True and path.exists(home+'padlock/src/conf/.log') == True:
        print('[+] Desfazendo configuração do sistema')
        " Remover as configuraçôes do padlock "
        rmtree('{}padlock/'.format(padlockPath))
        remove('{}.bash_login'.format(home))
        remove('{}padlock/.log'.format(home))
        remove('{}.padlock'.format(home))
        remove('{}padlock/.env'.format(home))
        remove('{}padlock/src/conf/.env'.format(home))
        remove('{}padlock/src/conf/.log'.format(home))
        sleep(1) 
        " Verificar se as configuraçôes foram removidas com sucesso "
        if path.exists(padlockPath+'padlock') == False and path.exists(home+'.bash_login') == False and path.exists(home+'padlock/.log') == False and path.exists(home+'.padlock') == False and path.exists(home+'padlock/.env') == False and path.exists(home+'padlock/src/conf/.env') == False and path.exists(home+'padlock/src/conf/.log') == False:
            print('[+] Configuração removida com sucesso')
            sleep(1)
            exit(0)
        else:
            print('[!] Ops, algo de errado aconteceu')
            exit()
    else:
        print('[!] Configuração ja foi removida recentemente')
        exit(0)
