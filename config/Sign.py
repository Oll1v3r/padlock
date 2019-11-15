#!/data/data/com.termux/files/usr/bin/env python3
# Descricao: login do termux
# Autor: olive

from os import system
from time import sleep
from colors import dict_colors
from getpass import getpass

# cores

(white, red, darkgreen, green, lightgreen, yellow, blue, darkblue, lightcyan, lightred, lightblue, cyan) = (dict_colors['coresNormais']['white'], dict_colors['coresNormais']['red'], dict_colors['coresEscuras']['darkgreen'], dict_colors['coresClaras']['lightgreen'],  dict_colors['coresNormais']['green'], dict_colors['coresNormais']['yellow'], dict_colors['coresNormais']['blue'], dict_colors['coresEscuras']['darkblue'], dict_colors['coresClaras']['lightcyan'], dict_colors['coresClaras']['lightred'], dict_colors['coresClaras']['lightblue'], dict_colors['coresNormais']['cyan'])


def janela1():
    system('clear')
    print("""

   %s┌──────────────────────────────────────────────────────────┐
   %s│%s\t╺┳╸┏━╸┏━┓┏┳┓╻ ╻╻ ╻  ┏━┓╻ ╻┏━┓╺┳╸┏━╸┏┳┓%s                │
   %s│%s\t ┃ ┣╸ ┣┳┛┃┃┃┃ ┃┏╋┛  ┗━┓┗┳┛┗━┓ ┃ ┣╸ ┃┃┃%s                │
   %s│%s\t ╹ ┗━╸╹┗╸╹ ╹┗━┛╹ ╹  ┗━┛ ╹ ┗━┛ ╹ ┗━╸╹ ╹%s                │
   %s│%s\t                                       %s               │
   %s│%s     User Name %s:                            %s              │
   %s│%s                                              %s            │
   %s│%s     Password  %s:                            %s              │ 
   %s│%s                                           %s               │
   %s│%s\t                      %s                                │
   %s╘──────────────────────────────────────────────────────────┘
   
    """ % (blue,\
            blue, red, blue,\
            blue, red, blue,\
            blue, red, blue,\
            blue, white, blue,\
            blue, darkgreen, cyan, blue,\
            blue, white, blue,\
            blue, darkgreen, cyan, blue,\
            blue, white, blue,\
            blue, white, blue,\
            blue))

    
def janela2():
    system('clear')
    print("""
      
   %s┌──────────────────────────────────────────────────────────┐
   %s│%s\t╺┳╸┏━╸┏━┓┏┳┓╻ ╻╻ ╻  ┏━┓╻ ╻┏━┓╺┳╸┏━╸┏┳┓  %s              │
   %s│%s\t ┃ ┣╸ ┣┳┛┃┃┃┃ ┃┏╋┛  ┗━┓┗┳┛┗━┓ ┃ ┣╸ ┃┃┃  %s              │
   %s│%s\t ╹ ┗━╸╹┗╸╹ ╹┗━┛╹ ╹  ┗━┛ ╹ ┗━┛ ╹ ┗━╸╹ ╹  %s              │
   %s│%s\t                                            %s          │
   %s│%s     User Name %s: %s%s                       %s      │
   %s│%s                                             %s             │
   %s│%s     Password  %s:                            %s              │
   %s│%s                                             %s             │
   %s│%s\t                                          %s            │
   %s╘──────────────────────────────────────────────────────────┘

    """ % (blue, blue, red, blue, blue, red, blue, blue, red, blue, blue, white, blue, blue, darkgreen, cyan, red, username, blue, blue, white, blue, blue, darkgreen, cyan, blue, blue, white, blue, blue, white, blue, blue))



