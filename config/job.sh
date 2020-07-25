#!/bin/env bash
# Version: 1.7
# Desceibe: Kill process
# By: Olive

process=`ps`

for proce in $process
do
	echo "kill process"
	kill -9 $proce
done
