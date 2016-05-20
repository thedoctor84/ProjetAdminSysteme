#!/bin/bash

UtilisateursNb=`users | xargs -n1 | uniq | wc -w`

echo "Nombre d'utilisateurs connectés : $UtilisateursNb"

if [ ! -f UtilisateursConnectes.json ]
then
	touch UtilisateursConnectes.json
	echo "{" >> UtilisateursConnectes.json
	echo "	\"info_nombre_utilisateurs\":[" >> UtilisateursConnectes.json
	echo "		{\"date\":\"`date`\", \"nombre_utilisateurs\":${UtilisateursNb}}," >> UtilisateursConnectes.json
	echo "	]" >> UtilisateursConnectes.json
	echo "}" >> UtilisateursConnectes.json
else
	echo "`head -n -2 UtilisateursConnectes.json`" > UtilisateursConnectes.json
	echo "		{\"date\":\"`date`\", \"nombre_utilisateurs\":${UtilisateursNb}}," >> UtilisateursConnectes.json
	echo "	]" >> UtilisateursConnectes.json
	echo "}" >> UtilisateursConnectes.json
fi
