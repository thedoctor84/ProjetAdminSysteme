import sys
import json
import os
from constantes import *


if os.path.exists('./state1.txt') :
	monfichier = open("state1.txt", "r")
	contenu = monfichier.read()
	monfichier.close()	

if contenu != '':
	sjson = json.loads(contenu)
	listecpu = sjson["cpu"]
	newlistecpu = listecpu[-NB_VAL:]
	listedr = sjson["disk_read"]
	newlistedr = listedr[-NB_VAL:]
	listedw = sjson["disk_write"]
	newlistedw = listedw[-NB_VAL:]
	listem = sjson["memoire"]
	newlistem = listem[-NB_VAL:]
	listenr = sjson["network_received"]
	newlistenr = listenr[-NB_VAL:]
	listens = sjson["network_sent"]
	newlistens = listens[-NB_VAL:]

	data = json.dumps( {"cpu" : newlistecpu, "memoire" : newlistem, "network_sent" : newlistens, "network_received" : newlistenr, "disk_read" : newlistedr, "disk_write" : newlistedw}, sort_keys=True, indent=4, separators=(',', ': '))


	monfichier = open("state1.txt", "w")
	monfichier.write(data)
	monfichier.close()

contenu = ''

if os.path.exists('./nombreProcessus.json') :
	monfichier = open("nombreProcessus.json", "r")
	contenu = monfichier.read()
	monfichier.close()


if contenu != '':
	sjson = json.loads(contenu)
	listepr = sjson["infos_processus"]
	newlistepr = listepr[-NB_VAL:]
	data = json.dumps( {"infos_processus" : newlistepr}, sort_keys=True, indent=4, separators=(',', ': '))

	monfichier = open("./nombreProcessus.json", "w")
	monfichier.write(data)
	monfichier.close()

contenu = ''

if os.path.exists('./UtilisateursConnectes.json') :
	monfichier = open("UtilisateursConnectes.json", "r")
	contenu = monfichier.read()
	monfichier.close()


if contenu != '':
	sjson = json.loads(contenu)
	listenbusr = sjson["info_nombre_utilisateurs"]
	newlistenbusr = listenbusr[-NB_VAL:]
	data = json.dumps( {"info_nombre_utilisateurs" : newlistenbusr}, sort_keys=True, indent=4, separators=(',', ': '))

	monfichier = open("UtilisateursConnectes.json", "w")
	monfichier.write(data)
	monfichier.close()