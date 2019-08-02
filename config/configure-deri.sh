#!/bin/bash
# configure
# 



dir_t=/usr/bin/
dir_der=/usr/bin/

dir_h=~/Sign/

ant='exec /var/lib/python3.7/Sign/PID'
dep='exec /var/lib/python3.7/Sign/config/PID'

if [ -d $dir_t ]
then
	cat Sign.py > configure/Sign
	chmod 700 configure/Sign

	if test -d /var/lib/python3.7/Sign;then
		sed -i "s|from colors import dict_colors|from Sign.config.colors import dict_colors|g" configure/Sign

		sed -i "s|$ant|$dep|g" configure/Sign

		cd $dir_h
		
		cp -rf * /var/lib/python3.7/Sign
		cd config 
		mv configure/Sign $dir_t
		if test -e ~/.profile ; then

			for linha in ~/.profile;do
				echo "Sign" >> ~/.profile
				break
			done
		elif test ! -e ~/.profile ; then

			touch ~/.profile

			for linha in ~/.profile;do
				echo "Sign" > ~/.profile
				break
			done
		fi
	

	elif test ! -d /var/lib/python3.7/Sign;then
		mkdir -p /var/lib/python3.7/Sign
		sed -i "s|from colors import dict_colors|from Sign.config.colors import dict_colors|g" configure/Sign
		sed -i "s|$ant|$dep|g" configure/Sign
		cd $dir_h
		cp -rf * /var/lib/python3.7/Sign
		cd config
		mv configure/Sign $dir_t

		if test -e ~/.profile ; then
			
			for linha in ~/.profile;do
				echo "Sign" >> ~/.profile
				break
			done
		
		elif test ! -e ~/.profile ; then
			touch ~/.profile
			
			for lonha in ~/.profile;do
				echo "Sign" > ~/.profile
				break
			done
		fi

	fi
fi
