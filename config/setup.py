#!/data/data/com.termux/files/usr/bin/env python3
# Descricao: 'setup' configure seus dados para login
# Autor: olive

from subprocess import run
from time import sleep
from os import system, path
from colors import dict_colors


# Extraindo cores expecificas do dicionario 'dict_colors' de cores pra fonte e passando para as variaveis 'white, red, green, darkgreen, lightgreen, yellow, darkblue, blue, cyan, lightcyan, darkcyan'

(white, red, green, darkgreen, lightgreen, yellow, darkblue, blue, cyan, lightcyan, darkcyan) = ( \
        \
        dict_colors['coresNormais']['white'], \
        dict_colors['coresNormais']['red'], \
        dict_colors['coresNormais']['green'], \
        dict_colors['coresEscuras']['darkgreen'], \
        dict_colors['coresClaras']['lightgreen'], \
        dict_colors['coresNormais']['yellow'], \
        dict_colors['coresEscuras']['darkblue'], \
        dict_colors['coresNormais']['blue'], \
        dict_colors['coresNormais']['cyan'], \
        dict_colors['coresClaras']['lightcyan'], \
        dict_colors['coresEscuras']['darkcyan'])


def banner():
    print(blue)
    system('toilet -f mono12 SETUP')
    print(blue)
def u():
    global username
    run('clear')
    banner()
    username = str(input('%sDigite um novo usuario %s: %s' % (cyan, lightcyan, darkgreen)))

def U():
    global Username
    Username = str(input('%sDigite novamente o novo usuario %s: %s' % (cyan, lightcyan, darkgreen)))

def p():
    run('clear')
    banner()
    global password
    password = str(input('%sDigite uma nova senha %s: %s' % (cyan, lightcyan, darkgreen)))
    
def P():
    global Password
    Password = str(input('%sDigite novamente a nova senha %s: %s' % (cyan, lightcyan, darkgreen)))
        



