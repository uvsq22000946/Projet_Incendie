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

liste_parcelle_eau = []
liste_parcelle_foret = []
liste_parcelle_plaine = []

###############################
# Fonctions

def generation():
    """Genere un terrain aleatoirement"""

    for l in range(LARGEUR // 25):
        for h in range (HAUTEUR // 25):
            etat = rd.randint(0,2)
            if etat == 0:
                canvas.create_rectangle((l * 25, h * 25), (l * 25 + 25, h * 25 + 25), fill="blue")
                liste_parcelle_eau.append([l, h])
            if etat == 1:
                canvas.create_rectangle((l * 25, h*25), l * 25 + 25, h*25+25, fill = "green")
                liste_parcelle_foret.append([l, h])
            if etat == 2:
                canvas.create_rectangle((l * 25, h * 25), (l + 25 * 25, h * 25 + 25), fill="yellow")
                liste_parcelle_plaine.append([l, h])


###############################
# Programme principal

racine = tk.Tk()
racine.config(bg="black")


canvas = tk.Canvas(racine, height=HAUTEUR, width=LARGEUR, bg="black")
boutton_generation = tk.Button(racine, text="Génération du terrain", font=("Helvatica", "20"), bg="black", fg="white", command=generation)

canvas.grid(column=0, rowspan=3)
boutton_generation.grid(row=0, column=1)




racine.mainloop()
