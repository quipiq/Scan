# -*- coding: utf-8 -*-

from bliblio import *
import socket

def main():

    print("\n 1 - Scan de cheval de Troie avec IP")
    print("\n 2 - traceroute sur un nom de domaine")
    print("\n 3 - Récupération d'adresse IP avec nom de domaine")
    print("\n 4 - Récupération de la version serveur sur réseau\n")
    demande = input("Veuillez entrer ce que vous voulez faire : ")

    if demande == '1':
        scan()

    elif demande == '2':
        traceroute()

    elif demande == '3':
        get_ip()
        
    elif demande == '4' :
        serveur()

    else :
        print("ERROR : veuillez entrer une valeur correct")

if __name__ == "__main__":
    main()
