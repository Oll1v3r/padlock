from os import system, path
from time import sleep
import banners

def painel_1():
    system('clear')
    print('''
    \033[0m{0}
    \033[01;92m{1}

    \033[00;93mUsername\033[0m:\033[00;92m

    \033[00;93mPassword\033[0m:\033[00;92m

    \033[00;92m(\033[00;91m{2}\033[00;92m)\033[0m


    {3}\033[0m'''.format('_'*42, banners.logo[0], message, '_'*42))

def painel_2():
    system('clear')
    print('''
    \033[0m{0}
    \033[01;92m{1}

    \033[00;93mUsername\033[0m: \033[00;92m{2}

    \033[00;93mPassword\033[0m: \033[00;92m

    \033[00;92m(\033[00;91m{3}\033[00;92m)\033[0m


    {4}\n\033[0m'''.format('_'*42, banners.logo[0], username_login, message, '_'*42))


tamanhoU = 'tput cup 10 14'
tamanhoP = 'tput cup 12 14 && tput cnorm'

def posicaoU():
    system('{0}'.format(tamanhoU))
    visivel = 'tput cnorm'
    system('{}'.format(visivel))

def posicaoP():
    system('{0}'.format(tamanhoP))

def loading_login():
    steps = ['[□□□□□□]','[■□□□□□]','[□■□□□□]','[□□■□□□]','[□□□■□□]','[□□□□■□]','[□□□□□■]','[■□□□□□]','[□■□□□□]','[□□■□□□]','[□□□■□□]','[□□□□■□]','[□□□□□■]','[ Done ]']
    for step in steps:
        tamanhoCursor = 'tput civis'
        system('%s' % (tamanhoCursor))
        cursor_end = 'tput cup 21'
        system('{0}'.format(cursor_end))
        print('\r    Loading... {0}'.format(step))
        sleep(0.2)

    posicaoErro = 'tput cup 14 5 && tput civis'
    system(posicaoErro)
    message = "Acess Sucess"
    print(message)
    visivel = 'tput cnorm'
    system(visivel)
    print('')

def login():
    if(path.exists('/data/data/com.termux/files/home/Sign-Ultimate/config/login/.login.txt') == True):
        open_file = open('/data/data/com.termux/files/home/Sign-Ultimate/config/login/.login.txt', 'r')
        open_file = list(open_file)

        global message
        message = 'Acess denied'
        painel_1()
        posicaoU()
        global username_login
        username_login = input("\033[00;92m")

        while(username_login+'\n' != open_file[0]):
            posicaoErro = 'tput cup 16 && tput civis'
            system(posicaoErro)
            print('    Username inválid, try other')
            sleep(1.5)
            login()
        else:
            def login_pass():
                system('clear')

                painel_2()
                posicaoP()
                global password_login
                password_login = input("\033[00;92m")

                while(password_login+'\n' != open_file[1]):
                    posicaoErro = 'tput cup 16 && tput civis'
                    system(posicaoErro)
                    print('    Password inválid, try other')
                    sleep(1)
                    login_pass()
                else:
                    loading_login()
                    posicaoErro = 'tput cup 25 && tput cnorm'
                    system(posicaoErro)
                    exit()
            login_pass()
def kill():
    cursor_end = 'tput cup 21'
    system(cursor_end)
    print("Encerrando e saindo...")
    sleep(1)
    system("bash job.sh")

try:
    login()
except KeyboardInterrupt:
    kill()
except EOFError:
    kill()
