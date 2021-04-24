# Scan
C'est un petit programme permettant de récupéré l'IP d'un site a partir de son url, d'avoir la version du serveur qui héberge le site, de faire un traceroute a une IP et de faire un scan de cheval de troie sur un réseau.

# A quoi sert-il?
Ce programme va permettre de facilité des actions principalement orienté web (sauf le scan de cheval de troie sur un réseau). Vous n'avez qu'a lancé le programme et choisir votre options. Une fois cela fait vous avez juste a suivre ce que le programme vous demande. Il reste très simpliste mais suffit largement.

# téléchargements
Vous avez juste a télécharger le dossier et à bien faire attention de mettre la [bibliotheque.py](https://github.com/quipiq/Scan/blob/main/bliblio.py) et le [main.py](https://github.com/quipiq/Scan/blob/main/main.py) dans le même dossier ou alors changer le chemin dans le programme.

# Les différentes options

## Le scan de cheval de troie sur réseau

### Comment sa marche ? 

La bibliothèques requise pour cette fonction est les [socket](https://pypi.org/project/sockets/).
Installation : `pip3 install socket`

Nous allons nous servir des ports ouvert sur le pare-feu d'un réseau. 

Tout d'abord qu'est ce que sont les ports et comment marchent-ils.
Votre pare-feu sert a protéger votre réseau. Pour cela il va ouvrir ou fermer certaine "porte d'accès" appelée ports. Le pare-feu est constituer de 65 535 ports dont les 1024 premiers sont utiliser pour des protocoles spécifique (20 = TCP, 80 = HTTP,  22 = SSH etc...).

 Pour faire des scans les 1024 premiers ne vont pas forcément être intéressant sauf si l'on veut récupérer la version du serveur derrière. La particularité de ces ports est de base pour une connexion de l'extérieur tout les ports au dessus de 1024 vont être fermé. Mais le plus intéressant est que de l'intérieur l'information peut sortir de n'importe qu'elle ports.

Example : 

![connexion_exterieur](https://user-images.githubusercontent.com/72353621/115956947-fe993000-a4ff-11eb-975a-cc4ef3a5e18e.png)


Sur cette exemple la connexion vient de l'extérieur sur un port fermé par défaut car au dessus de 1024. Cette essaie de connexion sera donc refusé par le pare-feu.


Si nous reprenons l'exemple du dessus mais cette fois si en changeait de sens la requête. C'est a dire de l'intérieur vers l'extérieur.

```mermaid
graph LR
A[Réseau local] -- test connexion --> B{{Pare-feux port: 45 300}}
B --> c[Serveur distant]
```

Par défaut toute les connexions de l'intérieur a l'extérieur sont autorisé. Donc cette connexion marchera. 

Voici le principe grossièrement expliquer des chevaux de Troie sur lequel on va s'appuyer pour faire le scan. Le cheval de Troie va rentré dans votre réseau d'un moyen ou d'un autre, une fois dans votre réseau il ouvrira pas une manière ou une autre un port de base fermer (au dessus de 1024). 

Une fois cela fait il ne reste plus qu'à se connecter au port et le tour est jouer. Mais ce programme ne permet pas de faire un de ces chevaux de Troie mais de scanner les potentiel réseau infecter part un de ces chevaux de Troie qui aurait ouvert un port.

Pour cela on va entrez une plage d'IP à scanner (exemple : Si l'on rentrer 198.235.145.1 le scan commencera par cette IP et finira par l'IP 198.235.145.255) Nous mettons dans un tuple au début les ports que des chevaux de Troie connut ouvre. Vous pouvez allez voir sur ce [site](https://docs.trendmicro.com/all/ent/officescan/v10.6/fr-fr/osce_10.6_sp3_client_olh/osce_topics/what_are_trojan_ports_.htm). Il existe plein d'autres sites comme sa, a vous de chercher.  SI on prend l'exemple du tuple du programme que je vous mets a disposition les ports a scanner que j'ai mit sont : 

    port = [23432,31337,12349,6667,6969]

Je n'ai pas mit une liste trop longue mais vous pouvez en rajouter et en enlevé a votre guise. 

 Prenons pour exemple un bout de scan sur l'IP 198.235.145.165:
 
 
 
 ![Diagramme vierge](https://user-images.githubusercontent.com/72353621/115940447-e98db400-a4a1-11eb-9fcd-219d0def3029.png)
 


Pour améliorer un peut se programme j'ai rajouter deux options, une qui va mettre dans un fichier texte tout les IP avec le numéros de port ouvert. Et une autre qui va afficher une notification sur votre PC avec le l'IP et le numéro de port ouvert. Attention cette dernière option n'est disponible que sur Windows, elle n'existe pas sur linux et sur mac os ou sous un autre nom. Ces options vous permettrons de faire des scans de plusieurs heures sans avoir a rester devant votre PC. 

Libre a vous de changer le programme pour faire des scans précis avec un objectifs précis.

### Utilisation
 Il faudra juste mettre les trois premiers nombres de l'IP (exemple : pour faire un scan a partir de l'IP 198.235.145.1 je mettrai 192.235.145). Pas besoin de mettre le point ni le dernier nombre sinon le programme va vous marquez une erreur.

## Récupération d'IP à partir d'url (nom de domaine) 

### Comment sa marche ? 

Ce programme va servir a récupérer l'IP d'un site. Je ne peut pas vraiment détaillé comment sa marche car c'est juste une fonction des sockets qui va me le permettre. Mais une fois l'IP récupéré elle nous servira pour savoir la version du serveur qui héberge le site web pour trouver des failles potentielles et faire une attaque.

## Récupération de la version du serveur web

### Comment sa marche ? 

Se programme va nous renvoyer la versions du serveur web d'un site. 

Pour avoir ces infos il faut ce pencher sur le Head des sites. Attention a ne pas confondre, je ne parle pas du Head qui se trouve dans le html mais d'un autre Head. C'est un peut le même principe, il contient des infos sur le site et sur le serveur web. Toute ces infos seront contenues dans un dictionnaire qui contient les même infos pour tout les sites. 

Nous allons donc faire une requêtes aux site pour qu'il nous renvoies ces infos, c'est ce que l'on appelle un requête web. Il en existe plein différente, mais dans ce programme je vais utiliser que celle la.

En python les dictionnaire sont constituer d'une clef a laquelle on va assigner une valeur. Une fois cela fait on peut faire des recherches dans le dictionnaire par clef.

Voici un exemple simple d'un dictionnaire reçus avec une requête web : 


|clefs                         |valeur                        |
|-------------------------------|-----------------------------|
|date                           |Fri, 23 Apr 2021 23:27:11 GMT|
|age                            |1733                         |
|vary                           |Accept-Encoding              |
|server                         |apache 2.4.46                |

Ce tableau représentatif est loin de montrer toute les valeurs du Head. J'ai juste mit quelques valeurs histoire de montrée. Celle qui va nous intéressées sera la valeur de la clefs nommée server. Dans l'exemple si dessus la valeur sera apache 2.4.46 donc la version du serveur web.

Il ne faut plus que faire la recherche de la valeur server dans le dictionnaire, de la faire affiché et le tour est jouer. 

A partir de cette information vous pouvez faire des recherches sur des potentielles failles de sécurité de la version du serveur puis essayer de les exploiter.
