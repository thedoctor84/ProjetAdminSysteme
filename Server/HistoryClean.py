import sys
import json
import os


if os.path.exists('./state1.txt') :
	monfichier = open("state1.txt", "r")
	contenu = monfichier.read()
	monfichier.close()	

if contenu != '':
	sjson = json.loads(contenu)
	listecpu = sjson["cpu"]
	newlistecpu = listecpu[-20:]
	print newlistecpu

