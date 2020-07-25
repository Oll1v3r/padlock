#!/usr/bin/env python3
# By: olive
# Version: v1.7
# Desc: setup from a logim system

# modules important
from os import system, path
from os.path import exists as exist
from time import sleep, localtime

system('clear')


# verify if the file '.data.txt' exist in ./ and is removid 
def remove_file_data():
    if(path.exists('.data.txt') == exist):
        system('rm ./.data.txt')
    else:
        pass


banner = """\033[00;92m

     _/_/_/              _/
   _/          _/_/    _/_/_/_/  _/    _/  _/_/_/
    _/_/    _/_/_/_/    _/      _/    _/  _/    _/
       _/  _/          _/      _/    _/  _/    _/
_/_/_/      _/_/_/      _/_/    _/_/_/  _/_/_/
                                       _/
                                      _/
"""
about = """
        \033[01;92mName\033[0m: \033[02;94m(\033[01;93msetup\033[02;94m)\033[0m, \033[01;92mVersion\033[0m: \033[02;94m(\033[01;93mv1.7\033[02;94m)
        \033[01;92mBy\033[0m: \033[02;94m(\033[01;93mOlive\033[02;94m)\033[0m, \033[01;92mFont by\033[0m: \033[02;94m(\033[02;93mRemo773\033[02;94m)
"""

caracteres = "@#$%&*-_+([)]!:;/?~|•√Π÷×{}£¢€°^_=[]™®©¶\<>"
caracteres = list(caracteres)
caracteres.sort()

def principalFuncao():
    print(banner)
    print(about)
    print('\t\033[01;92mRegistrar dados de login\n\n\033[0m')

    def user():
        global username
        username = input('Digite o NOVO Username: ')
        # tratar campo
        while username == "":
            print('\033[01;91mCampo necessário, preenchimento obrigatório\033[02;92m!\033[0m')
            user()
        else:
            pass
        def userRepeat():
            global usernameRepeat
            usernameRepeat = input('Digite NOVAMENTE o Username: ')
            while usernameRepeat == "":
                print('\033[01;91mCampo necessário, preenchimento obrigatório\033[02;92m!\033[0m')
                userRepeat()
            else:
                pass
            while username != usernameRepeat:
                print('\033[01;91mDados de username não correspondam \033[02;92m!\033[01;91m tente novamente\033[0m')
                user()
            else:
                pass
            def ppass():
                global ppassword
                ppassword = input('Digite uma senha NOVA: ')
                # tratar campo
                while ppassword == "":
                    print('\033[01;91mCampo necessário, preenchimento obrigatório\033[02;92m!\033[0m')
                    ppass()
                else:
                    pass
                def ppassRepeat():
                    global ppasswordRepeat
                    ppasswordRepeat = input('Digite NOVAMENTE o Password: ')
                    while ppasswordRepeat == "":
                        print('\033[01;91mCampo necessário, preenchimento obrigatório\033[02;92m!\033[0m')
                        ppassRepeat()
                    else:
                        pass
                    while ppassword != ppasswordRepeat:
                        print('\033[01;91mDados de senha não correspondam \033[02;92m! \033[01;91mtente novamente\033[0m')
                        ppass()
                    else:
                        pass

                    # Cria arquivo contendo os dados passado na entrada
                    system("clear")
                    system("tput civis;tput cup 0")
                    print("\r" + banner)
                    system("tput cup 10")
    
                    print("\r\033[02;92mCriando arquivo... [\033[00;93mNone\033[02;92m]")
                    sleep(1)
                    fileOpen = open('.login.txt', 'w')
                    fileOpen.write('%s\n%s\n' % (usernameRepeat, ppasswordRepeat))
                    fileOpen.close()
                    # Verificar se o arquivo foi criado com sucesso
                    system("tput cup 0")
                    print("\r" + banner)
                    if(exist(".login.txt") == bool(True)):
                        system("tput cup 10")
                        print("\r\033[02;92mCriando arquivo... [\033[00;93mDone\033[02;92m]")
                        sleep(1)
                        system("mv .login.txt $HOME/Sign-Ultimate/config/login")
                        system("tput cup 11")
                        print("\r\033[02;92mCopiando Sign para /lib [\033[00;93mNone\033[02;92m]")
                        sleep(1)
                        system("cp $HOME/Sign-Ultimate /data/data/com.termux/files/usr/lib/python3.8 -rf")
                        # Verificar se Sign foi copiado para /lib
                        if(exist("/data/data/com.termux/files/usr/lib/python3.8/Sign-Ultimate") == bool(True)):
                            system("tput cup 11")
                            print("\r\033[02;92mCopiando Sign para /lib [\033[00;93mDone\033[02;92m]")
                            sleep(1)
                            system("tput cup 11")        
                            sleep(1)
                            system("tput cup 12")
                            print("\r\033[02;92mCriando arquivo de registro 'registro.txt' [\033[00;93mNone\033[02;92m]")
                            sleep(1)
                            # Contagem de segundos
                            num = 6
                            while(num >= 0):
                                system('tput cup 13')
                                print("\033[02;94m\rPermita o acesso a memória interna em [\033[02;92m%s\033[02;94m] segundos" % num)
                                sleep(1)

                                num -= 1

                            system("termux-setup-storage")
                            # Verificar se o acesso a memória foi permitida
                            if(exist("/data/data/com.termux/files/home/storage") == bool(True)):
                                # Copiar arquivo para memória interna
                                temp = list(localtime())
                                fileOpenLog = open('registro.txt', 'w')
                                fileOpenLog.write('Dados de acesso ao painel de login feitos na data: [%s/%s/%s] As %s:%s e %s segundos.\n\nUsername: %s\nPassword: %s\n\n\n© Copyright Olliv3r - %s\n' % (temp[2], temp[1], temp[0], temp[3], temp[4], temp[5], usernameRepeat, ppasswordRepeat, temp[0]))
                                fileOpenLog.close()
                                # Verificar se arquivo 'registro.txt' foi criado com sucesso
                                if(exist('registro.txt') == bool(True)):
                                    system('mv registro.txt /sdcard/')
                                    system('tput cup 12')
                                    print("\r\033[02;92mCriando arquivo de registro 'registro.txt' [\033[00;93mDone\033[02;92m]")
                                    system('tput cup 20')
                                    system('tput cnorm')
                                    # Configurando login para ser executado na inicialização do shell
                                    system('bash configure.sh')
                                    # CONTINUA AQUI
                                    print("Ok")
                                    exit()

                            elif(exist("/data/data/com.termux/files/home/storage") == bool(False)):
                                system('tput cup 12')
                                print("\r\033[02;92mCriando arquivo de registro 'registro.txt' [\033[00;93mFailed\033[02;92m]")
                                sleep(1)
                                system("tput cup 14")
                                print("\033[01;91mÉ necessário o acesso a memória interna para poder colar o arquivo 'registro.txt' para memória interna")
                                sleep(1)
                                exit()
                        elif(exist("/data/data/com.termux/files/usr/lib/python3.*/Sign-Ultimate") == bool(False)):
                            system('tput cup 11')
                            print("\r\033[02;92mCopiando Sign para /lib [\033[00;93mFailed\033[02;92m]")
                            system('tput cup 12')
                            print("Sign não foi copiado com sucesso \033[00;92m!\033[0m")
                            exit()
                    elif(exist("/data/data/com.termux/files/home/Sign-Ultimate/config/login/login.txt") == bool(False)):
                        print("Não foi possível criar o arquivo !")
                        exit()

                ppassRepeat()
            ppass()

        userRepeat()
    user()



principalFuncao()
