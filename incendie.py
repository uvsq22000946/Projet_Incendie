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

###############################
# Constantes

HAUTEUR = 400
LARGEUR = 600
COTE = 25

###############################
# Variables globales

liste_parcelle = []

###############################
# Fonctions


def generation_parcelle(couleur, x, y):
    """Genere une parcelle de la couleur
    mise en argument aux coordonnee x et y"""
    case_actuelle = []
    case_actuelle.append(couleur)
    case_actuelle.append(canvas.create_rectangle((x * COTE, y * COTE),
                                                 (x * COTE + COTE, y * COTE + COTE),
                                                 fill=couleur))
    liste_parcelle.append(case_actuelle)


def generation():
    """Genere un terrain aleatoirement"""

    for x in range(LARGEUR // COTE):
        for y in range(HAUTEUR // COTE):
            etat = rd.randint(0, 2)
            if etat == 0:
                generation_parcelle("blue", x, y)
            if etat == 1:
                generation_parcelle("green", x, y)
            if etat == 2:
                generation_parcelle("yellow", x, y)


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


def checking(idx_parcelle):
    """Check les cases adjacentes"""
    nombre_parcelle_feu = 0
    liste_feu = create_liste_feu(liste_parcelle)
    if idx_parcelle + 1 in liste_feu:
        nombre_parcelle_feu += 1
    if idx_parcelle - 1 in liste_feu:
        nombre_parcelle_feu += 1
    if idx_parcelle + LARGEUR // COTE in liste_feu:
        nombre_parcelle_feu += 1
    if idx_parcelle - LARGEUR // COTE in liste_feu:
        nombre_parcelle_feu += 1
    return nombre_parcelle_feu


###############################
# Programme principal


racine = tk.Tk()
racine.config(bg="black")

canvas = tk.Canvas(racine, height=HAUTEUR, width=LARGEUR, bg="black")

boutton_generation = tk.Button(racine, text="Génération du terrain",
                               font=("Helvatica", "20"), bg="black",
                               fg="white", command=generation)

boutton_sauver = tk.Button(racine, text="Sauvegarder",
                           font=("Helvatica", "20"), bg="black", fg="white")

boutton_charger = tk.Button(racine, text="Charger", font=("Helvatica", "20"),
                            bg="black", fg="white")

boutton_start = tk.Button(racine, text="Start", font=("Helvatica", "20"),
                          bg="black", fg="white", command=start)


canvas.grid(column=0, rowspan=3)
boutton_generation.grid(row=0, column=1)
boutton_sauver.grid(row=1, column=1)
boutton_charger.grid(row=2, column=1)
boutton_start.grid(row=3, column=0)

racine.mainloop()
