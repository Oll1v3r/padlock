#!/usr/bin/env bash
# os release


release=$(cat /etc/os-release)

for lin in $release;do

	if [ $lin = "ID=ubuntu" ]
	then
		echo "System Ubuntu detected +"
		break
	elif [ $lin = "ID=kali" ]
	then
		echo "System Kali detected +"
		break
	fi

done