def janela3():
    system('clear')
    print("""\r

  %s┌──────────────────────────────────────────────────────────────┐
  %s│ %s██╗     ██╗███╗   ██╗██╗   ██╗██╗  ██╗     ██████╗ ███████╗ %s │
  %s│ %s██║     ██║████╗  ██║██║   ██║╚██╗██╔╝    ██╔═══██╗██╔════╝  %s│
  %s│ %s██║     ██║██╔██╗ ██║██║   ██║ ╚███╔╝     ██║   ██║███████╗  %s│
  %s│ %s██║     ██║██║╚██╗██║██║   ██║ ██╔██╗     ██║   ██║╚════██║  %s│
  %s│ %s███████╗██║██║ ╚████║╚██████╔╝██╔╝ ██╗    ╚██████╔╝███████║  %s│
  %s│ %s╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚══════╝  %s│
  %s│                                                              %s│
  %s│                                                              %s│
  %s│     %sUser Name %s:                                              %s│
  %s│                                                              %s│
  %s│     %sPassword  %s:                                              %s│
  %s│                                                              %s│
  %s│                                                              %s│
  %s╘──────────────────────────────────────────────────────────────┘

  """ % (darkblue, \
        darkblue, red, darkblue, \
        darkblue, red, darkblue, \
        darkblue, red, darkblue, \
        darkblue, red, darkblue, \
        darkblue, red, darkblue, \
        darkblue, red, darkblue, \
        darkblue, darkblue, \
        darkblue, darkblue, \
        darkblue, lightgreen, cyan, darkblue, \
        darkblue, darkblue, \
        darkblue, lightgreen, cyan, darkblue, \
        darkblue, darkblue, \
        darkblue, darkblue, \
        darkblue
        ))

def janela4():
    system('clear')
    print("""

  %s┌──────────────────────────────────────────────────────────────┐
  %s│ %s██╗     ██╗███╗   ██╗██╗   ██╗██╗  ██╗     ██████╗ ███████╗ %s │
  %s│ %s██║     ██║████╗  ██║██║   ██║╚██╗██╔╝    ██╔═══██╗██╔════╝  %s│
  %s│ %s██║     ██║██╔██╗ ██║██║   ██║ ╚███╔╝     ██║   ██║███████╗  %s│
  %s│ %s██║     ██║██║╚██╗██║██║   ██║ ██╔██╗     ██║   ██║╚════██║  %s│
  %s│ %s███████╗██║██║ ╚████║╚██████╔╝██╔╝ ██╗    ╚██████╔╝███████║  %s│
  %s│ %s╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚══════╝  %s│
  %s│                                                              %s│    
  %s│                                                              %s│
  %s│     %sUser Name %s: %s%s                                 %s│
  %s│                                                              %s│
  %s│     %sPassword  %s:                                              %s│
  %s│                                                              %s│
  %s│                                                              %s│
  %s╘──────────────────────────────────────────────────────────────┘
""" % (darkblue, \
        darkblue, red, darkblue, \
        darkblue, red, darkblue, \
        darkblue, red, darkblue, \
        darkblue, red, darkblue, \
        darkblue, red, darkblue, \
        darkblue, red, darkblue, \
        darkblue, darkblue, \
        darkblue, darkblue, \
        darkblue, lightgreen, cyan, red, username, darkblue, \
        darkblue, darkblue, \
        darkblue, lightgreen, cyan, darkblue, \
        darkblue, darkblue, \
        darkblue, darkblue, \
        darkblue
        ))


# tamanhos e margem do cursor
invisivel = 'tput civis'
visivel = 'tput cnorm'
tamanhoU = 'tput cup 11 20'
tamanhoP = 'tput cup 13 20'
tamanhoL = 'tput cup 20'
tamanhoF = 'tput cup 21'
tamanhoEU = 'tput cup 12 40'
tamanhoEP = 'tput cup 14 40'
clean = 'tput clear'


# obs! login padrao, pode ser alterado por você
USUARIO = "oliveobom100"
SENHA = "modoevilo001"

# DICA! pressionar 'CTR+4' em caso de esquecimento dos dados de login


def posicaoCursorU():
    system("%s" % (tamanhoU))

def posicaoCursorP():
    system("%s" % (tamanhoP))

