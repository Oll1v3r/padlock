#!/bin/bash
# configure
# 



dir_t=/data/data/com.termux/files/usr/bin/
dir_der=/usr/bin/

dir_h=/data/data/com.termux/files/home/Sign/

ant='exec /data/data/com.termux/files/usr/lib/python3.7/Sign/PID'
dep='exec /data/data/com.termux/files/usr/lib/python3.7/Sign/config/PID'

if [ -d $dir_t ]
then
	cat Sign.py > configure/Sign
	chmod 700 configure/Sign

	if test -d $PREFIX/lib/python3.7/Sign;then
		sed -i "s|from colors import dict_colors|from Sign.config.colors import dict_colors|g" configure/Sign

		sed -i "s|$ant|$dep|g" configure/Sign

		cd $dir_h
		
		cp -rf * $PREFIX/lib/python3.7/Sign
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
				echo "Sign" >> ~/.bashrc
				echo "bash ~/.boot" > ~/.boot_run
				break
			done
		fi
	

	elif test ! -d $PREFIX/lib/python3.7/Sign;then
		mkdir -p $PREFIX/lib/python3.7/Sign
		sed -i "s|from colors import dict_colors|from Sign.config.colors import dict_colors|g" configure/Sign
		sed -i "s|$ant|$dep|g" configure/Sign
		cd $dir_h
		cp -rf * $PREFIX/lib/python3.7/Sign
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

	fi

	if [ -e ~/.bashrc ]
	then
		for linha in ~/.bashrc;do
			cat ~/.boot_run >> ~/.bashrc
			break
		done
	elif [ ! -e ~/.bashrc ]
	then
		touch ~/.bashrc

		for linha in ~/.bashrc;do
			cat ~/.boot_run >> ~/.bashrc
			break
		done
		
	fi
fi
