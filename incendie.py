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
    canvas.create_rectangle((x * COTE, y * COTE), (x * COTE + COTE,
                                                   y * COTE + COTE),
                            fill=couleur)
    tableau[x][y][0] = etat


def creer_tableau():
    """Initialise un tableau qui vaut -1 pour une case
    morte et l'identifiant du carre si une case est vivante"""
    global tableau
    tableau = []
    for col in range(NB_COL):
        tableau_col = []
        for line in range(NB_LINE):
            tableau_col.append([-1])
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


def transformation_parcelle(event):
    """Mets le feu a une parcelle et change son etat en 3 = feu"""
    global tableau
    x = event.x // COTE
    y = event.y // COTE
    if tableau[x][y] == 0:
        pass
    else:
        canvas.create_rectangle((x * COTE, y * COTE),
                                (x * COTE + COTE, y * COTE + COTE), fill="red")
        tableau[x][y][0] = 3
        tableau[x][y].append(DUREE_FEU)


def prend_feu(x, y):
    """Enflame la parcelle aux coordonnées x y"""
    canvas.create_rectangle((x * COTE, y * COTE),
                            (x * COTE + COTE, y * COTE + COTE), fill="red")
    tableau[x][y][0] = 3
    tableau[x][y].append(DUREE_FEU)


def start():
    """Lance la simulation en affichant le nombre de
    cases en feu et l'étape de la simulation"""
    boutton_start.config(text="Pause", command=pause)
    for x in range(LARGEUR // COTE):
        for y in range(HAUTEUR // COTE):
                if tableau[x][y][0] == 3:
                    checking_plaine(x, y)
                if tableau[x][y][0] == 1:
                    checking_foret(x, y)
    canvas.after(1000, start)


def pause():
    """Mets la simulation en pause"""
    boutton_start.config(text="Start", command=start)


def checking_plaine(x, y):
    """Check les cases adjacentes"""
    if y - 1 >= 0:
        etat_case_dessus = tableau[x][y - 1][0]
        if etat_case_dessus == 2:
            prend_feu(x, y - 1)
        else:
            pass
    if y + 1 < HAUTEUR // COTE:
        etat_case_dessous = tableau[x][y + 1][0]
        if etat_case_dessous == 2:
            prend_feu(x, y + 1)
        else:
            pass
    if x + 1 < LARGEUR // COTE:
        etat_case_droite = tableau[x + 1][y][0]
        if etat_case_droite == 2:
            prend_feu(x + 1, y)
        else:
            pass
    if x - 1 >= 0:
        etat_case_gauche = tableau[x - 1][y][0]
        if etat_case_gauche == 2:
            prend_feu(x - 1, y)
        else:
            pass


def checking_foret(x, y):
    """Check les cases adjacentes"""
    var_feu = 0
    if y - 1 >= 0:
        feu_case_dessus = tableau[x][y - 1][0]
        if feu_case_dessus == 3:
            var_feu += 1
        else:
            pass
    if y + 1 < HAUTEUR // COTE:
        feu_case_dessous = tableau[x][y + 1][0]
        if feu_case_dessous == 3:
            var_feu += 1
        else:
            pass
    if x + 1 < LARGEUR // COTE:
        feu_case_droite = tableau[x + 1][y][0]
        if feu_case_droite == 3:
            var_feu += 1
        else:
            pass
    if x - 1 >= 0:
        feu_case_gauche = tableau[x - 1][y][0]
        if feu_case_gauche == 3:
            var_feu += 1
        else:
            pass
    random = rd.randint(1, 10)
    if random <= var_feu:
        prend_feu(x, y)


def sauvegarder():
    "sauvegarder son terrain actuel"
    variables = [liste_parcelle]
    fichierSauvegarde = open("Projet_Incendie-2", "wb")
    pickle.dump(variables, fichierSauvegarde)
    fichierSauvegarde.close()


def charger():
    "charger un terrain dans les fichiers "


def test(event):
    x = event.x // 25
    y = event.y // 25
    print(tableau[x][y])


###############################
# Programme principal


racine = tk.Tk()
racine.config(bg="black")

canvas = tk.Canvas(racine, height=HAUTEUR, width=LARGEUR, bg="black")

boutton_generation = tk.Button(racine, text="Génération du terrain",
                               font=("Helvatica", "20"), bg="black",
                               fg="white", command=generation)
boutton_sauvegarder = tk.Button(racine, text="Sauvegarder",
                                font=("Arvo", "20"), bg="black",
                                fg="white", command=sauvegarder)
boutton_charger = tk.Button(racine, text="Charger", font=("Arvo", "20"),
                            bg="black", fg="white", command=charger)
boutton_start = tk.Button(racine, text="Start", font=("Helvatica", "20"),
                          bg="black", fg="white", command=start)

creer_tableau()

canvas.grid(column=0, rowspan=3)
boutton_generation.grid(row=0, column=1)
boutton_sauvegarder.grid(row=1, column=1)
boutton_charger.grid(row=2, column=1)
boutton_start.grid(row=3, column=0)
canvas.bind('<Button-1>', transformation_parcelle)
canvas.bind('<Button-3>', test)
racine.mainloop()
