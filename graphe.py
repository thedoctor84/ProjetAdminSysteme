#!/usr/bin/python
import psutil
import json
import pygal



if __name__ == '__main__':

	monfichier = open("test.txt", "r")
	contenu = monfichier.read()
	monfichier.close()

	sjson = json.loads(contenu)

	liste_disque = sjson["disque"]
	liste_memoire = sjson["memoire"]
	liste_cpu = sjson["cpu"]

	print liste_disque

	graphe = pygal.Bar()
	graphe.add('CPU',liste_cpu)
	graphe.add('Disque',liste_disque)
	graphe.render_to_file('cpu.svg')
