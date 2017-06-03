#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522_2 as MFRC522
import signal

def Ecrire_le_bloc(bloc, data):

    continue_reading = True
    def end_read(signal, frame):
        global continue_reading
        print "Ctrl+C captured, ending read."
        continue_reading = False
        GPIO.cleanup()

    # Hook the SIGINT
    signal.signal(signal.SIGINT, end_read)

    # Create an object of the class MFRC522
    MIFAREReader = MFRC522.MFRC522()

    # This loop keeps checking for chips. If one is near it will get the UID and authenticate
    while continue_reading:

        # Scan for cards
        (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

        # If a card is found
        #if status == MIFAREReader.MI_OK:
          #  print "Card detected"

        # Get the UID of the card
        (status, uid) = MIFAREReader.MFRC522_Anticoll()

        # If we have the UID, continue
        if status == MIFAREReader.MI_OK:

            # Print UID
            #print "Card read UID: " + str(uid[0]) + "," + str(uid[1]) + "," + str(uid[2]) + "," + str(   uid[3]) + "," + str(uid[4])

            # This is the default key for authentication
            key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

            # Select the scanned tag
            MIFAREReader.MFRC522_SelectTag(uid)

            # Authenticate
            status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, bloc, key, uid)

            # Check if authenticated
            if status == MIFAREReader.MI_OK:

                # Variable for the data to write
                #data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
                #convert_text(data)

                #print "Sector bloc looked like this:"
                # Read block bloc
                MIFAREReader.MFRC522_Read(bloc)

                #print "Sector bloc will now be filled with data:"
                # Write the data
                MIFAREReader.MFRC522_Write(bloc, data)

                #print "It now looks like this:"
                # Check to see if it was written
                #print MIFAREReader.MFRC522_Read(bloc)

                # Stop
                MIFAREReader.MFRC522_StopCrypto1()

                # Make sure to stop reading for cards
                continue_reading = False
            else:
                print "Authentication error"

def Lire_le_bloc(bloc):
    continue_reading = True


    # Capture le SIGINT afin de "cleanup" lorsque l'on arrête la lecture
    def end_read(signal, frame):
        global continue_reading
        print("Ctrl+C captured, ending read.")
        continue_reading = False
        GPIO.cleanup()


    # Capter le SIGINT
    signal.signal(signal.SIGINT, end_read)
    # Créer l'objet de classe MFRC522
    MIFAREReader = MFRC522.MFRC522()

    # Message de début de lecture
    #print("Vous avez choisi de lire le block du tag: ")
    #print("Appuyez sur Ctrl-C pour arrêter la lecture de tag.")

    while continue_reading:

        # Scan les environs à la recherche d'un tag
        (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

        # Si tag trouvé
        if status == MIFAREReader.MI_OK:
            #print("Tag détecté")
            # on arrête la lecture à la fin de la boucle afin de ne pas lire plusieurs fois le même tag
            continue_reading = False
        global uid

        # Récupérer l'IUD et le status
        (status, uid) = MIFAREReader.MFRC522_Anticoll()


    # Clé d'authentification default
    key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

    # Sélectionner le tag
    MIFAREReader.MFRC522_SelectTag(uid)

    # Authentification
    status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, (bloc), key, uid)

    # Check l'authentification
    if status == MIFAREReader.MI_OK:
        backdata = MIFAREReader.MFRC522_Read(bloc)
        GPIO.cleanup()
        return backdata
    else:
        print("Erreur d'authenfication du bloc ", bloc)

def Convert_text_int(text):
    for i in range (len(text)):
        text[i] = ord(text[i])
    return text

def Convert_liste_str(liste):
    chaine = "".join(liste)
    return chaine

def Convert_uid_str(liste):
    chaine = ""
    for i in range(16):
        chaine = chaine + str('{0:02x}'.format(liste[i]))
    return chaine

def Convert_str_liste(chaine):
    liste = list(chaine)
    return liste

def Remplir_liste_16(liste):
    for i in range(len(liste),16):
        liste.append(0)
    return liste

def Decoupe_liste(liste):
    # On initialise les 3 listes
    liste1 = []
    liste2 = []
    liste3 = []
    for i in range(16):
        liste1.append(0)
        liste2.append(0)
        liste3.append(0)


    # On remplie les listes avec le texte et on les complete avec des 0
    if len(liste)>16:
        liste1 =  liste [0:16]
        if len(liste)>32:
            liste2 = liste[16:32]
            liste3 = Remplir_liste_16(liste[32:])
        else:
            liste2 = Remplir_liste_16(liste[16:])
    else:
        liste1 = Remplir_liste_16(liste[0:])
    return (liste1, liste2, liste3)

def Concatene_liste(p1, p2, p3):
    liste = p1 + p2 + p3
    return liste

def Supprime_0_liste(liste):
    while liste.count(0)>0:
        liste.remove(0)
    return liste

def Convert_int_text(liste):
    for i in range (len(liste)):
        liste[i] = str(unichr(liste[i]))
    return liste

def Ecrire_texte(secteur, chaine):
    bloc=secteur*4
    p1, p2, p3 = Decoupe_liste(Convert_text_int(Convert_str_liste(chaine)))
    print p1, "||", p2, "||", p3
    Ecrire_le_bloc(bloc, p1)
    Ecrire_le_bloc(bloc+1, p2)
    Ecrire_le_bloc(bloc+2, p3)
    print"Ecriture réalisee"

def Lire_texte(secteur):
    bloc = secteur *4
    p1 = Lire_le_bloc(bloc)
    p2 = Lire_le_bloc(bloc+1)
    p3 = Lire_le_bloc(bloc+2)
    print"3 blocs lus"
    texte = Convert_liste_str(Convert_int_text(Supprime_0_liste(Concatene_liste(p1,p2,p3))))
    print "Secteur ", bloc/4, " :", texte
    return texte

def Lire_UID():
    bloc = 0
    texte = Convert_uid_str(Lire_le_bloc(bloc))
    return texte


