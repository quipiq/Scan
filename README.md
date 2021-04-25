# Scan
Scan est un programme de type couteau-suisse permettant de :
- Récupérer l'IP d'un site a partir de son url
- Obtenir la version du serveur hébergeant le site
- Faire un traceroute vers une IP 
- Scanner des chevaux de Troie sur un réseau.



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

Ce tableau n'est pas exhaustif, référrez-vous aux RFC pour en obtenir une liste détaillée. La clef qui nous intéresse est la clef "server" qui retourne sur l'exemple ci-dessus la version d'Apache utilisée.

A partir de cette information vous pouvez faire des recherches sur de potentielles failles de sécurité de la version du serveur afin de les exploiter ou de protéger votre serveur.

## Faire un traceroute vers une IP

### Comment sa marche ? 
Cette option est assez simple. Elle envoie un paquet UDP ou ICMP vers un serveur. Ces derniers transitent par des routeurs qui permettent d'indiquer différentes informations sur le parcours suivi par le paquet. 

Cette fonction est très pratique car lancée sur un réseau elle peut aider à encomprendre l'architecture interne. 
Imaginons vous avez accès à une invite de commande sur un PC dans un réseau. Vous voulez étudier la structure du réseau c'est a dire le nombre de machines, de routeurs, etc...
Le traceroute vous indiquera par quels points la paquet passera, c'est les dire les différents routeurs rencontrés. 

Voila un exemple de structure de réseau: 

![Untitled Workspace (1)](https://user-images.githubusercontent.com/72353621/115970945-04196900-a546-11eb-80f3-3256c520e0b2.png)

Ce réseau est assez complet, pour mieux vous expliquez comment marche le traceroute je vais utiliser un autre réseau simplifier :

![Untitled Workspace](https://user-images.githubusercontent.com/72353621/115970949-08de1d00-a546-11eb-8c0a-a9547a5052d8.png)

Pour vous montrez je vais utiliser CMD. La commande pour CMD ne s'appelle pas traceroute mais tracert, il faut après le tracert mettre le nom de domaine(url) ou l'IP. Je vais pour cette exemple utiliser la commande sur le site ibm.com. 

je vais donc entrer la commande :  `tracert www.ibm.com`

une fois cela fait voici le retour de l'opération :

    1     5 ms     4 ms     5 ms  livebox.home [****:****:****:****:****:****:****:****]
	2     5 ms    11 ms    34 ms  2a01cb08a00402080193025300750037.ipv6.abo.wanadoo.fr [2a01:cb08:a004:208:193:253:75:37]
	3    17 ms    27 ms    21 ms  2a01:cfc4:0:b00::b
	4    24 ms    19 ms     *     bundle-ether101.auvtr5.aubervilliers.opentransit.net [2a01:cfc4:0:b00::5]
	5    33 ms    23 ms    28 ms  2001:688:0:3:8::332
	6    92 ms    31 ms    25 ms  ae2.r07.spine101.par01.fab.netarch.akamai.com [2a02:26f0:2900:308::1]
	7    31 ms    36 ms    32 ms  ae7.r01.leaf101.par01.fab.netarch.akamai.com [2a02:26f0:2900:a01::1]
	8    21 ms    29 ms    59 ms  ae1.r07.tor101.par01.fab.netarch.akamai.com [2a02:26f0:2900:1407::1]
	9    19 ms    29 ms    20 ms  g2a02-26f0-2b00-03ad-0000-0000-0000-0b3a.deploy.static.akamaitechnologies.com [2a02:26f0:2b00:3ad::b3a]

Commençons par décomposée ce résultat en deux partie distinctes, la première est celle comportant les 3 première valeur de chaque ligne qui s'avère être le temps que l'action a pris à s'effectuer (le temps d'envoie et de réception).

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

La deuxième sera le reste de chaque ligne. Cela va donner le nom du routeur par lequel il passe et son IP V6. Attention pour la dernière ligne ce n'est pas un routeur mais un serveur web car il est arrivé a destinations. Si je compare le résultat de ce traceroute et mon schéma de réseau ci-dessus, les valeurs correspondes bien, j'ai le paquet qui passe par le seul routeur que contient mon réseau (en générale la box qui comprend aussi le firewall) puis va ensuite dans les routeur externe pour arriver à la destination voulue (le serveur web).

> Pour des raisons de sécurité j'ai remplacer l'IP de mon routeur par des étoiles. Vous vous douterez bien qu'il y aura marqué l'IP de votre routeur lorsque vous le ferrez et non des étoiles. 



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
