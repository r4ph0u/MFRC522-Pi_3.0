#!/usr/bin/env python
# -*- coding: utf8 -*-

from Tkinter import *
import tkMessageBox
import fonctions_lib as  lib
import gestion_bdd as bdd

#CHAMP           =  secteur
TAG_UID          = 0
TAG_NOM          = 1
TAG_PRENOM       = 2
TAG_ETAT         = 3
TAG_CODE         = 4

def Affichage(root):

    fenetre_affichage = Toplevel(root)
    fenetre_affichage.geometry("450x330+350+30")
    fenetre_affichage.title("Lecture du tag")
    fenetre_affichage['bg'] = 'light grey'

    #FRAMES
    frame_affichage_text = Frame(fenetre_affichage, bg='light grey', height=300, width=200, relief=FLAT)
    frame_affichage_text.pack(side=LEFT, padx=10, pady=10)

    frame_affichage_close = Frame(fenetre_affichage, bg='white', relief=FLAT, borderwidth=1)
    frame_affichage_close.pack(side=TOP, padx=5, pady=15)

    frame_affichage_run = Frame(fenetre_affichage, bg='white', relief=FLAT, borderwidth=1)
    frame_affichage_run.pack(side=TOP, padx=5, pady=15)

    frame_affichage_upload = Frame(fenetre_affichage, bg='white', relief=FLAT, borderwidth=1)
    frame_affichage_upload.pack(side=TOP, padx=5, pady=15)

    #CANVAS
    canvas_affichage_text = Canvas(frame_affichage_text, width=310, height=200, bg='white', relief=RIDGE, borderwidth=3)
    canvas_affichage_text.pack(side=LEFT, padx=10, pady=10)

    def lire_run():
        tkMessageBox.showinfo("Rappel", "Déposez le tag sur le lecteur")
        canvas_affichage_text.delete("all")
        canvas_affichage_text.create_text(10, 10, text="Client : "+lib.Lire_texte(TAG_PRENOM) + " "+lib.Lire_texte(TAG_NOM), font="Showcard 13", anchor=NW)
        canvas_affichage_text.create_text(10, 60, text="Etat du produit : "+lib.Lire_texte(TAG_ETAT), font="Showcard 13", anchor=NW)
        canvas_affichage_text.create_text(10, 110, text="Code du produit : "+lib.Lire_texte(TAG_CODE), font="Showcard 13", anchor=NW)
        canvas_affichage_text.create_text(10, 185, text="UID: " + lib.Lire_UID(), font="Showcard 7", anchor=NW)
        canvas_affichage_text.pack(side=LEFT, padx=10, pady=10)

    def upload_run():
        tkMessageBox.showinfo("Rappel", "Déposez le tag sur le lecteur")
        nom=lib.Lire_texte(TAG_NOM)
        prenom=lib.Lire_texte(TAG_PRENOM)
        etat=lib.Lire_texte(TAG_ETAT)
        code=lib.Lire_texte(TAG_CODE)
        uid=lib.Lire_UID()

        retour = bdd.ecriture_bdd(uid, nom, prenom, etat, code)
        if retour == 0:
            tkMessageBox.showinfo("Result", "Tag stocké dans la base de donnée avec succès")
        else:
            tkMessageBox.showinfo("Result", "Erreur lors de l'écriture dans la base de données")
        fenetre_affichage.destroy()


    #BUTTONS
    button_affichage_close = Button(frame_affichage_close, relief=RIDGE,image=exit, bg='white', command=fenetre_affichage.destroy)
    button_affichage_close.pack()

    button_affichage_run = Button(frame_affichage_run, relief=RIDGE, image=afficher, bg='white', command=lire_run)
    button_affichage_run.pack()

    button_affichage_upload = Button(frame_affichage_upload, relief=RIDGE, image=upload, bg='white', command=upload_run)
    button_affichage_upload.pack()

    fenetre_affichage.mainloop()

