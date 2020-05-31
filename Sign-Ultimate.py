#!/usr/bin/env python3
# Sign-Ultimate
# By: olive


from os import system, path
from time import sleep
import optparse

# setup of system disponible on sign-ulgimate
def setupConfig():
    command = 'cd config && python3 setup.py'
    system('{0}'.format(command))
# test of sign-ultimate
def testConfig():
    command = 'cd config && python3 test.py'
    system(command)
# list of system disponible on sign-ultimate
def listSystem():
    system = ['Termux', 'Gnuroot', 'Userland', 'Nethunter', 'Linux deploy']
    disponible_system = ['Termux']

    for sys in system:
        if(sys not in disponible_system):
            print('\033[01;31m- Indisponível => \033[00;93m%s\033[0m' % (sys))
            sleep(0.5)
        else:
            print('\033[01;32m- Disponível => \033[01;93m%s\033[0m' % (sys))
            sleep(0.5)

def removeConfig():
    if(path.exists('/data/data/com.termux/files/usr/lib/python3.8/Sign-Ultimate') == True):
        system('rm /data/data/com.termux/files/usr/lib/python3.8/Sign-Ultimate/ -rf')
        print("Removido com êxito")
    else:
        print("Ja foi removido")

# opçôes
parse = optparse.OptionParser()
parse.add_option('-?', action='help', help='Mostra ajuda detalhada e sai')

parse.add_option('-s', '--setup', action='store_false', dest='verboseSignSetup', default=True, help='Configura sistema de login')

parse.add_option('-r', '--remove', action='store_false', dest='verboseSignRemove', default=True, help='Remove configuraçäo de login')

parse.add_option('-t', '--test', action='store_false', dest='verboseSignTest', default=True, help='Testa o sistema, serve para testar antes de configurar')

parse.add_option('-l', '--list', action='store_false', dest='verboseSignList', default=True, help='Lista quais sistemas estão disponíveis')

parse.add_option('-i', '--identify', action='store_false', dest='verboseSignIdentify', default=True, help='Identifica qual sistema logado atualmente')
options, args = parse.parse_args()


if(options.verboseSignSetup is not True):
    setupConfig()
elif(options.verboseSignRemove is not True):
    removeConfig()
elif(options.verboseSignTest is not True):
    testConfig()
elif(options.verboseSignList is not True):
    listSystem()
elif(options.verboseSignIdentify is not True):
    identify()
else:
    print('Obs! tente -?/-h/--help p/ mais ajuda de Sign-Ultimate')
