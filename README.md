# Sign Login para sistema TERMUX ou derivados do DEBIAN


![Image description](https://github.com/Oll1v3r/Sign/raw/master/config/img/login.png)

 
Instalação
----


pkg update

pkg upgrade

pkg install git

cd ~

git clone https://github.com/Oll1v3r/Sign

cd Sign

bash install


Instalando no derivados do debian
----
	cd Sign
	cd INSTALL
	./install_dere_debian.sh

Instalando no android (TERMUX
----
	cd Sign
	cd INSTALL
	./install

Teste o script login antes de configurar login
----
	python3 sign.py --view-login=login


Verifique sistemas disponiveis
----
	python3 sign.py --list=dd


Verifique que sistema possui
----
	python3 sign.py --indent-os=os

Login padrão
----
	*O login por padrão vem com usuario 'oliveobom205' e senha 'modoeviilo205'



configure seu login: Comandos para configurar o login
-----


Uso:
-----
	python3 sign.py --setup-login=OS



Para remover a configuração de login
-----

Uso:
------
	python3 sign.py --remove-login=OS



Exemplo: Configurar login para ambiente 'termux'
------

	python3 sign.py --setup-login=termux

configurar para derivados do debian
------

	python3 sign.py --setup-login=debian


Remover configuracao do sistema
-----

Uso:
-----
	python3 sign.py --remove-login=OS



Exemplo: remover configuração do ambiente termux
-----
	python3 sign.py --remove-login=termux


Exemplo: remover configuração do ambiente derivados do debian
-----
	python3 sign.py --remove-login=debian



Sistemas disponíveis
-----
	### 1 Ubuntu
	### 2 Debian
	### 3 Kali
	### 4 Parrot
