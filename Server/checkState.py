#!/usr/bin/python
import psutil
import json
import time
import os
import datetime
from constantes import *
import sys
	
if __name__ == '__main__':

	cpu = psutil.cpu_percent(2)
	mem =	psutil.virtual_memory()
	network = psutil.net_io_counters()
	disque = psutil.disk_io_counters()

	pour_mem = mem.percent
	network_sent = network.bytes_sent / 1000000
	network_received = network.bytes_recv / 1000000
	disk_write = disque.write_count
	disk_read = disque.read_count
	
	#date = time.strftime("%A %d %B %Y %H:%M:%S")
	date = unicode(datetime.datetime.now())
	contenu = ''
	
	if os.path.exists('./state1.txt') :
		monfichier = open("state1.txt", "r")
		contenu = monfichier.read()
		monfichier.close()	

	if contenu != '':
		sjson = json.loads(contenu)
		listem = sjson["memoire"]
		listec = sjson["cpu"]
		listen = sjson["network_sent"]
		listenr = sjson["network_received"]
		listedr = sjson["disk_read"]
		listedw = sjson["disk_write"]

	else :
		listem = []
		listec = []
		listen = []
		listenr = []
		listedr = []
		listedw = []

	z = (date, pour_mem)
	x = (date, cpu)
	y = (date, network_sent)
	w = (date, network_received)
	v = (date, disk_read)
	u = (date, disk_write)

	listem.append(z)
	listec.append(x)
	listen.append(y)
	listenr.append(w)
	listedr.append(v)
	listedw.append(u)


	data = json.dumps( {"cpu" : listec, "memoire" : listem, "network_sent" : listen, "network_received" : listenr, "disk_read" : listedr, "disk_write" : listedw}, sort_keys=True, indent=4, separators=(',', ': '))

	monfichier = open("state1.txt", "w")
	monfichier.write(data)
	monfichier.close()


	if cpu >= CPU_ALERTE :
		sys.argv = ['mail.py', 'Le cpu est actuellement a ' + str(cpu) + '% de charge']
		execfile('mail.py')

	if pour_mem >= MEM_ALERTE :
		sys.argv = ['mail.py', 'La memoire est actuellement a ' + str(mem) + '% de charge']
		execfile('mail.py')