###############################
# Groupe : MIASHS TD2
# Maxime Ebran
# Marie-Ange MESKINE
# Victoire Maga
# Sedra Ramarosaona
# Saïdou Barry
#
#
# https://github.com/uvsq22000946/Projet_Incendie
###############################

###############################
# Import des librairies

import tkinter as tk
import random as rd
from pathlib import Path
from os import getcwd, chdir, mkdir
import shutil
import pickle
###############################
# Constantes

HAUTEUR = 400
LARGEUR = 600
COTE = 25
DUREE_FEU = 8
DUREE_CENDRE = 16
NB_LINE = HAUTEUR // COTE
NB_COL = LARGEUR // COTE

###############################
# Variables globales

liste_parcelle = []

###############################
# Fonctions


def generation_parcelle(couleur, x, y, etat):
    """Genere une parcelle de la couleur
    mise en argument aux coordonnee x et y. La variable
    etat change en fonction de la nature de la parcelle
    0 = Eau, 1 = Foret, 2 = Plaine"""
    global tableau
    canvas.create_rectangle((x * COTE, y * COTE), (x * COTE + COTE, y * COTE + COTE),
                            fill=couleur)
    tableau[x][y] = etat

def creer_tableau():
    """Initialise un tableau qui vaut -1 pour une case morte et l'identifiant du carre si une case est vivante"""
    global tableau
    tableau = []
    for col in range(NB_COL):
        tableau_col = []
        for line in range(NB_LINE):
            tableau_col.append(-1)
        tableau.append(tableau_col)


def generation():
    """Genere un terrain aleatoirement"""

    for x in range(LARGEUR // COTE):
        for y in range(HAUTEUR // COTE):
            etat = rd.randint(0, 2)
            if etat == 0:
                generation_parcelle("blue", x, y, 0)
            if etat == 1:
                generation_parcelle("green", x, y, 1)
            if etat == 2:
                generation_parcelle("yellow", x, y, 2)
    print(tableau)


def start():
    """Lance la simulation en affichant le nombre de
    cases en feu et l'étape de la simulation"""
    boutton_start.config(text="Pause", command=pause)
    


def pause():
    """Mets la simulation en pause"""
    boutton_start.config(text="Start", command=start)


def create_liste_feu(liste):
    """Créer la liste des parcelles en feu"""
    liste_feu = []
    for parcelle in liste:
        if "red" in parcelle:
            liste_feu.append(parcelle[1])
        else:
            pass
    return liste_feu


def checking(x, y):
    """Check les cases adjacentes"""
    pass


def sauvegarder():
    "sauvegarder son terrain actuel"
    variables = [liste_parcelle]
    fichierSauvegarde = open("Projet_Incendie-2","wb")
    pickle.dump(variables, fichierSauvegarde)
    fichierSauvegarde.close()


def charger():
    "charger un terrain dans les fichiers "


def compteur_de_tour_feu():
    """Ajoute une case de durée d'état dans chaque liste de cendres et de feu"""
    liste_feu = create_liste_feu(liste_parcelle)
    liste_temps = []
    for element in liste_feu:
        parcelle_feu = []
        parcelle_feu.append(element)
        parcelle_feu.append(DUREE_FEU)
        liste_temps.append(parcelle_feu)


###############################
# Programme principal


racine = tk.Tk()
racine.config(bg="black")

canvas = tk.Canvas(racine, height=HAUTEUR, width=LARGEUR, bg="black")

boutton_generation = tk.Button(racine, text="Génération du terrain", font=("Helvatica", "20"), bg="black", fg="white", command=generation)
boutton_sauvegarder= tk.Button(racine, text="Sauvegarder", font=("Arvo", "20"), bg="black", fg="white", command=sauvegarder)
boutton_charger = tk.Button(racine, text="Charger", font=("Arvo", "20"), bg="black", fg="white", command=charger)

creer_tableau()

canvas.grid(column=0, rowspan=3)
boutton_generation.grid(row=0, column=1)
boutton_sauvegarder.grid(row=1, column=1)
boutton_charger.grid(row=2 , column=1)
racine.mainloop()
