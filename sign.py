#!/usr/bin/env python
# desc: sign
# autor: olive



from os import system, path
from time import sleep
from optparse import OptionParser


def banner():
    system('clear && figlet -f lean SIGN')

banner()

parse = OptionParser()


parse.add_option('--setup-login', '-s', help='Configura login para um tipo de sistema, termux e derivados do debian',  dest='os', metavar='OS')
parse.add_option('--remove-login', '-r', help='Remove configuracao de login', dest='remove', metavar='name-tool')


(args, options) = parse.parse_args()


rm = "rm -rf $PREFIX/lib/python3.7/Sign/ && rm $PREFIX/bin/Sign && rm ~/.profile"

RM = "rm -rf /var/lib/python3.7/Sign/ && rm /usr/local/bin/Sign && rm ~/.profile"

if not args.os and not args.remove:
    banner()
    print('-h\--help pra mais informações !')

else:
    if args.os:
        if args.os == "termux":

            print("\033[00;92mConfigurando para termux\033[0m")
            sleep(1)
            system('cd config && python3 setup.py && bash configure.sh && cd ..')
            tamanhoPosicaoF = 'tput cup 32'
            system('%s' % (tamanhoPosicaoF))
            print("\033[00;92mLogin configurado com sucesso. 'Ai que delicia' 😂")
            sleep(1)
        
        elif args.os == "debian":
            if path.exists('/usr/local/bin') == True:
                print("\033[00;92mConfigurando derivado do debian\033[0m")
                sleep(1)
                system('cd config && python3 setup.py && bash configure-deri.sh && cd ..')
                tamanhoPosicaoF = 'tput cup 32'
                system('%s' % (tamanhoPosicaoF))
                print("\033[00;92mLogin configurado com sucesso. 'Ai que delicia' 😂\033[0m")
                sleep(1)
            elif path.exists('/usr/local/bim') == False:
                print("Você não possui sistema debian ou derivados")
                sleep(0.05)
                exit()
        else:
            print("\033[00;92mInvalido %s\033[0m" % (args.os))


    # opcao de remocao
    else:
        if args.remove:
            if args.remove == "termux":
                if path.exists('/data/data/com.termux/files/usr/bin/') == True:
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
                    elif path.exists('/data/data/com.termux/files/usr/lib/python3.7/Sign/') == False:
                        print("\033[00;92mConfiguraçåo ja removida\033[0m")
                        sleep(1)
                        system("%s" % (visivel))
                        exit(0)

                elif path.exists('/data/data/com.termux/files/usr/bin/') == False:
                    print("Você não possui sistema termux")
                    sleep(0.05)
            
            elif args.remove == "debian":

                if path.exists('/usr/bin/') == True or path.exists('/bin/') == True or path.exists('/usr/local/bin/') == True :


                    system('clear')
                    banner()
                    tF = 'tput cup 10'
                    visivel = 'tput cnorm'
                    invisivel = 'tput civis'
                
                    if path.exists('/var/lib/python3.7/Sign/') == True:
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

                    elif path.exists('/var/lib/python3.7/Sign/') == False:
                        print("\033[00;92mConfiguraçåo ja removida\033[0m")
                        sleep(1)
                        visivel = 'tput cnorm'
                        system("%s" % (visivel))
                        exit(0)

                else:
                    pass
                #elif path.exists('/usr/bin') == False or path.exists('/bin/') == False or path.exists('/usr/local/bin/') == False:
                    


            else:
                print("\033[01;91mInvalido %s\033[0m" % (args.remove))
                exit(2)