def verifica_campos():
    global Username, Password, username, password

    def while01():
        # primeiro loop usuario
        u()
        while username == "" :
            run('clear')
            print("%sCampo de usuario obrigatório %s!" % (red, lightgreen))
            sleep(1)
            while01()
        else:
            while len(username) < 12 :
                run('clear')
                print("%s12 é o MÍNIMO de caractéres %s!" % (red, lightgreen))
                sleep(2)
                while01()

            else:
                while username == "" :
                    run('clear')
                    print("%sCampo de usuario obrigatório %s!" % (red, lightgreen))
                    sleep(1)
                    while01()

                else:
                    while len(username) > 12 :
                        run('clear')
                        print("%s12 é o MÁXIMO de caractéres %s!" % (red, lightcyan))
                        sleep(2)
                        u()
                        
                    else:
                        while username == "" :
                            run('clear')
                            print("%sCampo de usuario obrigatório %s!" % (red, lightgreen))
                            sleep(1)
                            while01()
                
                        else:

                            # segundo loop usuario
                            def while02():
                                U()
                                while Username == "" :
                                    run('clear')
                                    print("%sCampo de usuario obrigatório %s!" % (red, lightgreen))
                                    sleep(1)
                                    while02()

                                else:
                                    while len(Username) < 12 :
                                        run('clear')
                                        print("%s12 é o MÍXIMO de caractéres %s!" % (red, lightgreen))
                                        sleep(2)
                                        while02()
                                    
                                    else:
                                        while len(Username) > 12 :
                                            run('clear')
                                            print("%s12 é o MÁXIMO de caractéres %s!" % (red, lightgreen))
                                            sleep(1)
                                            while02()

                                        else:
                                            while username != Username :
                                                run('clear')
                                                print("%sDados de usuario não confere %s!" % (red, lightgreen))
                                                sleep(2)
                                                while01()
                                            
                                            else:
                                                # proximo 1 loop senha
                                                def while001():
                                                    p()
                                                    while password == "" :
                                                        run('clear')
                                                        print("%sCampo de senha obrigatório %s!" % (red, lightgreen))
                                                        sleep(1)
                                                        while001()

                                                    else:
                                                        while len(password) < 12 :
                                                            run('clear')
                                                            print("%s12 é o MÍNIMO de caractéres %s" % (red, white))
                                                            sleep(2)
                                                            while001()

                                                        else:
                                                            while password == "" :
                                                                run('clear')
                                                                print("%sCampo de senha obrigatório %s!" % (red, lightgreen))
                                                                sleep(1)
                                                                while001()

                                                            else:
                                                                while len(password) > 12 :
                                                                    run('clear')
                                                                    print("%s12 é o MÁXIMO de caractéres %s" % (red, white))
                                                                    sleep(2)
                                                                    while001()

                                                                else:
                                                                    while password == "" :
                                                                        run('clear')
                                                                        print("%sCampo de senha obrigatório %s!" % (red, lightgreen))
                                                                        sleep(1)
                                                                        while001()

                                                                    else:
                                                                        # segundo loop de senha
                                                                        def while002():
                                                                            P()
                                                                            while Password == "" :
                                                                                run('clear')
                                                                                print("%sCampo de senha obrigatório %s!" % (red, lightgreen))
                                                                                sleep(1)
                                                                                while002()
                                                                                
                                                                            else:
                                                                                while len(Password) < 12 :
                                                                                    run('clear')
                                                                                    print("%s12 é o MÍXIMO de caractéres %s" % (red, white))
                                                                                    sleep(2)
                                                                                    while002()

                                                                                else:
                                                                                    while Password == "" :
                                                                                        run('clear')
                                                                                        print("%sCampo de senha obrigatório %s!" % (red, lightgreen))
                                                                                        sleep(1)
                                                                                        while002()

                                                                                    else:
                                                                                        while len(Password) > 12 :
                                                                                            run('clear')
                                                                                            print("%s12 é o MÁXIMO de caractéres %s" % (red, white))
                                                                                            sleep(2)
                                                                                            while002()
                                                                                        else:
                                                                                            while Password != password :
                                                                                                run('clear')
                                                                                                print("%sDados de senha não confere %s!" % (red, lightgreen))
                                                                                                sleep(2)
                                                                                                while001()
                                                                                            else:

                                                                                                # procwssa
                                                                                                processa()
                                                                                                fin()

                                                                                

                                                                        while002()
                                                while001() 

                            while02()
    while01()


        


def spin():
    invisivel = 'tput civis'
    visivel = 'tput cnorm'
    tamanhoPosicaoF = 'tput cup 20'
    pid = ['■■■■■', '█■■■■', '■█■■■', '■■█■■', '■■■█■', '■■■■█', '■■■■■', '█■■■■', '■█■■■', '■■█■■', '■■■█■', '■■■■█', '■■■■■', ""]
    
    for i in pid:
        system('{}'.format(invisivel))
        system('{}'.format(tamanhoPosicaoF))
        print('\r{}Processando dados...  {}[{}{}{}]'.format(darkgreen, blue, yellow, i, blue))
        sleep(0.08)
        pass
    
    system('{}'.format(tamanhoPosicaoF))
    print('\r%sProcessando dados...  %s[%sDone%s] \n' % (darkgreen, blue, yellow, blue))
    system('{}'.format(visivel))
    


