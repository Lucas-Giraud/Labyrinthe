# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 16:13:05 2022

@author: Lucas
"""

from Partie_3 import*

print("Bonjour nobles explorateurs !")
print()
print("Vous avez fais appel à mes services pour vous aider à traverser la structure qui vous bloque le passage.")
print("En regardant avec précision votre scanner, ")
ligne=int(input("Veuillez m'indiquer combien de lignes de salles comporte cette structure : "))
colonne=int(input("ainsi que le nombre de colonnes de salles : "))
print("La structure ressmble-t-elle à ceci ?")
print("(Veuillez fermer le plan pour continuer)")
grille=Grille(ligne,colonne)
dessin(grille)
choix=int(input("1:OUI          2:NON\n"))
while choix==2:
    print("Je vous avais pourtant dit de regarder avec PRECISION...")
    ligne=int(input("Veuillez m'indiquer combien de lignes de salles comporte cette structure : "))
    colonne=int(input("ainsi que le nombre de olonnes de salles : "))
    print("La structure ressmble-t-elle à ceci ?")
    print("(Veuillez fermer le plan pour continuer)")
    grille=Grille(ligne,colonne)
    dessin(grille)
    
    choix=int(input("1:OUI          2:NON\n"))
print("Calcul de l'itinéraire en cours.....")
graphe=Graphe(grille)
chem11, p11=chemin(graphe,"e1","s1")
chem12, p12=chemin(graphe,"e1","s2")
chem21, p21=chemin(graphe,"e2","s1")
chem22, p22=chemin(graphe,"e2","s2")

chemin,cout=chemin_court(chem11, chem12, chem21, chem22, p11, p12, p21, p22)
trou_grille(grille, chemin)
chemin=coo(chemin,grille)
print("Le chemin le plus court est "+str(chemin)+" avec un coût de "+str(cout))
dessin_v2(grille)
t.done