def Nom(root):
    tkMessageBox.showinfo("Rappel", "Ne pas utiliser de caractères spéciaux")
    fenetre_nom = Toplevel(root)
    fenetre_nom.geometry("400x230+350+30")
    fenetre_nom.title("Saisie Client")
    fenetre_nom['bg'] = 'light grey'

    #FRAMES
    frame_nom_input1 = Frame(fenetre_nom, bg='light grey', height=50, width=200, relief=RIDGE)
    frame_nom_input1.pack(side=TOP, padx=10, pady=10)

    frame_nom_input2 = Frame(fenetre_nom, bg='light grey', height=50, width=200, relief=RIDGE)
    frame_nom_input2.pack(side=TOP, padx=10, pady=10)

    frame_nom_run = Frame(fenetre_nom, bg='light grey', relief=FLAT)
    frame_nom_run.pack(side=LEFT, padx=10, pady=10)

    frame_nom_close = Frame(fenetre_nom, bg='white', relief=FLAT, borderwidth=1)
    frame_nom_close.pack(side=LEFT, padx=5, pady=5)

    #LABELS
    label_input_1 = Label (frame_nom_input1, text="Nom :", font="Showcard 13", relief=RIDGE, bg='white', bd=1)
    label_input_1.pack()
    label_input_2 = Label (frame_nom_input2, text="Prénom :", font="Showcard 13", relief=RIDGE, bg='white', bd=1)
    label_input_2.pack()


    def nom_run ():

        tkMessageBox.showinfo("Rappel", "Déposez le tag sur le lecteur")
        X= input1.get()
        Y= input2.get()

        print X,Y

        lib.Ecrire_texte(TAG_NOM,X)
        lib.Ecrire_texte(TAG_PRENOM,Y)
        fenetre_nom.destroy()

    nom = StringVar()

    input1 = Entry(frame_nom_input1, textvariable=nom, width=30)
    input1.pack()

    prenom = StringVar()

    input2 = Entry(frame_nom_input2, textvariable=prenom, width=30)
    input2.pack()

    #BUTTONS
    button_nom_close = Button(frame_nom_close, image=exit, relief=RIDGE, bg='white', command=fenetre_nom.destroy)
    button_nom_close.pack()

    button_nom_run = Button(frame_nom_run, image=valider, relief=RIDGE, bg='white', command=nom_run)
    button_nom_run.pack(padx=50)

    fenetre_nom.mainloop()

def Etat(root):

    fenetre_etat = Toplevel(root)
    fenetre_etat.geometry("400x320+350+35")
    fenetre_etat.title("Etat produit")
    fenetre_etat['bg'] = 'light grey'

    # FRAMES
    frame_selection = Frame(fenetre_etat, bg='light grey', height=50, width=200, relief=RIDGE)
    frame_selection.pack(side=TOP, padx=10, pady=10)

    frame_etat_run = Frame(fenetre_etat, bg='light grey', relief=FLAT, borderwidth=1)
    frame_etat_run.pack(side=LEFT, padx=10, pady=10)

    frame_etat_close = Frame(fenetre_etat, bg='white', relief=FLAT, borderwidth=1)
    frame_etat_close.pack(side=LEFT, padx=5, pady=5)

    # LABELS
    label_selection = Label(frame_selection, text="Selectionner l'etat du produit :", font="Showcard 11", relief=RIDGE, bg='white')
    label_selection.pack()

    ##GRILLE
    value = StringVar()
    code_pdt1 = Radiobutton(frame_selection, bg='white', text="En stock", font="Showcard 12", relief=RIDGE, borderwidth=1, variable=value, value="En stock", indicatoron=0)
    code_pdt2 = Radiobutton(frame_selection, bg='white', text="En préparation", font="Showcard 12", relief=RIDGE, borderwidth=1, variable=value, value="En preparation", indicatoron=0)
    code_pdt3 = Radiobutton(frame_selection, bg='white', text="En livraison", font="Showcard 12", relief=RIDGE, borderwidth=1, variable=value, value="En livraison", indicatoron=0)
    code_pdt1.pack(side=TOP, pady=5)
    code_pdt2.pack(side=TOP, pady=5)
    code_pdt3.pack(side=TOP, pady=5)

    def etat_run():
        tkMessageBox.showinfo("Rappel", "Déposez le tag sur le lecteur")
        X = value.get()
        lib.Ecrire_texte(TAG_ETAT,X)
        fenetre_etat.destroy()

    # BUTTONS
    button_etat_close = Button(frame_etat_close, image=exit, relief=RIDGE, bg='white', command=fenetre_etat.destroy)
    button_etat_close.pack()

    button_etat_run = Button(frame_etat_run, image=valider, relief=RIDGE, bg='white', command=etat_run)
    button_etat_run.pack(padx=30)

    fenetre_etat.mainloop()


