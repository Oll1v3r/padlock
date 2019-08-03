#!/usr/bin/env python
# desc: sign
# autor: olive
# -*- coding: utf-8 -*-

from os import system, path
from time import sleep
from optparse import OptionParser
from sys import version



#if (version[0:3] == '3.7'):
 #   print("Disponivel apenas na versao 3.7 do python3")


def banner():
    system('clear && figlet -f lean SIGN')

banner()

parse = OptionParser()


parse.add_option('--setup-login', '-s', help='Configura login para um tipo de sistema, termux e derivados do debian',  dest='os', metavar='OS')
parse.add_option('--remove-login', '-r', help='Remove configuracao de login', dest='remove', metavar='name-tool')
parse.add_option('--list', '-l', help='Lista os sistemas disponiveis', dest='list', metavar='LIST', default=4, type=str)

(args, options) = parse.parse_args()


rm = "rm -rf $PREFIX/lib/python3.7/Sign/ && rm $PREFIX/bin/Sign && rm ~/.profile "

RM = "rm -rf /usr/lib/python3/dist-packages/Sign/ && rm /usr//bin/Sign  && rm ~/.profile"

distribuicoes = ['debian', 'ubuntu', 'kali', 'parrot']

if not args.os and not args.remove:
    banner()
    print('-h\--help pra mais informações !')

else:
    if args.os:
        if args.os == "termux":
            if path.exists('/data/data/com.termux/files/usr/lib/python3.7/Sign') == True:
                print("\033[0mExiste uma configuração em andamento\033[1;91m! \033[0mobs\033[1;91m!\033[0m, remova a configuração atual\033[0m")
                sleep(1)

            elif path.exists('/data/data/com.termux/files/usr/lib/python3.7/Sign') == False:

                if path.exists('/data/data/com.termux/files/usr/lib/') == True:
                    print("\033[00;92mConfigurando para termux\033[0m")
                    sleep(1)
                    system('cd config && python3 setup.py && bash configure.sh && cd ..')
                    tamanhoPosicaoF = 'tput cup 32'
                    system('%s' % (tamanhoPosicaoF))
                    print("\033[00;92mLogin configurado com sucesso. 'Ai que de maaais' 😂")
                    sleep(1)
                elif path.exists('/data/data/com.termux/files/usr/lib/') == False:
                    print("\033[01;91mVocê não possui sistema termux\033[0m")
                    sleep(1)
        
        elif args.os == "ubuntu" or args.os in distribuicoes:
            if path.exists('/usr/lib/python3/dist-packages/Sign') == True:
                print("\033[01;91mExiste uma configuração em andamento\033[1;91m! \033[0mobs\033[1;91m!\033[0m, remova a configuração atual")
                sleep(1)

            elif path.exists('/usr/lib/python3/dist-packages/Sign') == False:

                if path.exists('/usr/lib/') == True:
                    print("\033[00;92mConfigurando derivado do debian\033[0m")
                    sleep(1)
                    system('cd config && python3 setup-deri.py && bash configure-deri.sh && cd ..')
                    tamanhoPosicaoF = 'tput cup 32'
                    system('%s' % (tamanhoPosicaoF))
                    print("\033[00;92mLogin configurado com sucesso. 'Ai que de maaais' 😂\033[0m")
                    sleep(1)

                elif path.exists('/usr/lib/') == False:
                    print("\033[01;91mVocê não possui sistema debian ou derivado\033[0m")
                    sleep(0.05)
                    exit()
            else:
                print("\033[00;92mInvalido %s\033[0m" % (args.os))
    


    # opcao de remocao
    elif args.remove:
        if args.remove == "termux":
            if path.exists('/data/data/com.termux/files/usr/lib/') == True:
                system('clear')
                tF = 'tput cup 10'
                visivel = 'tput cnorm'
                invisivel = 'tput civis'
                    
                if path.exists('/data/data/com.termux/files/usr/lib/python3.7/Sign/') == True:
                    system("%s" % (tF))
                    system('%s' % (invisivel))
                    print("\033[00;92m\rDesfazendo configuração \033[00;94m [\033[01;91mno\033[00;94m] \033[0m")
                    sleep(3)

                    system('%s' % (rm))
                    system("%s" % (tF))
                    system('%s' % (invisivel))
                    print("\033[00;92m\rDesfazendo configuração \033[00;94m [\033[01;91mok\033[00;94m] \033[0m")
                    sleep(1)
                    system("%s" % (visivel))

                elif path.exists('/data/data/com.termux/files/usr/lib/python3.*/Sign/') == False:
                    print("\033[00;92mConfiguraçåo ja removida\033[0m")
                    sleep(1)
                    system("%s" % (visivel))
                    exit(0)

            elif path.exists('/data/data/com.termux/files/usr/lib/') == False:
                print("\033[01;91mVocê não possui sistema termux\033[0m")
                sleep(0.05)
            

        elif args.remove == "ubuntu":
            if path.exists('/usr/lib/') == True:
                
                system('clear')
                banner()
                tF = 'tput cup 10'
                visivel = 'tput cnorm'
                invisivel = 'tput civis'
                
                if path.exists('/usr/lib/python3/dist-packages/Sign/') == True:
                    system("%s" % (tF))
                    system('%s' % (invisivel))
                    print("\033[00;92m\rDesfazendo configuração \033[00;94m [\033[01;91mno\033[00;94m] \033[0m")
                    sleep(3)
                    system('%s' % (RM))
                    system("%s" % (tF))
                    system('%s' % (invisivel))
                    print("\033[00;92m\rDesfazendo configuração \033[00;94m [\033[01;91mok\033[00;94m] \033[0m")
                    sleep(1)
                    system("%s" % (visivel))

                elif path.exists('/usr/lib/python3/dist-packages/Sign/') == False:
                    print("\033[00;92mConfiguraçåo ja removida\033[0m")
                    sleep(1)
                    visivel = 'tput cnorm'
                    system("%s" % (visivel))
                    exit(0)

            else:
                    print("Você não possui um sistema debian ou derivado")

        else:
            print("\033[01;91mInvalido %s\033[0m" % (args.remove))
            exit(2)
