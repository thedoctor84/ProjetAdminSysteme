#!/usr/bin/python
from bs4 import BeautifulSoup
import urllib


url='http://www.cert.ssi.gouv.fr/site/cert-fr.rss'
page = urllib.urlopen(url)
stre = page.read()

soup = BeautifulSoup(stre,"lxml" )

#print(soup.item.text)

#print soup.find_all('title')

res = str(soup.find_all('title')).split('<title>')

print res[2].split('</title>')[0]