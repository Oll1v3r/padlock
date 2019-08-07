#!/usr/bin/env python3
# desc: sign
# autor: olive



from os import system, path
from time import sleep
from optparse import OptionParser

from config.funcoes import menu_list_dd


__autor__ = """\
----------------------------------------------------------------

        Criado por: Olive Silveira.
        Telegram: https://t.me/joinchat/IX29FFjo4hwKBMzMI3LxPQ
        Duvidas FB: https://www.facebook.com/oliveobom
        BLOG: https://olivetech933842787.wordpress.com
        Website: https://techmobilesafe.000webhostapp.com/

---------------------------------------------------------------
"""


if path.exists('config/configure') == False:
    system('mkdir -p config/configure/')

elif path.exists('config/configure') == True:
    pass


def banner():
    system('clear && figlet -f lean SIGN')

banner()

parse = OptionParser()


parse.add_option('--setup-login', '-s', help='Configura login para um tipo de sistema, termux e derivados do debian',  dest='os', metavar='OS')
parse.add_option('--remove-login', '-r', help='Remove configuracao de login', dest='remove', metavar='type-os')
parse.add_option('--list', '-l', help='Lista os sistemas disponiveis', dest='list', metavar='LIST')
parse.add_option('--indent-os', '-o', help='Identifica qual distribuicao usa no momento', dest='indent', metavar='tipo')

(args, options) = parse.parse_args()


rm = "rm -rf $PREFIX/lib/python3.7/Sign/ && rm $PREFIX/bin/Sign && rm ~/.profile"

RM = "rm -rf /usr/lib/python3/dist-packages/Sign/ && rm /usr//bin/Sign  && rm ~/.profile"

distribuicoes = ['ubuntu', 'termux']

if not args.os and not args.remove and not args.list and not args.indent:
    banner()
    print(__autor__)
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
                    print("\033[00;92mLogin configurado com sucesso\033[0m")
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
                    print("\033[00;92mLogin configurado com sucesso.\033[0m")
                    sleep(1)

                elif path.exists('/usr/lib/') == False:
                    print("\033[01;91mVocê não possui sistema debian ou derivado\033[0m")
                    sleep(0.05)
                    exit()

                else:
                    print("\033[01;91mImvalido %s\033[0m" % (ars.os))
                    sleep(1)
                    
            else:
                print("\033[00;92mInvalido %s\033[0m" % (args.os))
    
        elif args.os not in distribuicoes:
            print("\033[01;91mDerivado %s não existe\033[0m" % (args.os))
    
        else:
            print("\033[01;91mInvalido %s\033[0m" % (args.os))
            sleep(1)



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
                    banner()
                    print("\033[00;92mConfiguraçåo ja removida\033[0m")
                    sleep(1)
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
                    print("\033[01;91mVocê não possui um sistema debian ou derivado\033[0m")
        

        else:
            print("\033[01;91mInvalido %s\033[0m" % (args.remove))
            exit(2)



    # opcoes de lista
    elif args.list:
        if args.list[0:3] == "dd":
            print("\033[00;92mListando derivados\033[0m")
            menu_list_dd()
            sleep(1)


    elif args.indent:
        if args.indent[0:2] == "os":

            OS = {"ubuntu": "/bin/bash", "termux": "/data/data/com.termux/files/usr/bin/bash"}
            print("\033[00;92mIdentificando OS\033[0m")
            sleep(1)


            if path.exists(OS['termux']) == True:
                print("\033[00;92mSeu sistema é termux\033[0m")
                sleep(1)
        
            
            elif path.exists(OS['ubuntu']) == True:
                print("\033[00;92mSeu sistema é derivado do debian\033[0m")
                sleep(1)

            elif path.exists(OS['termux']) == False:
                print("\033[00;91mVocê não possui sistema termux\033[0m")
                sleep(1)

            elif path.exists(OS['ubuntu']) == False:
                print("\033[00;91mVocê não possui sistema debian ou derivado\033[0m")
