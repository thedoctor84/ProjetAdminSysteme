#!/usr/bin/python


from Tkinter import *
from ttk import *
import subprocess
import os
import json
import graphe
import urllib


def produit_graph(a):
	
	contenu = ''
	addresse = getAddress(int(a))

	if addresse != '':
		contenu = getStat(addresse)

	if contenu != '':	
		graphe.draw(contenu,addresse)
		top = Toplevel()
		top.title("SVG")
		top.geometry('400x100+500+400')
		msg = Message(top, text= 'Votre Graphe est maintenant present dans le repertoire de travail.',width=350)
		msg.pack()
		button = Button(top, text="Ok", command=top.destroy)
		button.pack(side = BOTTOM)


def getStat(url):
	try:
		page = urllib.urlopen('http://'+url+':8000/state1.txt')
	except IOError:
		return ''
	else:
		stre = page.read()
		return stre

def getConfig(url):
	try:
		page = urllib.urlopen('http://'+url+':8000/constantes.py')
	except IOError:
		return ''
	else:
		stre = page.read()
		return stre

def getNbProcess(url):
	try:
		page = urllib.urlopen('http://'+url+':8000/nombreProcessus.json')
	except IOError:
		return ''
	else:
		stre = page.read()
		return stre

def getNbUsers(url):
	try: 
		page = urllib.urlopen('http://'+url+':8000/UtilisateursConnectes.json')
	except IOError:
		return ''
	else:
		stre = page.read()
		return stre


def getAddress(num):

	if os.path.exists('./listserv.txt') :
		monfichier = open("listserv.txt", "r")
		contenu = monfichier.read()
		monfichier.close()

	if contenu != '':
		sjson = json.loads(contenu)
		listserv = sjson["server"]

	else :
		listserv = []

	if len(listserv) <= num:
		print "pas de serveur"
		return ''
	else:
		return listserv[num][1]

def add_serv(address, top):

	top.destroy()
	contenu = ''

	if os.path.exists('./listserv.txt') :
		monfichier = open("listserv.txt", "r")
		contenu = monfichier.read()
		monfichier.close()	

	if contenu != '':
		sjson = json.loads(contenu)
		listserv = sjson["server"]

	else :
		listserv = []

	for ip in listserv:
		if ip[1] == address:
			return

	z = (len(listserv),address)
	listserv.append(z)
	data = json.dumps({"server" : listserv}, sort_keys=True, indent=4, separators=(',', ': '))
	monfichier = open("listserv.txt", "w")
	monfichier.write(data)
	monfichier.close()

def ajout_serv():

	top = Toplevel()
	top.title("Add Server")
	top.geometry('400x100+500+400')
	E = Entry(top)
	E.grid(row = 0, column = 1, pady = 30)
	lab = Label(top, text = "Ip Address : ")
	lab.grid(row = 0, column = 0)
	ajout = Button(top, text = 'Add', command = lambda : add_serv(E.get(), top), width = 20)
	ajout.grid(row = 0, column = 2)


