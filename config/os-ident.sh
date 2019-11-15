#!/usr/bin/env bash
# identificador de sistema operacional linux
# versao: beta 0.0



FILE=/data/data/com.termux/lib/libtermux.so


if [ ! -e ${FILE} ]
then

file="$(cat /etc/os-release)"

for lin in $file
do
	case $lin in
		
		'NAME="Ubuntu"')
			# echo "Ubuntu detected [+]"
			# ubuntu=$lin

			for linn in $file
			do
				if [ $linn = 'VERSION_ID="18.04"' ]
				then
					# echo "Version 18.04"

					for linnn in $file
					do
						if [ $linnn = 'VERSION_CODENAME=bionic' ]
						then
							echo "Ubuntu Bionic Version 18.04 detected [+]"
						fi
					done
				fi
			done;;

		'NAME="Debian"')
			echo "Debian detected [+]"
			# debian=$lin
			;;
		'NAME="Kali"')
			echo "Kali detected [+]"
			# kali=$lin
			;;
		'NAME="Parrot"')
			echo "Parrot detected [+]"
			# parrot=$lin
			;;
		*)
	esac
done

elif [ -e ${FILE} ]
then
	echo "Termux Detected [+]"

else
	echo "Error !"
fi
