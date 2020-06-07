#!/usr/bin/env python3
# By: olive
# Version: v1.2
# Desc: setup from a logim system

# modules important
from os import system, path
from time import sleep, localtime

bash = system
bash('clear');
distr = ['termux', 'gnuroot', 'userland', 'kali nethunter', 'linux deploy']
exist = True

# verify if the file '.data.txt' exist in ./ and is removid
def remove_file_data():
    if(path.exists('.data.txt') == exist):
        system('rm ./.data.txt')
    else:
        pass

# window
def window():
    
    bash('clear')
    print("""
        1) Termux (android)
        2) Gnuroot debian (Android)
        3) Userland (android)
        4) Kali Nethunter (android)
        5) Linux deploy (android)
    """)

    system = input('Qual seu sistema? => ')
    
    global systema
    systema = system

    if(system == '1'):
        bash("clear")
        systema = 'termux'
        processLogin(systema)
        add_path()
    elif(system == '2'):
        systema = 'gnuroot'
        processLogin(systema)
    elif(system == '3'):
        systema = 'userland'
        processLogin(systema)
    elif(system == '4'):
        systema = 'kali nethunter'
        procesLogin(systema)
    elif(system == '5'):
        systema = 'linux deploy'
        processLogin(systema)
    elif(system == ''):
        print('\033[01;91mCampo obrigatório\033[0m')
        sleep(2)
        window()
    else:
        print('\033[01;91mOpção inválida, tente números entre 1 e 5\033[0m')
        sleep(2)
        window()

def processLogin(system="termux"):
    if(system not in distr):
        print('\033[01;91mIndisponível para sistema \033[01;93m({})\033[0m'.format(system))
        sleep(2)
        window()
    # os-1
    elif(system in distr):
        pwd = "/data/data/com.termux/files/usr/etc/apt"
        openFileApt = open(pwd+"/sources.list", "r")
        openFileApt = list(openFileApt)
        
        counter = 0
        for link in openFileApt:
            link = link.rstrip()
            counter += 1
            # 1
            if counter == 2:
                if(link[4:22] == "https://termux.org" or "https://termux.net"):

                    print("Configurando para sistema: {}".format(system))
                    def capture_input_user_var():
                        global username_repeat
                        username_repeat = ""
            
                        bash('clear')
                        username = input('Digite um usuário: ')
                        while username == "":
                            print("Campo de usuário obrigatório")
                            sleep(1)
                            capture_input_user_var()
                        else:
                            def capture_input_user_vars():
                                username_repeat = input('Digite novamente: ')
                                while username_repeat == "":
                                    print("Campo de usuário obrigatório")
                                    sleep(1)
                                    capture_input_user_vars()
                                else:
                                    while username != username_repeat:
                                        print('! Falha: Dados de usuário não confere')
                                        sleep(1)
                                        capture_input_user_var()
                                    else:
                                        def capture_input_pass_var():
                                            global password_repeat
                                            password_repeat = ""

                                            bash('clear')
                                            password = input('Digite uma senha: ')
                                            while password == "":
                                                print("Campo de senha obrigatório")
                                                sleep(1)
                                                capture_input_pass_var()
                                            else:
                                                def capture_input_pass_vars():
                                                    password_repeat = input('Digite novamente: ')
                                                    while password_repeat == "":
                                                        print("campo de senha obrigatório")
                                                        sleep(1)
                                                        capture_input_pass_vars()
                                                    else:
                                                        while password != password_repeat:
                                                            print('! Falha: Dados de senha não confere')
                                                            sleep(1)
                                                            capture_input_pass_var()
                                                        else:
                                                            remove_file_data()
                                                            login_file = open('.data.txt', 'a')
                                                            login_file.write('{}\n'.format(username_repeat))
                                                            login_file.write('{}\n'.format(password_repeat))
                                                            login_file.close()

                                                capture_input_pass_vars()
                                        capture_input_pass_var()

                            capture_input_user_vars()
                    capture_input_user_var()

                else:
                    print("\033[01;91mSeu sistema não possúi \033[00;94m'\033[00;93m%s\033[00;94m'\033[0m" % systema)
                    exit()
            # 2
    # os-2

def add_path():
    if(path.exists('/data/data/com.termux/files/usr/lib/python3.8/Sign-Ultimate') != True):
        print('\033[00;92mCopiando diretório Sign-Ultimate para /lib/python3.8/')
        sleep(1)
        system('cp /data/data/com.termux/files/home/Sign-Ultimate/ /data/data/com.termux/files/usr/lib/python3.8/ -rf')
        print('\033[00;92mCriando log "data.txt" e copiando para /sdcard/')
        sleep(1)
        index = open('dataLogin.txt', 'a')
        index.write('Dados de login:\n')
        index.write('Data do registro: {0}/{1}/{2} as {3} horas e {4} minútos e {5} segundos\n'.format(localtime()[2], localtime()[1], localtime()[0], localtime()[3], localtime()[4], localtime()[5]))
        index.write('Username: {}\n'.format(username_repeat))
        index.write('Password: {}\n'.format(password_repeat))
        index.write('\nCopyright Sign-Ultimate - {0}'.format(localtime()[0]))
        index.close()
        if(path.exists('dataLogin.txt') == False):
            print("\033[00;92m! \033[01;91mErro ao encontrar o arquivo de log\033[0m")
        else:
            if(path.exists('/sdcard/') == False):
                print("Diretório /sdcard não foi encontrado")
                exit()
            else:
                system("bash configure.sh")
                print("\n\033[00;95mAceite o acesso a memoria interna\033[0m")
                system("termux-setup-storage && mv dataLogin.txt /sdcard")
                print("\033[00;92mConfigurado com êxito\033[0m")
                print("")
                fileOpenRegist = open('.data.txt','r')
                fileOpenRegist = list(fileOpenRegist)
                print("\033[01;93mUsuário\033[0m: \033[00;94m%s\033[0m" % fileOpenRegist[0])
                print("\033[01;93mSenha\033[0m: \033[00;94m%s\033[0m" % fileOpenRegist[1])
                print("Execute 'exit' e entre novamente para ver o efeito")

                os = open('.os.txt', 'w')
                os.write('{}\n'.format(systema))
                os.close()
    else:
        print("Obs! \033[01;93mExiste uma configuraçäo em andamento, remova primeiro a configuraçäo atual\033[0m")



window()
