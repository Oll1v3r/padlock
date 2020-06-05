#!/bin/env bash


process=`ps`

for proce in $process
do
	kill -9 $proce
done
