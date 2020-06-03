from os import system, path
from time import sleep

def painel_1():

    system('clear')
    print(
        '''
    {0}\n
    AQUI FICA O LOGO OU BANNER
    
    \033[00;93mUsername\033[0m:\033[00;92m

    \033[00;93mPassword\033[0m:\033[00;92m

    \033[00;92m(\033[00;91m{1}\033[00;92m)


    {2}'''.format('_'*30, message, '_'*30))

def painel_2():
    system('clear')
    print(                                                              '''
    {0}\n
    AQUI FICA O LOGO OU BANNER

    \033[00;93mUsername\033[0m: \033[00;92m{1}
                                                               \033[00;93mPassword\033[0m: \033[00;92m
                                                               \033[00;92m(\033[00;91m{2}\033[00;92m)


    {3}\n
        '''.format('_'*30, username_login, message, '_'*30))


tamanhoU = 'tput cup 5 14'
tamanhoP = 'tput cup 7 14 && tput cnorm'

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
        cursor_end = 'tput cup 14'
        system('{0}'.format(cursor_end))
        print('\r    Loading... {0}'.format(step))
        sleep(0.2)

    visivel = 'tput cnorm'
    system(visivel)
    print('')

def login():
    if(path.exists('.data-test.txt') == True):
        open_file = open('.data-test.txt', 'r')
        open_file = list(open_file)

        global message
        message = 'Acess Denied'
        painel_1()
        posicaoU()
        global username_login
        username_login = input()

        while(username_login+'\n' != open_file[0]):
            posicaoErro = 'tput cup 11 && tput civis'
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
                password_login = input()

                while(password_login+'\n' != open_file[1]):
                    posicaoErro = 'tput cup 11 && tput civis'
                    system(posicaoErro)
                    print('    Password inválid, try other')
                    sleep(1)
                    login_pass()
                else:
                    message = 'Acess sucessfuly'
                    loading_login()
                    exit()
            login_pass()
login()
