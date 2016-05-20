#!/usr/bin/python
import psutil
import json
	
if __name__ == '__main__':

	cpu = psutil.cpu_percent(2)
	a=str(psutil.virtual_memory())
	total,available,percent,used,free,active,inactive,buffers,cache = a.split(',')
	z,pour_mem = percent.split('=')


	b = str(psutil.disk_usage('/home'))
	d,f,g,h = b.split(',')
	d,v = g.split('=')
	v = float(v)
	disque_libre = v/1000000000
	

	monfichier = open("test.txt", "r")
	contenu = monfichier.read()
	monfichier.close()	

	sjson = json.loads(contenu)

	listed = sjson["disque"]
	listem = sjson["memoire"]
	listec = sjson["cpu"]

	listed.append(disque_libre)
	listem.append(pour_mem)
	listec.append(cpu)


	test2 = json.dumps({"disque" : listed, "cpu" : listec, "memoire" : listem}, sort_keys=True, indent=4, separators=(',', ': '))

	monfichier = open("test.txt", "w")
	monfichier.write(test2)
	monfichier.close()