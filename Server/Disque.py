#!/usr/bin/python
import subprocess

diskspace = "df"
diskspace_arg = "-h"
print "Recuperation des informations sur les disques with %s command:\n" %diskspace
subprocess.call([diskspace, diskspace_arg])
