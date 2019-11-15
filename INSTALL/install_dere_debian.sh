#!/usr/bin/env bash
# install
#

if [ ! -e /data/data/com.termux/lib/libtermux.so ]
then

clear
echo Please wait...
(apt-get update && apt-get install ncurses-utils -y) &> /dev/null

echo "Identifying Linux operating system"
sleep 2
bash ../config/os-ident.sh
sleep 3
ar=( '█■■■■' '■█■■■' '■■█■■' '■■■█■' '■■■■█' '█■■■■' '■█■■■' '■■█■■' '■■■█■' '■■■■█' )

spin() {
clear
for i in ${ar[@]}
do
    tput civis
    tput cup 10
    echo -ne "\rPlease wait... [$i]"
    sleep 0.1
done
tput cup 10
echo -ne "Please wait... [Done ]"
sleep 1
tput cnorm
}
spin
echo ""

sleep 1
clear
tput cup 5
tput civis
echo -e "\033[00;92m\rPlease wait... Installing packages \033[0m[\033[00;93mNone\033[0m]"

(apt-get update && apt-get install toilet figlet python3 -y) &> /dev/null
tput civis
tput cup 5
echo -e "\033[00;92m\rPlease wait... Installing packages \033[0m[\033[00;93mDone\033[0m]"
sleep 1

tput cnorm
cd ..
echo -e "\n\nrun '\033[00;92mpython3 ./sign.py\033[0m' or '\033[00;92mpython3 sign.py\033[0m'\n"

else
	echo "Undetected debian derivative"
fi
