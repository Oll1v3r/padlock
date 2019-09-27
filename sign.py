#!/usr/bin/env python3
# desc: sign
# autor: olive



from os import system, path
from time import sleep
from optparse import OptionParser

from config.funcoes import menu_list_dd


__autor__ = """\
----------------------------------------------------------------

        BY: olive.
        DUVIDAS: https://t.me/joinchat/IX29FFjo4hwKBMzMI3LxPQ.
        PAGINA FB: https://www.facebook.com/oliveobom.
        BLOG: https://olivetech933842787.wordpress.com.
        Website: https://techmobilesafe.000webhostapp.com/.

---------------------------------------------------------------
"""

# checar se o shell é /bin/bash
if path.exists('/data/data/com.termux/files/home/.termux/') == True:
    system('clear')
    print("Shell '\033[01;91mzsh\033[0m' detectado !, Disponibilidade apenas Shell 'BASH'")
    exit()
    

if path.exists('config/configure') == False:
    system('mkdir -p config/configure/')

elif path.exists('config/configure') == True:
    pass



def teste():

    tamanhoF = 'tput cup 10'

    list_numeric = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    invisivel, visivel = 'tput civis', 'tput cnorm'
    for num in list_numeric:
        system('%s' % (invisivel))
        system('%s' % (tamanhoF))

        print("\033[01;92m\rTemporario \033[0m=\033[00;96m> \033[0m[\033[00;91m%s\033[0m] Testando e 15 segundos. Entre com usuario '\033[00;92m%s\033[0m' e senha '\033[00;92m%s\033[0m' para o seu teste!" % (num, 'rootrootroot', 'toortoortoor'))
        sleep(1)


    system('%s' % (visivel))


parse = OptionParser()
print(parse.expand_prog_name('Sign v1.5 (c) 2019 by olive - Desenvolvido para configurar um sistema de login.'))
parse.set_usage('Usage: sign.py [options] [-s OS|-r OS] [-l dd] [-o os] [-v login]')
parse.add_option('--setup-login', '-s', help='Configura login para um tipo de sistema, termux e derivados do debian',  dest='os', metavar='OS')
parse.add_option('--remove-login', '-r', help='Remove configuracao de login', dest='remove', metavar='type-os')
parse.add_option('--list', '-l', help='Lista os sistemas disponiveis', dest='list', metavar='LIST')
parse.add_option('--indent-os', '-o', help='Identifica qual distribuicao usa no momento', dest='indent', metavar='tipo')
parse.add_option('--view-login', '-v', help='Executa o script apenas para teste', dest='view', metavar='login')
(args, options) = parse.parse_args()


rm = "rm -rf $PREFIX/lib/python3.7/Sign/ && rm $PREFIX/bin/Sign && rm ~/.boot && rm -rf ~/.boot_run && sed -i 's|bash ~/.boot|# Deletado arquivo .boot|g' ~/.bashrc && sed -i 's|# Deletado arquivo .boot||g' ~/.bashrc "

RM = "rm -rf /usr/lib/python3/dist-packages/Sign/ && rm /usr//bin/Sign  && rm ~/.boot && rm ~/.boot_run && sed -i 's|bash ~/.boot|# Deletado aqui o arquivo .boot|g' ~/.profile && sed -i 's|# Deletado aqui o arquivo .boot||g' ~/.profile"
distribuicoes = ['ubuntu', 'termux']

if not args.os and not args.remove and not args.list and not args.indent and not args.view:
    system('clear && figlet -f lean SIGN')
    print(__autor__)
    print('-h\--help pra mais informações !')

else:
    system('clear')
    if args.os:
        system('clear')
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
                system('clear')
                print("\033[00;92mInvalido %s\033[0m" % (args.os))
    
        elif args.os not in distribuicoes:
            system('clear')
            print("\033[01;91mDerivado %s não existe\033[0m" % (args.os))
    
        else:
            system('clear')
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
            system('clear')
            print("\033[00;92mListando derivados\033[0m")
            menu_list_dd()
            sleep(1)


    elif args.indent:
        if args.indent[0:2] == "os":
            system('clear')
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
    

    elif args.view:
        system('clear')
        if args.view == 'login':
            teste()
            system('python3 config/test.py')

        else:
            print("\033[01;91mImvalido %s" % (args.view))



    else:

        system('clear')