def Code(root):

    fenetre_code = Toplevel(root)
    fenetre_code.geometry("400x300+350+35")
    fenetre_code.title("Etat produit")
    fenetre_code['bg'] = 'light grey'

    # FRAMES
    frame_select_code = Frame(fenetre_code, bg='light grey', height=50, width=200, relief=RIDGE)
    frame_select_code.pack(side=TOP, padx=10, pady=10)

    frame_code_run = Frame(fenetre_code, bg='light grey', relief=FLAT, borderwidth=1)
    frame_code_run.pack(side=LEFT, padx=10, pady=10)

    frame_code_close = Frame(fenetre_code, bg='white', relief=FLAT, borderwidth=1)
    frame_code_close.pack(side=LEFT, padx=5, pady=5)

    # LABELS
    label_select = Label(frame_select_code, text="Selectionner le code produit :", font="Showcard 11", relief=RIDGE, bg='white')
    label_select.pack(side=TOP,pady=10)

    #GRILLE
    value = StringVar()
    code_pdt1 = Radiobutton(frame_select_code, bg='white', text="A01A", font="Showcard 12", relief=RIDGE, borderwidth=1, variable=value, value="A01A")
    code_pdt2 = Radiobutton(frame_select_code, bg='white', text="B0X3", font="Showcard 12", relief=RIDGE, borderwidth=1, variable=value, value="B0X3")
    code_pdt3 = Radiobutton(frame_select_code, bg='white', text="G7S4", font="Showcard 12", relief=RIDGE, borderwidth=1, variable=value, value="G7S4")
    code_pdt1.pack(side=LEFT, padx=2)
    code_pdt2.pack(side=LEFT, padx=2)
    code_pdt3.pack(side=LEFT, padx=2)

    def code_run ():
        tkMessageBox.showinfo("Rappel", "Déposez le tag sur le lecteur")
        X = value.get()
        lib.Ecrire_texte(TAG_CODE,X)
        fenetre_code.destroy()

    # BUTTONS
    button_code_close = Button(frame_code_close, image=exit, relief=RIDGE, bg='white', command=fenetre_code.destroy)
    button_code_close.pack()

    button_code_run = Button(frame_code_run, image=valider, relief=RIDGE, bg='white', command=code_run)
    button_code_run.pack(padx=30)

    fenetre_code.mainloop()


fenetre_main = Tk()
fenetre_main.geometry("330x415+0+0")
fenetre_main.title("Menu principal")
fenetre_main['bg'] = 'light grey'

#FRAMES
frame_main_logo = Frame(fenetre_main, bg='light grey', height=300, width=150, relief=RIDGE, borderwidth=1)
frame_main_logo.pack(side=LEFT, padx=5, pady=5)

frame_main_close = Frame(fenetre_main, bg='white', height=50, width=200, relief=RIDGE, borderwidth=1)
frame_main_close.pack(side=TOP, padx=5, pady=5)

frame_main_write =Frame(fenetre_main, bg='white', height=300, width=200, relief=RIDGE, borderwidth=1)
frame_main_write.pack(side=TOP, padx=5, pady=5)

frame_main_read =Frame(fenetre_main, bg='white', height=75, width=200, relief=RIDGE, borderwidth=1)
frame_main_read.pack(side=TOP, padx=5, pady=5)


#IMAGES
logo = PhotoImage(file="ICONES/LOGO.gif")
afficher = PhotoImage(file="ICONES/afficher.gif")
exit = PhotoImage(file="ICONES/exit.gif")
modif_nom = PhotoImage(file="ICONES/nom.gif")
code_produit = PhotoImage(file="ICONES/code_produit.gif")
state = PhotoImage (file="ICONES/state.gif")
valider = PhotoImage(file="ICONES/valid.gif")
upload = PhotoImage (file="ICONES/upload.gif")

#LOGO
canvas_logo = Canvas(frame_main_logo, width=195, height=350, bg='white', relief=RIDGE, borderwidth=3)
canvas_logo.create_image(15, 15, anchor=NW, image=logo)
canvas_logo.pack()

#BUTTONS
button_close = Button(frame_main_close, image=exit, relief=RIDGE, bg='white', command=fenetre_main.destroy)
button_close.pack()

button_read = Button(frame_main_read, image=afficher, relief=RIDGE, bg='white', command=lambda x=fenetre_main: Affichage(x))
button_read.pack()

button_write_name = Button(frame_main_write, image=modif_nom, relief=RIDGE, bg='white', command=lambda x=fenetre_main: Nom(x))
button_write_name.pack()

button_write_state = Button(frame_main_write, image=state, relief=RIDGE, bg='white', command=lambda x=fenetre_main: Etat(x))
button_write_state.pack()

button_write_code = Button(frame_main_write, image=code_produit, relief=RIDGE, bg='white', command=lambda x=fenetre_main: Code(x))
button_write_code.pack()

fenetre_main.mainloop()