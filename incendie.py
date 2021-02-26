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
###############################
# Variables globales

HAUTEUR = 400
LARGEUR = 600

###############################
# Fonctions

def generation():
    """Genere un terrain aleatoirement"""
    x = 0
    while x != LARGEUR // 25:
        canvas.create_line((x * 25, 0), (x * 25, HAUTEUR), fill="white")
        x += 1

def sauvegarder():
    "sauvegarder son terrain actuel"
    shutil.copytree("C:\Users\acer\Desktop\Projet_Incendie-2\incendie.py","C:\Users\acer\Desktop\Projet_Incendie-2\proj")
    
def charger():
    "charger un terrain dans les fichiers "    
    
###############################
# Programme principal

racine = tk.Tk()
racine.config(bg="black")


canvas = tk.Canvas(racine, height=HAUTEUR, width=LARGEUR, bg="black")
boutton_generation = tk.Button(racine, text="Génération du terrain", font=("Helvatica", "20"), bg="black", fg="white", command=generation)
boutton_sauvegarder= tk.Button(racine, text="Sauvegarder", font=("Arvo", "20"), bg="black", fg="white", command=sauvegarder)
boutton_charger = tk.Button(racine, text="Charger", font=("Arvo", "20"), bg="black", fg="white", command=charger)

canvas.grid(column=0, rowspan=3)
boutton_generation.grid(row=0, column=1)
boutton_sauvegarder.grid(row=1, column=1)
boutton_charger.grid(row=2 , column=1)
racine.mainloop()
