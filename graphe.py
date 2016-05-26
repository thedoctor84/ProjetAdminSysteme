#!/usr/bin/python
import psutil
import json
import pygal
import os
import sys
import datetime



def draw(contenu,addresse):


	sjson = json.loads(contenu)

	liste_memoire = sjson["memoire"]
	liste_cpu = sjson["cpu"]
	liste_network = sjson["network_received"]
	liste_network_send = sjson["network_sent"]

	liste_network_good_date = []
	liste_networks_good_date = []   # on remet les dates sous le type datetime
	liste_cpu_good_date = []
	liste_mem_good_date = []

	for item in liste_network:
		z = (datetime.datetime.strptime(item[0], '%Y-%m-%d %H:%M:%S.%f'),item[1])
		liste_network_good_date.append(z)

	for item in liste_network_send:
		z = (datetime.datetime.strptime(item[0], '%Y-%m-%d %H:%M:%S.%f'),item[1])
		liste_networks_good_date.append(z)

	for item in liste_cpu:
		z = (datetime.datetime.strptime(item[0], '%Y-%m-%d %H:%M:%S.%f'),item[1])
		liste_cpu_good_date.append(z)

	for item in liste_memoire:
		z = (datetime.datetime.strptime(item[0], '%Y-%m-%d %H:%M:%S.%f'),item[1])
		liste_mem_good_date.append(z)

	dateline = pygal.DateTimeLine(x_label_rotation=35)
	dateline.add("MB Recus", liste_network_good_date)
	dateline.add("MB Envoyes", liste_networks_good_date)
	dateline.add("% CPU", liste_cpu_good_date)
	dateline.add("% Memoire", liste_mem_good_date)
	dateline.render_to_file('graphe'+addresse+'.svg')
