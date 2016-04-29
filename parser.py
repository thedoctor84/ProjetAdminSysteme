#!/usr/bin/python
from bs4 import BeautifulSoup
import urllib


url='http://www.cert.ssi.gouv.fr/site/cert-fr.rss'
page = urllib.urlopen(url)
stre = page.read()

soup = BeautifulSoup(stre,"lxml" )

print(soup.get_text())