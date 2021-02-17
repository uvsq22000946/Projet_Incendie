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


    for h in range (HAUTEUR // 25):
        etat = rd.randint(0,2)
        if etat == 1:
            canvas.create_rectangle((0, h*25), 0+25, h*25+25, fill = "green")



###############################
# Programme principal

racine = tk.Tk()
racine.config(bg="black")


canvas = tk.Canvas(racine, height=HAUTEUR, width=LARGEUR, bg="black")
boutton_generation = tk.Button(racine, text="Génération du terrain", font=("Helvatica", "20"), bg="black", fg="white", command=generation)

canvas.grid(column=0, rowspan=3)
boutton_generation.grid(row=0, column=1)




racine.mainloop()