def fin():
    tamanhoPosicaoF = 'tput cup 21'
    invisivel = 'tput civis'
    visivel = 'tput cnorm'
    system('%s' % (tamanhoPosicaoF))
    system('%s' % (invisivel))
    print("\r%sAdicionando Username para Sign     %s[%sno%s]" % (darkgreen, blue, yellow, blue))
    sleep(0.5)

    tamanhoPosicaoF = 'tput cup 21'
    system('%s' % (tamanhoPosicaoF))
    system('%s' % (invisivel))
    print("\r%sAdicionando Username para Sign     %s[%sok%s]" % (darkgreen, blue, yellow, blue))
    sleep(0.5)
    

    tamanhoPosicaoF = 'tput cup 22'

    system('%s' % (tamanhoPosicaoF))
    system('%s' % (invisivel))
    print("\r%sAdicionando Password para Sign   %s[%sno%s]" % (darkgreen, blue, yellow, blue))
    sleep(0.5)

    system('%s' % (tamanhoPosicaoF))
    system('%s' % (invisivel))
    print("\r%sAdicionando Password para Sign   %s[%sok%s]" % (darkgreen, blue, yellow, blue))
    sleep(0.5)


    tamanhoPosicaoF = 'tput cup 23'

    system('%s' % (tamanhoPosicaoF))
    system('%s' % (invisivel))
    print("\r%sRenomeando backup para Sign %s[%sno%s]" % (darkgreen, blue, yellow, blue))
    sleep(0.5)

    system('%s' % (tamanhoPosicaoF))
    system('%s' % (invisivel))
    print("\r%sRenomeando backup para Sign %s[%sok%s]" % (darkgreen, blue, yellow, blue))
    sleep(0.5)


    tamanhoPosicaoF = 'tput cup 24'

    system('%s' % (tamanhoPosicaoF))
    system('%s' % (invisivel))
    print("\r%sRegistrando login          %s[%sno%s]" % (darkgreen, blue, yellow, blue))
    sleep(0.5)


    system('%s' % (tamanhoPosicaoF))
    system('%s' % (invisivel))
    print("\r%sRegistrando login          %s[%sok%s]" % (darkgreen, blue, yellow, blue))
    sleep(0.5)

    
    tamanhoPosicaoF = 'tput cup 25'

    system('%s' % (tamanhoPosicaoF))
    system('%s' % (invisivel))
    print("\r%sCopiando Sign para /bin/Sign          %s[%sno%s]" % (darkgreen, blue, yellow, blue))
    sleep(0.5)

    system('%s' % (tamanhoPosicaoF))
    system('%s' % (invisivel))
    print("\r%sCopiando Sign para /bin/Sign          %s[%sok%s]" % (darkgreen, blue, yellow, blue))
    sleep(0.5)
    
    tamanhoPosicaoF = 'tput cup 26'
    system('%s' % (tamanhoPosicaoF))
    concluir = "\r\n%sSeu usuario é%s: %s'%s%s%s'.%s e sua senha é%s: %s'%s%s%s'%s.\n" % (darkgreen, cyan, white, blue, username, white, darkgreen, cyan, white, blue, password, white, white)

    print(concluir)
    system('%s' % (visivel))
    
    tamanhoPosicaoF = 'tput cup 28'
    system('%s' % (tamanhoPosicaoF))
    print("\n\n%sObs%s! %sReinicie o termux e faça login com dados cadastrados%s" % (darkgreen, red, darkgreen, white))
    sleep(1)
    exit(0)
    

def processa():
    global username, password

    invisivel = 'tput civis'
    visivel = 'tput cnorm'
    tamanhoPosicaoF = 'tput cup 29'
    comuser = 'sed -i "s|oliveobom205|%s|g" Sign.py' % (Username)
    compass = 'sed -i "s|modoevilo205|%s|g" Sign.py' % (Password)
    mod = 'sed -i "s|from config.colors import dict_colors|from colors import dict_colors|g" Sign.py'
    comm = 'rm Sign.py'
    commm = 'cp backup/backup.py Sign.py'


    spin()

    if (path.exists('Sign.py') == True):
        system('%s' % (comm))
        system('%s' % (commm))
        system('%s' % (mod))
        system('%s' % (comuser))
        system('%s' % (compass))

    elif (path.exists('Sign.py') == False):
        system('%s' % (commm))
        system('%s' % (mod))
        system('%s' % (comuser))
        system('%s' % (compass))


verifica_campos()
