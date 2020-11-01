#!/usr/bin/env pyhon3
# Describe: Cadastra utilizador
# Version: 2.0
# License: MIT License
# Author: Oliver

from os import system, path, getenv
from time import sleep, localtime
import dotenv

dotenv.load_dotenv()

username = getenv('username')
password = getenv('password')

date = localtime()

def checkConf():

    " Verificar se existe dados de cadastro"
    NewFile = '.log'
    if(path.exists(NewFile) == True):
        print('[+] Há uma configuração registrada no momento')
        exit()

    "setup()"

def setup():

    print("""\033[0m
        █▀▀ █▀▀ ▀▀█▀▀ █░░█ █▀▀█
        ▀▀█ █▀▀ ░░█░░ █░░█ █░░█
        ▀▀▀ ▀▀▀ ░░▀░░ ░▀▀▀ █▀▀▀

        \033[01;92mName\033[0m: \033[02;94m(\033[01;93msetup\033[02;94m)\033[0m, \033[01;92mVersion\033[0m: \033[02;94m(\033[01;93mv2.0\033[02;94m)
        \033[01;92mBy\033[0m: \033[02;94m(\033[01;93mOlive\033[02;94m)\033[0m, \033[01;92mFont by\033[0m: \033[02;94m(\033[02;93mRemo7777\033[02;94m)

        \033[0m""")

    firstUser()

" firstUser "
def firstUser():
    global firtsUsername
    firstUsername = input('Enter a NEW User : ')
    while firstUsername == '':
        print('Input user required!')
        firstUser()
    else:
        def lastUser():
            global lastUsername
            lastUsername = input('Re-enter the NEW user: ')
            while lastUsername == '':
                print('Input user required!')
                lastUser()
            else:
                while firstUsername != lastUsername:
                    print("'Data doesn't match, try again!'")
                    firstUser()
                else:
                    " Verificar se a quantidade de caracteres do utilizador ultrapassar de 28 caracteres OU a tiver uma quantidade menor que 8 caracteres "
                    while len(lastUsername) > 28 or len(lastUsername) < 4:
                        print('Minimum number of characters is: 8, Maximum number of characters is: 28')
                        firstUser()
                    else:
                        pass
    
                    " fisrtPass "
                    firstPass()

        lastUser()
" firtPass "
def firstPass():
    global firstPassword
    firstPassword = input('Enter a NEW password: ')
    while firstPassword == '':
        print('Input pass required!')
        firstPass()
    else:
        def lastPass():
            global lastPassword
            lastPassword = input('Re-enter the NEW password : ')
            while lastPassword == '':
                print('Input pass required!')
                lastPass()
            else:
                while firstPassword != lastPassword:
                    print("Data doesn't 'match try again!'")
                    firstPass()
                else:
                    while len(lastPassword) > 28 or len(lastPassword) < 4:
                        " Verificar se a quantidade de caracteres do passe ultrapassar de 28 caracteres OU a tiver uma quantidade menor que 8 caracteres "
                        print('Minimum number of characters is: 8, Maximum number of characters is: 28')
                        firstPass()
                    else:
                        pass
                    writerData(lastUsername, lastPassword)
        lastPass()

