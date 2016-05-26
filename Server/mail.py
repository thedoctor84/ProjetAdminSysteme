import smtplib
import sys
from constantes import *



if len(sys.argv) != 2:
	print("pas assez d'arguments")
	sys.exit(1)


server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('alerte.test.yo@gmail.com','motdepasse123')


msg=sys.argv[1]
msg = "Subject: ALERTE SECURITE\n" + msg

server.sendmail('alert.test.yo@gmailcom', MAILALRT, msg)
server.quit()