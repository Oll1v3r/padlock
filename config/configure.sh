
if test ! -d $PREFIX/lib/python3.8/Sign-Ultimate;then
echo "Erro ao executar, primeiro configure o login"
exit
else
if test -e $HOME/.bashrc
then
	echo "mod" >> $HOME/.bashrc
else
	touch $HOME/.bashrc
	echo "mod" >> $HOME/.bashrc
fi
cat ->> .log-sign <<- end
cd $HOME && cd Sign-Ultimate && cd config && python3 verify.py
end

file=`cat $HOME/.bashrc`

for line in $file
do
	case $line in
		"mod")
			mv .log-sign $HOME/
			sed -i "s|mod|bash $HOME/.log-sign|g" $HOME/.bashrc;;
		*)
			exit
	esac
done
fi
