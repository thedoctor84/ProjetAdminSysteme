#!/bin/bash

ProcessNb=`ps -aux | wc -l`

#echo "Nombre de processus : $ProcessNb"

if [ ! -f nombreProcessus.json ]
then
	touch nombreProcessus.json
	echo "{" >> nombreProcessus.json
	echo "	\"infos_processus\":[" >> nombreProcessus.json
	echo "		{\"date\":\"`date`\", \"nombre_processus\":${ProcessNb}}," >> nombreProcessus.json
	echo "	]" >> nombreProcessus.json
	echo "}" >> nombreProcessus.json
else
	echo "`head -n -2 nombreProcessus.json`" > nombreProcessus.json
	echo "		{\"date\":\"`date`\", \"nombre_processus\":${ProcessNb}}," >> nombreProcessus.json
	echo "	]" >> nombreProcessus.json
	echo "}" >> nombreProcessus.json
fi



