# -*- coding: utf-8 -*-

import socket
import win10toast
import requests
from urllib.parse import urlparse
from subprocess import Popen, PIPE
#from webb import webb


def scan():
    toaster = win10toast.ToastNotifier()
    demande = input("Veuillez entrer l'IP : ")
    port = [23432,31337,12349,6667,6969]


    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    x=1
    while x < 255:
        ip = f"{demande}.{x}"

        for i in port:

            try:
                sock.connect((ip, i))
                portco = print(f"{ip} port {i} connecté")
                print(portco)
                print (" try socket.error=",socket.error)
                sock.close()
                toaster.show_toast('Port ouvert',f'{ip} port {i} connecté', duration = 10)
                fichier = open("data.txt", "a")
                fichier.write(f"{ip} port {i} connecté\n")
                fichier.close()

            except socket.error:

                print (" except socket.error=",socket.error)
                print(f"{ip}Port {i} Ferme")


        x = x + 1


def traceroute(*arg):

    url = input("Veuillez entrer le nom de domaine : ")
    while True:
        if 'http' not in url:
            url = "http://" + url
        elif "www" not in url:
            url = "www."[:7] + url[7:]
        else:
            url = url
            break
    url = urlparse(url)
    url = url.netloc
    print(url)
    p = Popen(['tracert', url], stdout=PIPE)
    while True:
        line = p.stdout.readline()
        line2 = str(line).replace('\\r','').replace('\\n','')
        if len(arg)>0:
            file = open(arg[0], "a")
            file.write(line2)
            file.close()
        print(line2)
        if not line:
            break


def get_ip():

    url = input("Veuillez entrer le nom de domaine : ")

    ip = socket.gethostbyname(url)
    print(ip)

    return ip
    
def serveur():
	url = input("Veuillez entrer le nom de domaine : ")
	
	reponse = requests.head(url)

	Head = reponse.headers

	serveur = Head.get("Server")
	print(f"Serveur : {serveur}")
	
