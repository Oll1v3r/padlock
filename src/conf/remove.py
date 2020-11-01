from os import path, system
from time import sleep


def removePadlock():

    padlockPath = '/data/data/com.termux/files/usr/lib/python3.9/'
    home = '/data/data/com.termux/files/home/'

    if path.exists(padlockPath+'padlock') == True and path.exists(home+'.bash_login') == True and path.exists(home+'padlock/.log') == True and path.exists(home+'.padlock') == True and path.exists(home+'padlock/.env') == True and path.exists(home+'padlock/src/conf/.env') == True and path.exists(home+'padlock/src/conf/.log') == True:
        print('[+] Desfazendo configuração do sistema')
        " Remover as configuraçôes do padlock "
        system('rm -rf {}padlock/'.format(padlockPath))
        system('rm {}.bash_login'.format(home))
        system('rm {}padlock/.log'.format(home))
        system('rm {}.padlock'.format(home))
        system('rm {}padlock/.env'.format(home))
        system('rm {}padlock/src/conf/.env'.format(home))
        system('rm {}padlock/src/conf/.log'.format(home))

        sleep(1)
        
        " Verificar se as configuraçôes foram removidas com sucesso "
        if path.exists(padlockPath+'padlock') == False and path.exists(home+'.bash_login') == False and path.exists(home+'padlock/.log') == False and path.exists(home+'.padlock') == False and path.exists(home+'padlock/.env') == False and path.exists(home+'padlock/src/conf/.env') == False and path.exists(home+'padlock/src/conf/.log') == False:

            system("sed -i '$s/run/#run/g' src/conf/verify.py")
            print('[+] Configuração removida com sucesso')
            sleep(1)
        else:
            print('[!] Ops, algo de errado aconteceu')
            exit()

    else:
        print('[!] Configuração ja foi removida recentemente')
        exit(0)

