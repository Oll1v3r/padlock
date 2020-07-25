
if test ! -d $PREFIX/lib/python3.8/Sign-Ultimate;then

	echo "Erro ao executar, primeiro configure o login"
	exit

else
	if test -e $HOME/.bashrc
	then
	echo "mod" >> $HOME/.bashrc
	cat ->> .log-sign <<- end
	cd $HOME && cd Sign-Ultimate && cd config && python3 verify.py
	end
	file=`cat $HOME/.bashrc`
			
	for line in $file # inicio do loop
	do
	case $line in # inicio do case
	"mod")
	mv .log-sign $HOME/
	sed -i "s|mod|bash $HOME/.log-sign|g" $HOME/.bashrc;;
	*)
	exit
	esac # fim do case
	done # fim do loop
	else

	touch $HOME/.bashrc
	echo "mod" >> $HOME/.bashrc
	cat ->> .log-sign <<- end
	cd $HOME && cd Sign-Ultimate && cd config && python3 verify.py
	end

	file=`cat $HOME/.bashrc`

	for line in $file # inicio do loop
	do
	case $line in # inicio do case
	"mod")
	mv .log-sign $HOME/
	sed -i "s|mod|bash $HOME/.log-sign|g" $HOME/.bashrc;;
	*)

	exit
	esac # fim do case
	done # fim do loop
	fi # fim da condicao if interna

fi # da condicao if
