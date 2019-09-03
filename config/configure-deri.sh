#!/bin/bash
# configure
# 



dir_t=/usr/bin/
dir_der=/usr/bin/

dir_h=~/Sign/

ant='exec /usr/lib/python3.7/Sign/PID'
dep='exec /usr/lib/python3.7/Sign/config/PID'

if [ -d $dir_t ]
then

	cat Sign.py > configure/Sign
	chmod 700 configure/Sign

	if test -d /usr/lib/python3/dist-packages/Sign;then
		sed -i "s|#!/data/data/com.termux/files/usr/bin/env python3|#!/usr/bin/env python3|g" configure/Sign
		sed -i "s|from colors import dict_colors|from Sign.config.colors import dict_colors|g" configure/Sign

		sed -i "s|$ant|$dep|g" configure/Sign

		cd $dir_h
		cp -rf * /usr/lib/python3/dist-packages/Sign
		cd config 
		mv configure/Sign $dir_t

		if test -e ~/.boot; then

			for linha in ~/.boot;do
				echo "Sign" >> ~/.boot
				echo "bash ~/.boot" > ~/.boot_run
				break
			done
		elif test ! -e ~/.boot ; then

			touch ~/.boot

			for linha in ~/.boot;do
				echo "Sign" >> ~/.boot
				echo "bash ~/.boot" > ~/.boot_run
				break
			done
		fi
	

	elif test ! -d /usr/lib/python3/dist-packages/Sign;then
		mkdir -p /usr/lib/python3/dist-packages/Sign
		sed -i "s|#!/data/data/com.termux/files/usr/bin/env python3|#!/usr/bin/env python3|g" configure/Sign
		sed -i "s|from colors import dict_colors|from Sign.config.colors import dict_colors|g" configure/Sign
		sed -i "s|$ant|$dep|g" configure/Sign
		cd $dir_h
		cp -rf * /usr/lib/python3/dist-packages/Sign
		cd config
		mv configure/Sign $dir_t

		if test -e ~/.boot ; then
			
			for linha in ~/.boot;do
				echo "Sign" >> ~/.boot
				echo "bash ~/.boot" > ~/.boot_run
				break
			done
		
		elif test ! -e ~/.boot ; then
			touch ~/.boot
			
			for linha in ~/.boot;do
				echo "Sign" > ~/.boot
				echo "bash ~/.boot" > ~/.boot_run
				break
			done
		fi

	fi


	if [ -e ~/.profile ];then
	
	for linha in ~/.profile;do
		cat ~/.boot_run >> ~/.profile
		break
	done
	else
		echo "Arquivo profile"
		exit 1
	fi
fi
