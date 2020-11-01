import os
import time
def verifyTest(username, password):
    os.system('clear')
    def firstUser():
        print('\r    '+'_'*43)
        print("""\r
     ▒█▀▀█ █▀▀█ █▀▀▄ █░░ █▀▀█ █▀▀ █░█
     ▒█▄▄█ █▄▄█ █░░█ █░░ █░░█ █░░ █▀▄
     ▒█░░░ ▀░░▀ ▀▀▀░ ▀▀▀ ▀▀▀▀ ▀▀▀ ▀░▀


     User Name :

     Pass Word :
   

    {}

        """.format('_'*43))
        global firstUsername
        os.system('tput cnorm')
        os.system('tput cup 7')
        firstUsername = input('\r\t\t ')
        os.system('tput civis')
        while firstUsername == '':
            os.system('tput cup 11')
            print('\r\t\t\tUser required!')
            time.sleep(0.3)
            os.system('clear')
            firstUser()
        else:
            while firstUsername != username:
                os.system('tput cup 11')
                # os.system('tput civis')
                print('\r\t\t\tUser incorrect!')
                time.sleep(0.3)
                os.system('clear')
                firstUser()
            else:
                pass
            pass

        def firstPass():
            os.system('clear')
            print('\r    '+'_'*43)
            print("""\r
     ▒█▀▀█ █▀▀█ █▀▀▄ █░░ █▀▀█ █▀▀ █░█
     ▒█▄▄█ █▄▄█ █░░█ █░░ █░░█ █░░ █▀▄
     ▒█░░░ ▀░░▀ ▀▀▀░ ▀▀▀ ▀▀▀▀ ▀▀▀ ▀░▀


     User Name : {}

     Pass Word : 


    {}
              """.format(firstUsername, '_'*43))
            global firstPassword
            os.system('tput cnorm')
            os.system('tput cup 9')
            firstPassword = input('\r\t\t ')
            os.system('tput civis')
            while firstPassword == '':
                os.system('tput cup 11')
                print('\r\t\t\tPass required!')
                time.sleep(0.3)
                firstPass()
            else:
                while firstPassword != password:
                    os.system('tput cup 11')
                    print('\r\t\t\tPass incorrect!')
                    time.sleep(0.3)
                    firstPass()
                else:
                    sucess()
                    os.system('tput cup 19')
                    print('Sucessfuly Ok')
                    os.system('tput cnorm')
                    exit()
        firstPass() 
    firstUser()


def sucess():
    steps = ['[□□□□□□]','[■□□□□□]','[□■□□□□]','[□□■□□□]','[□□□■□□]','[□□□□■□]','[□□□□□■]','[■□□□□□]','[□■□□□□]','[□□■□□□]','[□□□■□□]','[□□□□■□]','[□□□□□■]','[ Done ]']

    for step in steps:
        os.system('tput cup 17')
        print('\r    Loading... {}'.format(step))
        time.sleep(0.1)

