# Scan
Scan est un programme de type couteau-suisse permettant de :
- Récupérer l'IP d'un site a partir de son url
- Obtenir la version du serveur hébergeant le site
- Faire un traceroute vers une IP 
- Scanner des chevaux de Troie sur un réseau



# Téléchargements
Téléchargez le dossier. Attention à mettre la [bibliotheque.py](https://github.com/quipiq/Scan/blob/main/bliblio.py) et le [main.py](https://github.com/quipiq/Scan/blob/main/main.py) dans le même dossier ou bien changer le chemin dans le programme.

# Les différentes options

## Récupérer l'IP d'un site a partir de son url:

### Comment ça marche ? 

Cette option n'est que l'exploitation de la résolution de noms des serveurs DNS permttant de retourner l'adresse Ip correspondant à une URL.

Une fois l'IP récupérée, vous pouvez l'utiliser afin de rechercher la version du serveur web, ainsi que réaliser des scans sur la présence de chevaux de Troie.


## Obtenir la version du serveur hébergeant le site

### Comment ça marche ? 

Cette option renvoie la version du serveur web d'un site. 

Nous faisons appel aux méthodes de requêtes HTTP, définies dans la section 4 de la RFC 7231 et section 2 dela RFC 5789.

En python les dictionnaire sont constituer d'une clef a laquelle on va assigner une valeur. Une fois cela fait on peut faire des recherches dans le dictionnaire par clef.

Voici un exemple simple d'un dictionnaire reçus avec une requête web : 


|clefs                         |valeur                        |
|-------------------------------|-----------------------------|
|date                           |Fri, 23 Apr 2021 23:27:11 GMT|
|age                            |1733                         |
|vary                           |Accept-Encoding              |
|server                         |apache 2.4.46                |

Ce tableau n'est pas exhaustif, référez-vous aux RFC afin d'en obtenir une liste détaillée. La clef qui nous intéresse est la clef "server" qui retourne dans l'exemple ci-dessus la version d'Apache utilisée.

A partir de cette information vous pouvez faire des recherches sur de potentielles failles de sécurité de la version du serveur afin de les exploiter ou de protéger votre serveur.

## Faire un traceroute vers une IP

### Comment sa marche ? 
Cette option envoie un paquet UDP ou ICMP vers un serveur. Il transite par des routeurs qui permettent d'indiquer différentes informations sur le parcours suivi par le paquet. 

Cette fonction est très pratique car lancée sur un réseau elle peut aider à encomprendre l'architecture interne. 
Imaginons vous avez accès à une invite de commande sur un PC dans un réseau. Vous voulez étudier la structure du réseau c'est a dire le nombre de machines, de routeurs, etc...
Le traceroute vous indiquera par quels points la paquet passera, c'est-à-dire les différents routeurs rencontrés. 

Voila un exemple de structure de réseau: 


![Untitled Workspace](https://user-images.githubusercontent.com/72353621/115970949-08de1d00-a546-11eb-8c0a-a9547a5052d8.png)

Vous souhaitez savoir par quels routeurs vous transitez pour atteinde le site 'www.ibm.com`.
Utilisez l'option 2 de cette manière:

2 - traceroute sur un nom de domaine

Veuillez entrer ce que vous voulez faire : 2

Veuillez entrer le nom de domaine : www.ibm.com

une fois cela fait voici le retour de l'opération :

    1     5 ms     4 ms     5 ms  livebox.home [****:****:****:****:****:****:****:****]
	2     5 ms    11 ms    34 ms  2001cb08a01402080193025300760037.ipv6.abo.wanadoo.fr [2001:cb08:a014:208:193:253:76:37]
	3    17 ms    27 ms    21 ms  2001:cfc4:0:b00::b
	4    24 ms    19 ms     *     bundle-ether101.auvtr5.aubervilliers.opentransit.net [2a01:cfc4:0:b00::5]
	5    33 ms    23 ms    28 ms  2001:688:0:3:8::332
	6    92 ms    31 ms    25 ms  ae2.r07.spine101.par01.fab.netarch.akamai.com [2a02:26f0:2900:308::1]
	7    31 ms    36 ms    32 ms  ae7.r01.leaf101.par01.fab.netarch.akamai.com [2a02:26f0:2900:a01::1]
	8    21 ms    29 ms    59 ms  ae1.r07.tor101.par01.fab.netarch.akamai.com [2a02:26f0:2900:1407::1]
	9    19 ms    29 ms    20 ms  g2a02-26f0-2b00-03ad-0000-0000-0000-0b3a.deploy.static.akamaitechnologies.com [2a02:26f0:2b00:3ad::b3a]

Décomposons ce résultat en deux parties distinctes:
- La première comporte les 3 premières valeur de chaque ligne qui s'avère être le temps que l'action a pris à s'effectuer (le temps d'envoie et de réception).

	|lignes                         |valeur                        |
	|-------------------------------|-----------------------------|
	|1                              |5 ms - 4 ms - 5 ms           |
	|2                              |5 ms - 11 ms - 34 ms             |
	|3                              |17 ms - 27 ms - 21 ms            |
	|4                              |24 ms - 19 ms - *                |
	|5                              |33 ms - 23 ms - 28 ms            |
	|6                              |92 ms - 31 ms - 25 ms            |
	|7                              |31 ms - 36 ms - 32 ms            |
	|8                              |21 ms - 29 ms - 59 ms            |
	|9                              |19 ms - 29 ms - 20 ms            |

- La seconde sera le reste de chaque ligne.

Cela indique le nom du routeur par lequel transite le paquet. La dernière ligne représente la cible.


## Scanner des chevaux de Troie sur un réseau

### Comment ça marche ? 

La bibliothèque [sockets](https://pypi.org/project/sockets/) est requise. 
Installation : `pip3 install socket`

Le but est de rechercher des ports ouverts sur le pare-feu d'un réseau, correspondant à des ports généralement affectés à dees Chevaux de Troie. 

Qu'est-ce qu'un port?
Le pare-feu sert a protéger votre réseau. Pour cela il ouvre ou ferme certaines "porte d'accès" appelée ports. Ces ports sont 'natés' (NAT : Network Adress Translation) vers des ports logiques de serveurs. Ces ports sont au nombre de 65 535. Les 1024 premiers sont utilisés pour des protocoles spécifiques (20 et 21 = FTP, 80 = HTTP,  22 = SSH etc...) mais ce n'est qu'une attribution arbitraire qui peut être modifiée. 
Vous aurez plus de détails, dont l'origine de 65535 ports en consultant la section 3.1 de la RFC 793.

Example : 

![connexion_exterieur](https://user-images.githubusercontent.com/72353621/115956947-fe993000-a4ff-11eb-975a-cc4ef3a5e18e.png)


Sur cet exemple la connexion vient de l'extérieur sur un port fermé par défaut car situé au dessus de 1024. Cet essai de connexion sera donc refusé par le pare-feu.


Reprenons notre exemple en changeant la requête de sens . C'est a dire de l'intérieur vers l'extérieur.

![connexion_interieur](https://user-images.githubusercontent.com/72353621/115956988-2f796500-a500-11eb-88ba-24ccba2bce51.png)

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





# Conclusion

Voila les 4 fonctions de ce programme expliqué. A vous d'en faire ce que vous voulez.