def writerData(username, password):
    system('clear')
    system('tput civis')

    print('\033[0m')
    _File = '.env'
    with open(_File, 'w') as envFile, open('.log', 'w') as logFile:
        " Escrever dados cadastrado "
        envFile.write("username='{}'\n".format(username))
        envFile.write("password='{}'".format(password))

        " Registrar arquivo .log "
        logFile.write("let's go")

        " Adicionar diretorio do padlock em /usr/lib/python3.9 "
        padlockPath = '/data/data/com.termux/files/usr/lib/python3.9'
        home = '/data/data/com.termux/files/home/'

        system('tput cup 0')
        print('\r\033[0mCopying padlock directory to /lib/python3.9/padlock [\033[01;93mNone\033[0m]')
        sleep(1)
        system('cp {}/padlock/ {} -rf'.format(home, padlockPath))
        " Verificar se criou com sucesso "
        if (path.exists(padlockPath+'/padlock') == True):
            system('tput cup 0')
            print('\r\033[0mCopying padlock directory to /lib/python3.9/padlock [\033[01;92mDone\033[0m]')
            sleep(1)
        elif (path.exists(padlockPath+'/padlock') == False):
            system('tput cup 0')
            print('\r\033[0mCopying padlock directory to /lib/python3.9/padlock [\033[01;91mFailed\033[0m]')
            sleep(1)
            " Senao, excluir o log "
            system('rm .log')

    
    "Configurar acesso do painel admin na inicialização"

    if (path.exists(home+'.bash_login') == True and path.exists(home+'.padlock') == True):

        """
        Se os arquivos '.bash_login' e '.padlock' existirem
        Abra o arquivo '.bash_login e escreve:

        'bash $HOME/.padlock' :

        Abra o arquivo '.padlock' e escreve:

        O arquivo '.padlock' será
        executado na inicialização do sistema linux

        """
        with open(home+'.bash_login', 'w') as lineBashlogin, open(home+'.padlock', 'w') as linePadlock:
            """
            Escreve no arquivo '.bash_login' o comando:

            'bash $HOME/.padlock'

            """
            lineBashlogin.write('bash $HOME/.padlock')
            """
            Escreve no arquivo '.padlock' o comando:

            cd $HOME && cd padlock && cd src && cd conf && python3 verify.py

            """
            linePadlock.write('cd $HOME && cd padlock && cd src && cd conf && python3 verify.py')
    else:
        """
        Se os arquivos '.bash_login' e '.padlock' não existirem
        Abra o arquivo '.bash_login e escreve:

        'bash $HOME/.padlock' :

        Abra o arquivo '.padlock' e escreve:

        cd $HOME && cd padlock && cd src && cd conf && python3 verify.py

        O arquivo '.padlock' será
        executado na inicialização do sistema linux

        """
        with open(home+'.bash_login', 'w') as lineBashlogin, open(home+'.padlock', 'w') as linePadlock:
            """
            Escreve no arquivo '.bash_login' o comando:

            'bash $HOME/.padlock'

            """
            lineBashlogin.write('bash $HOME/.padlock')
            """
            Escreve no arquivo '.padlock' o comando:

            cd $HOME && cd padlock && cd src && cd conf && python3 verify.py

            """
            linePadlock.write('cd $HOME && cd padlock && cd src && cd conf && python3 verify.py')

    

        " Verificar se o acesso a memoria foi permitido "
        if path.exists(home+'storage/') == True:
            " Escrever 'registro.txt' "
            system('tput cup 1')
            print("\r\033[0mCreating file 'registro.txt' in /sdcard/ [\033[01;93mNone\033[0m]")
            sleep(1)
            with open(home+'storage/shared/registro.txt', 'w') as log:
                log.write('User Name : {}\nPass Word : {}\n\nRegistered at: {}/{}/{} - PT {}:{} - {}\n'.format(username, password, date[2], date[1], date[0], date[3], date[4], date[5]))

            if path.exists(home+'storage/shared/registro.txt') == True:
                system('tput cup 1')
                print("\r\033[0mCreating file 'registro.txt' in /sdcard/ [\033[01;92mDone\033[0m]")
                sleep(1)

            elif path.exists(home+'storage/shared/registro.txt') == False:
                system('tput cup 1')
                print("\rCreating file 'registro.txt' in /sdcard/ [\033[01;91mFailed\033[0m]")
                sleep(1)
            else:
                print('Something went wrong')
                exit(1)

        elif path.exists(home+'storage/') == False:
            print('Allow access to internal memory')
            sleep(1)
            system('termux-setup-storage')
            " Escrever 'registro.txt' "
            system('tput cup 1')
            print("/rCriando arquivo 'registro.txt' em /sdcard/ [None]")
            sleep(1)
            with open(home+'storage/shared/registro.txt', 'w') as log:
                log.write('User Name : {}\nPass Word : {}\n\nRegistered at: {}/{}/{} - PT {}:{} - {}\n'.format(username, password, date[2], date[1], date[0], date[3], date[4], date[5]))

            " Verificar se foi  criado "
            if path.exists(home+'storage/shared/registro.txt') == True:
                system('tput cup 1')
                print("\rCriando arquivo 'registro.txt' em /sdcard/ [Done]")
                sleep(1)
            elif path.exists(home+'storage/shared/registro.txt') == False:
                system('tput cup 1')
                print("\rCriando arquivo 'registro.txt' em /sdcard/ [Failed]")
                sleep(1)
            else:
                print('Something went wrong')
                exit(0)


        else:
            print('Something went wrong')
            exit(1)

    system('cp {}padlock/.env {}padlock/src/conf'.format(home, home))
    system('cp {}padlock/.log {}padlock/src/conf'.format(home, home))
    system("sed -i '$s/#verify/verify/g' src/conf/verify.py")
    system('tput cnorm')

    system('tput cup 3')
    print('\033[0mYour data to log into the system:\n\n')
    print('User Name : \033[01;92m{}\033[0m'.format(username))
    print('Pass Word : \033[01;92m{}\033[0m'.format(password))

    print('\n')
    
    print('\033[01;92mRegistered at\033[0m: {}/{}/{} PT hour {}:{} - {}'.format(date[2], date[1], date[0], date[3], date[4], date[5]))

    print('\nWhich insects or problems to the application, report the problem in https://t.me/theolliver')
    exit()