def u():
    global username
    username = str(input((lightred)))

def p():
    global password
    password = getpass(lightred)

#▐

#▗


list_Char = ['▗▗▗▗▗', '▐▗▗▗▗','▗▐▗▗▗','▗▗▐▗▗','▗▗▗▐▗','▗▗▗▗▐','▗▗▗▗▗','▐▗▗▗▗','▗▐▗▗▗','▗▗▐▗▗','▗▗▗▐▗','▗▗▗▗▐']

list_char = ['■■■■■', '█■■■■', '■█■■■', '■■█■■', '■■■█■', '■■■■█', '█■■■■', '■█■■■', '■■█■■', '■■■█■', '■■■■█', '█■■■■', '■█■■■', '■■█■■', '■■■█■', '■■■■█', '█■■■■', '■█■■■', '■■█■■', '■■■█■', '■■■■█', '■■■■■']

def loading():
    
    for char in list_Char:
        system("%s" % (tamanhoL))
        print("\n\r    %sLOADING... %s[%s%s%s]" % (green, darkgreen, yellow, char, darkgreen))
        system("%s" % (invisivel))
        sleep(0.08)


def main():
    
    def while1():
        janela3()
        posicaoCursorU()
        system('%s' % (visivel))
        u()
    
        while username == "" :
            system("%s" % (tamanhoEU))
            system("%s" % (invisivel))
            print("%sCampo obrigatório%s! %s" %(darkgreen, red, white))
            system("%s" % (tamanhoU))
            sleep(0.5)
            while1()
                                     #
        else:
            while username != USUARIO:
                system("%s" % (tamanhoEU))
                system("%s" % (invisivel))
                print("%s Usuario incorreto%s! %s" %(darkgreen, red, white))
                system("%s" % (tamanhoU))
                sleep(0.5)
                while1()
        
            else:
                while username == "":
                    system("%s" % (tamanhoEU))
                    system("%s" % (invisivel))
                    print("%s Campo obrigatório%s! %s" %(darkgreen, red, white))
                    system("%s" % (tamanhoU))
                    sleep(0.5)
                    while1()

                else:
                
                    def while2():
                        janela4()
                        posicaoCursorP()
                        system("%s" % (visivel))
                        p()

                        while password == "":
                            system("%s" % (tamanhoEP))
                            system("%s" % (invisivel))
                            print("%s Campo obrigatório%s! %s" % (darkgreen, red, white))
                            sleep(0.5)
                            while2()
                    
                        else:
                            while password != SENHA:
                                system("%s" % (tamanhoEP))
                                system("%s" % (invisivel))
                                print("%s Senha incorreto%s! %s" % (darkgreen, red, white))
                                sleep(0.5)
                                system("%s" % (tamanhoP))
                                while2()

                            else:
                                while password == "":
                                    system("%s" % (tamanhoEP))
                                    system("%s" % (invisivel))
                                    print("%s Campo obrigatorio%s! %s" % (darkgreen, red, white))
                                    sleep(0.5)
                                    while2()
                        
                                else:
                                    loading()
                                    system("%s" % (invisivel))
                                    system("%s" % (tamanhoF))
                                    print("    %sLOADING... %s[%sDone%s] %s" % (green, darkgreen, yellow, darkgreen, white))
                                    system("%s" % (visivel))
                                    exit()

                                    
                    while2()
    while1()

if __name__ =='__main__':

    try:
        main()
    except KeyboardInterrupt:
        system("%s" % (tamanhoF))
        print("Encerrando com tecla CTR+C")
        sleep(1)
        system("exec /data/data/com.termux/files/usr/lib/python3.7/Sign/PID")
    except EOFError:
        system("%s" % (tamanhoF))
        print("Encerrando com tecla CTR+D")
        sleep(1)
        system("exec /data/data/com.termux/files/usr/lib/python3.7/Sign/PID")
    #except:
     #   print("Encerramento desconhecido")
      #  sleep(1)

       # system("#exec ~/Sign/config/PID")