def config(a):

	addresse = getAddress(int(a))
	temp = getConfig(addresse)
	monfichier = open("temp.txt", "w")
	monfichier.write(temp)
	monfichier.close()
	subprocess.call(["vi","temp.txt"])
	arg = 'netcat ' + addresse + ' 8001 < temp.txt'

	process = subprocess.Popen(arg, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	err = process.stderr.read()
	print str(err)

def onglet(a) : 

	SERVER = a
	contenu = ''
	addresse = getAddress(int(a))


	lf = LabelFrame(MainMenu, text='Data Server ' + str(addresse))
	lf.grid(row = 2, column = 0, columnspan = 4, pady = 1)

	if addresse != '':
		contenu = getStat(addresse)
	

	if contenu == '':
		cpu = Label(lf, text = 'Cpu : ' + '-- ' + '%')
		cpu.grid(row = 0, column = 0, padx = 76, pady = 10)

		memory = Label(lf, text = 'Memory : '  + '-- ' + '%')
		memory.grid(row = 0, column = 1, padx = 76, pady = 10)

		nr = Label(lf, text = 'Download : ' + '-- ' + 'MB')
		nr.grid(row = 1, column = 0 , padx = 76, pady = 10)

		ns = Label(lf, text = 'Upload : ' + '-- ' + 'MB')
		ns.grid(row = 1, column = 1 , padx = 76, pady = 10)

		dw = Label(lf, text = ' NB Disk Write : ' + '--')
		dw.grid(row = 2, column = 0 , padx = 76, pady = 10)

		dr = Label(lf, text = 'NB Disk Read : ' + '--')
		dr.grid(row = 2, column = 1 , padx = 76, pady = 10)
		

	if contenu != '':
		try:
			sjson = json.loads(contenu)
		except ValueError:
			cpu = Label(lf, text = 'Cpu : ' + '-- ' + '%')
			cpu.grid(row = 0, column = 0, padx = 76, pady = 10)

			memory = Label(lf, text = 'Memory : '  + '-- ' + '%')
			memory.grid(row = 0, column = 1, padx = 76, pady = 10)

			nr = Label(lf, text = 'Download : ' + '-- ' + 'MB')
			nr.grid(row = 1, column = 0 , padx = 76, pady = 10)

			ns = Label(lf, text = 'Upload : ' + '-- ' + 'MB')
			ns.grid(row = 1, column = 1 , padx = 76, pady = 10)

			dw = Label(lf, text = ' NB Disk Write : ' + '--')
			dw.grid(row = 2, column = 0 , padx = 76, pady = 10)

			dr = Label(lf, text = 'NB Disk Read : ' + '--')
			dr.grid(row = 2, column = 1 , padx = 76, pady = 10)
		else:

			listem = sjson["memoire"]
			listec = sjson["cpu"]
			listen = sjson["network_sent"]
			listenr = sjson["network_received"]
			listedr = sjson["disk_read"]
			listedw = sjson["disk_write"]

			cpu = Label(lf, text = 'Cpu : ' + str(listec[-1][-1]) + '%')
			cpu.grid(row = 0, column = 0, padx = 62, pady = 10)

			memory = Label(lf, text = 'Memory : '  + str(listem[-1][-1]) + '%')
			memory.grid(row = 0, column = 1, padx = 62, pady = 10)

			nr = Label(lf, text = 'Download : ' + str(listenr[-1][-1]) + 'MB')
			nr.grid(row = 1, column = 0 , padx = 62, pady = 10)

			ns = Label(lf, text = 'Upload : ' + str(listen[-1][-1]) + 'MB')
			ns.grid(row = 1, column = 1 , padx = 62, pady = 10)

			dw = Label(lf, text = ' NB Disk Write : ' + str(listedw[-1][-1]))
			dw.grid(row = 2, column = 0 , padx = 62, pady = 10)

			dr = Label(lf, text = 'NB Disk Read : ' + str(listedr[-1][-1]))
			dr.grid(row = 2, column = 1 , padx = 62, pady = 10)


	contenu = ''
	contenu = getNbProcess(addresse)

	if contenu == '':
		process = Label(lf, text = 'NB Processes : -- ')
		process.grid(row = 3, column = 0, padx = 60, pady = 20)

	else:
		try:
			sjson = json.loads(contenu)
		except ValueError:
			process = Label(lf, text = 'NB Processes : -- ')
			process.grid(row = 3, column = 0, padx = 60, pady = 20)
		else:
			listepr = sjson["infos_processus"]
			process = Label(lf, text = 'NB Processes : ' + str(listepr[-1][-1]))
			process.grid(row = 3, column = 0, padx = 60, pady = 20)
	
	contenu = ''
	contenu = getNbUsers(addresse)

	if contenu == '':
		usr = Label(lf, text = 'Nb Users :  -- ')
		usr.grid(row = 3, column = 1, padx = 60, pady = 20)
	else :	
		try:
			sjson = json.loads(contenu)
		except ValueError:
			usr = Label(lf, text = 'Nb Users :  -- ')
			usr.grid(row = 3, column = 1, padx = 60, pady = 20)
		else:
			listeusr = sjson["info_nombre_utilisateurs"]
			usr = Label(lf, text = 'Nb Users : ' + str(listeusr[-1][-1]))
			usr.grid(row = 3, column = 1, padx = 60, pady = 20)


	lf2 = LabelFrame(MainMenu, text = 'Actions')
	lf2.grid(row = 3, column = 0, columnspan = 4, pady = 5)

	bouton_graphique = Button(lf2, text = 'Produce graphic', command = lambda: produit_graph(SERVER), width = 10)
	bouton_graphique.grid(row = 3, column = 0, padx = 10, pady = 10)

	bouton_config = Button(lf2, text = 'Config', command = lambda: config(SERVER), width = 10)
	bouton_config.grid(row = 3, column = 1, padx = 10, pady = 10)

	bouton_ajout = Button(lf2, text = 'Add Server', command = ajout_serv, width = 10)
	bouton_ajout.grid(row = 3, column = 2, padx = 10, pady = 10)

	bouton_refresh = Button(lf2, text = 'Refresh', command = lambda: onglet(SERVER), width = 10)
	bouton_refresh.grid(row = 3, column = 3, padx = 10, pady = 10)

	

fenetre  = Tk()
fenetre.title('CheckServ')
fenetre.geometry('550x350+450+350')
fenetre.resizable(width = False, height = False)

MainMenu = Frame(fenetre)
MainMenu.pack()

lf3 = LabelFrame(MainMenu, text = 'Select Server')
lf3.grid(row = 1, column = 0, columnspan = 4, pady = 5)

num_serv = Label(lf3, text = 'Server : ')
num_serv.grid(row = 0, column = 0, pady = 5, padx = 20)

E1 = Entry(lf3)
E1.grid(row = 0, column = 1, pady = 5, padx = 20)

bouton_display = Button(lf3, text = 'Display', command = lambda: onglet(E1.get()))
bouton_display.grid(row = 0, column = 2, pady = 5, padx = 20)



onglet(0)

fenetre.mainloop()