# padlock
padlock - sistema de login para distribuiçôes Linux: em forma de janela gráfica. AVISO! é um aplicativo beta
----
### Painel de acesso:
![Image description](https://github.com/Oll1v3r/padlock/blob/master/src/media/painel-1.png)

### Painel em processo:
![Image description](https://github.com/Oll1v3r/padlock/blob/master/src/media/painel-2.png)

### Script para cadastro:

![Image description](https://github.com/Oll1v3r/padlock/blob/master/src/media/setupRegister.png)

### Resultado do cadastro:

![Image description](https://github.com/Oll1v3r/padlock/blob/master/src/media/setupRegistered.png)

----
### Modo de uso do script:

----

##### Opçôes:

##### Permite testar o sistema antes de aplicar a configuração cadastrada
> --test
#### Define um sistema operacional linux para ser configurado
> --setup
#### Desfaz a configuração aplicada anteriormente com o --setup
> --undo
#### Identifica shell rodando atualmente
> --shell

----
### Exemplos:

#### Testar o sistema
> ./padlock.py --test

#### Termux
> ./padlock.py --setup termux

#### Ubuntu ou derivados
> ./padlock.py --setup ubuntu

#### Identificar shell
> ./padlock.py --shell
----

@ Copyright [Oliver] (https://github.com/Olliv3r/), [Tecnospeed] (https://tecnospeed.000webhostapp.com) 2020
