#!/usr/bin/python
from bs4 import BeautifulSoup
import urllib
import subprocess
import sys
import string

if __name__ == '__main__':

	url='http://www.cert.ssi.gouv.fr/site/cert-fr.rss'
	page = urllib.urlopen(url)
	stre = page.read()

	soup = BeautifulSoup(stre,"lxml" )

	#print(soup.item.text)
	#print soup.find_all('title')

	res = str(soup.find_all('title')).split('<title>')

	msg = res[2].split('</title>')[0]
	msg = string.replace(msg, '\\xe9','e')
	msg = string.replace(msg,':', ' ')

	sys.argv = ['mail.py', msg]
	execfile('mail.py')