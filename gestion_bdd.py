# -*- coding: utf8 -*-
import mysql.connector
from mysql.connector import errorcode
HOST_IP = '192.168.43.122'
DATABASE = 'rfid'
USER = 'raspberry'
PASSWORD = 'rfid2017'


def ecriture_bdd(uid,nom,prenom,etat,code):
    try:
        #Connection
        bdd = mysql.connector.connect(user='raspberry', password='rfid2017',host='192.168.43.122',database='rfid')
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Mauvais nom d'utilisateur / mot de passe.")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("La base de donnée n'existe pas.")
      else:
        print("Erreur bdd")
        return -1
    else:
        #Si la connection a bien marchée, on créé un curseur
        cursor = bdd.cursor()
        #On regarde si le tag existe et on adapte la commande en fonction
        print "Lancement de la recherche"
        if recherche_bdd(uid) == 0:
            operation = ("INSERT INTO puces "
                         "(UID,Nom,Prenom,Etat,Code) "
                         "VALUES (%(uid)s,%(nom)s,%(prenom)s,%(etat)s,%(code)s)")
        else:
            operation = ("UPDATE puces SET Nom = %(nom)s, Prenom = %(prenom)s, Etat = %(etat)s, Code = %(code)s "
                         "WHERE UID = %(uid)s")
        data_ajouter = {
            'uid': uid,
            'nom': nom,
            'prenom': prenom,
            'etat': etat,
            'code': code,
        }
        #Placement dans le curseur
        cursor.execute(operation,data_ajouter)
        #Execution du curseur
        bdd.commit()
        #Fermeture de la connection
        cursor.close()
        bdd.close()
        print "Base de donnée mise à jour."
        return 0
#Fonction de recherche pour savoir si l'uid existe dans la base de donnée
def recherche_bdd(uid):
    try:
        bdd = mysql.connector.connect(user='raspberry', password='rfid2017',host='192.168.43.122',database='rfid')
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Mauvais nom d'utilisateur / mot de passe.")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("La base de donnée n'existe pas.")
      else:
        print("Erreur bdd" +err)
    else:
        cursor = bdd.cursor()
        data = {
            'uid': uid,
        }
        cursor.execute("SELECT UID FROM puces WHERE UID = %(uid)s", data)
        row = cursor.fetchone()
        if row == None:
            return 0
        else:
            return 1
        bdd.commit()
        cursor.close()
        bdd.close()
