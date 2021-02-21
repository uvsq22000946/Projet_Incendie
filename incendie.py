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

###############################
# Variables globales

liste_parcelle = []

###############################
# Fonctions


def generation():
    """Genere un terrain aleatoirement"""

    for x in range(LARGEUR // 25):
        for y in range(HAUTEUR // 25):
            etat = rd.randint(0, 2)
            if etat == 0:
                case_actuelle = []
                case_actuelle.append("blue")
                case_actuelle.append(canvas.create_rectangle((x * 25, y * 25),
                                                             (x * 25 + 25,
                                                              y * 25 + 25),
                                                             fill="blue"))
                liste_parcelle.append(case_actuelle)
            if etat == 1:
                case_actuelle = []
                case_actuelle.append("green")
                case_actuelle.append(canvas.create_rectangle((x * 25, y * 25),
                                                             (x * 25 + 25,
                                                             y * 25 + 25),
                                                             fill="green"))
                liste_parcelle.append(case_actuelle)
            if etat == 2:
                case_actuelle = []
                case_actuelle.append("yellow")
                case_actuelle.append(canvas.create_rectangle((x * 25, y * 25),
                                                             (x + 25 * 25,
                                                             y * 25 + 25),
                                                             fill="yellow"))
                liste_parcelle.append(case_actuelle)


def start():
    """Lance la simulation en affichant le nombre de
    cases en feu et l'étape de la simulation"""
    boutton_start.config(text="Pause", command=pause)


def pause():
    """Mets la simulation en pause"""
    boutton_start.config(text="Start", command=start)


def check():
    """Checking des cases adjacentes"""


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
