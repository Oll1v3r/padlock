#!/usr/bin/env bash
# identificador de sistema operacional linux
# versao: beta 0.0



FILE=/data/data/com.termux/lib/libtermux.so


if [ ! -e ${FILE} ]
then

file="$(cat /etc/*release | grep PRETTY | cut -c14-20)"

for lin in $file
do
	case $lin in
		
		Ubuntu)
			echo "Detected Operational System Ubuntu GNU/Linux [+]"
			;;

		Debian)
			echo "Detected Operational System Debian GNU/Linux [+]"
			;;

		Kali)
			echo "Detected Operational System Kali GNU/Linux [+]"
			;;

		Parrot)
			echo "Detected Operational System Parrot GNU/Linux [+]"
			;;
		*)
	esac
done

elif [ -e ${FILE} ]
then
	echo "Detected Operational System Termux[+]"

else
	echo "Error !"
fi
