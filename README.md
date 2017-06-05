# MFRC522-Pi_3.0
## French

Graphical Interface for MFRC522 RFID on Raspberry Pi

Réalisé par Quentin Arnould, Antonin Chauvet et Raphaël Brogat

Ce Projet a été réalisé dans le cadre de nos études à l'INSA Centre-Val-de-Loire

#### Prérequis:
Cloner le repository SPI-Py :

<code> cd /home/Pi/</code>

<code>sudo git clone https://github.com/lthiery/SPI-Py.git </code>

Notre programme utilise 4 fichiers Python:
  Interface.py est le programme principal et permet le lancement de notre interface graphique

  fonctions_lib.py contient les fonctions de lecture et d'écriture via le lecteur RFID. Ces fonctions peuvent être utilisées indépendemment de l'interface

  gestion_bdd.py contient les fonctions permettant l'upload du contenu des tags vers la base de données
  
  MFRC522-Pi_2.py est une révision du "MFRC522-Pi" présent ici : https://github.com/mxgxw/MFRC522-python
  
 
  ## English

Graphical Interface for MFRC522 RFID on Raspberry Pi

Accomplished by Quentin Arnould, Antonin Chauvet and Raphael Brogat

This software was made as part of our studies in INSA CENTRE-VAL-DE-LOIRE

#### REQUIRED :
you have to clone SPI-Py repository:

<code> cd /home/Pi/</code>

<code>sudo git clone https://github.com/lthiery/SPI-Py.git </code>

Our program uses 4 Python files:
  Interface.py is the main program and launches our graphical interface

  fonctions_lib.py contains functions of reading and and writing trough RFID reader. These functions can be used independently from the interface

  gestion_bdd.py contains functions for uploading tag's content to the database
   
  MFRC522-PI_2 is a revision of "MFRC522-Pi" : https://github.com/mxgxw/MFRC522-python
