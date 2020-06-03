#!/usr/bin/env python3
# By: olive
# Version: v1.2
# Desc: setup from a logim system

# modules important
from os import system, path
from time import sleep, localtime

bash = system
bash('clear');
distr = ['termux']
exist = True

# verify if the file '.data.txt' exist in ./ and is removid
def remove_file_data():
    if(path.exists('.data.txt') == exist):
        system('rm ./.data.txt')
    else:
        pass

# window
def window():
    print("""
        1) Termux (android)
        2) Gnuroot debian (Android)
        3) Userland (android)
        4) Kali Nethunter (android)
        5) Linux deploy (android)
    """)

    system = int(input('Qual seu sistema? => '))

    if(system == 1):
        bash("clear")
        systema = 'termux'
        capture_input_user(systema)
        add_path()
    elif(system == 2):
        systema = 'gnuroot'
        capture_input_user(systema)
    elif(system == 3):
        systema = 'userland'
        capture_input_user(systema)
    elif(system == 4):
        systema = 'kali nethunter'
        capture_input_user(systema)
    elif(system == 5):
        systema = 'linux deploy'
        capture_input_user(systema)
    else:
        print('Opção inválida, tente números entre 1 e 5')

def capture_input_user(system="termux"):
    if(system not in distr):
        print('Indisponível para sistema {}'.format(system))
        exit(0)
    elif(system in distr):
        print("Configurando para sistema: {}".format(system))
        username = input('Digite um usuário: ')
        global username_repeat
        username_repeat = input('Digite novamente: ')

        while username != username_repeat:
            bash('clear')
            capture_input_user()
        else:
            def capture_input_pass():
                password = input('Digite uma senha: ')
                global password_repeat
                password_repeat = input('Digite novamente: ')
                while password != password_repeat:
                    bash("clear")
                    capture_input_pass()
                else:
                    remove_file_data()
                    login_file = open('.data.txt', 'a')
                    login_file.write('{}\n'.format(username_repeat))
                    login_file.write('{}\n'.format(password_repeat))
                    login_file.close()

            capture_input_pass()

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
                print("Diretório /sdcad não foi encontrado")
                exit()
            else:
                system("bash configure.sh")
                print("Aceite o acesso a memoria interna")
                system("termux-setup-storage && mv dataLogin.txt /sdcard")
                print("\033[00;92mConfigurado com êxito\033[0m")
                print("")
                fileOpenRegist = open('.data.txt','r')
                fileOpenRegist = list(fileOpenRegist)
                print("Usuário: %s" % fileOpenRegist[0])
                print("Senha: %s" % fileOpenRegist[1])
                print("execute 'exit' e entre novamente para ver o efeito")
    else:
        print("Obs! \033[01;93mExiste uma configuraçäo em andamento, remova primeiro a configuraçäo atual\033[0m")


window()

