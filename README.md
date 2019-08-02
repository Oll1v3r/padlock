# Sign 'Login do ambiente 'termux os'


[Image description](https://raw.githubusercontent.com/Olliv3r/Sign/master/config/img/logo1.png)

 
Instalação
----


pkg update

pkg upgrade

pkg install git

cd ~

git clone https://github.com/Olliv3r/Sign.git

cd Sign

bash install

Conclui
-----




Login padrão
----


O login por padrão vem com usuario 'oliveobom205' e senha 'modoeviilo205'



configure seu login:
----



Comandos para configurar o login
-----

Uso:
------
	python3 sign.py --setup-login=OS


Para remover a configuração de login
-----

Uso:
------
	python3 sign.py --remove-login=OS




Exemplo: 
-----


Configurar login para ambiente 'termux'
------

	python3 sign.py --setup-login=termux

configurar para derivados do debian
------

	python3 sign.py --setup-login=debian
