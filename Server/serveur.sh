#!/bin/bash

i=1

while [ "$i" -eq 1 ]
do
	nc -l -p 8001 > temp.txt
	cat temp.txt > constantes.py
	
done