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
	mkdir -p configure
	cat Sign.py > configure/Sign
	chmod 700 configure/Sign

	if test -d $PREFIX/lib/python3.7/Sign;then
		sed -i "s|from colors import dict_colors|from Sign.config.colors import dict_colors|g" configure/Sign

		sed -i "s|$ant|$dep|g" configure/Sign

		cd $dir_h
		
		cp -rf * $PREFIX/lib/python3.7/Sign
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
				echo "Sign" >> ~/.profile
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

		if test -e ~/.profile ; then
			for linha in ~/.profile;do
				echo "Sign" >> ~/.profile
				break
			done

		elif test ! -e ~/.profile ; then
			touch ~/.profile
			for linha in ~/.profile;do
				echo "Sign" >> ~/.profile
				break
			done
		fi

	fi
fi
