# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 15:53:55 2022

@author: Lucas
"""

from Case import*
import random
import turtle as t



"""
Question a
"""
def Grille(l,c):
    Grille=[]
    for i in range(0,l):
        ligne=[]
        for j in range(0,c):
            case=Case()
            case.setTH(False)
            case.setTD(False)
            case.setTB(False)
            case.setTG(False)
            if i==0 and j==0:#case en haut à gauche 
                case.setH(random.randint(1,5))
                case.setD(random.randint(1,5))
                case.setB(random.randint(1,5))
                case.setG(random.randint(1,5))
            elif i==0 and j>0:#ligne du haut 
                case.setH(random.randint(1,5))
                case.setD(random.randint(1,5))
                case.setB(random.randint(1,5))
                case.setG(ligne[j-1].getD())
            elif i>0 and j==0:#colonne de gauche
                case.setH(Grille[i-1][j].getB())
                case.setD(random.randint(1,5))
                case.setB(random.randint(1,5))
                case.setG(random.randint(1,5))            
            elif i>0 and j>0:#les autres cases
                case.setH(Grille[i-1][j].getB())
                case.setD(random.randint(1,5))
                case.setB(random.randint(1,5))
                case.setG(ligne[j-1].getD()) 
            ligne.append(case)
        Grille.append(ligne)  #ajout de la ligne nouvellement créée danss la graille         
    return Grille

"""
Question b
"""

def affiche(G):#parcours la grille et récupère les informations de chaque case avec la fonction stri
    s=""
    for L in G:
        for i in range(0,len(L)):
            s+=L[i].stri()
        s+="\n"
    print(s)

def dessin(G):#dessine chaque mur de chaque case avec la bonne epaisseur
    t.TurtleScreen._RUNNING=True
    tw = t.Screen()
    t.speed(0)
    for i in range(0,len(G)):
        ligne=G[i]
        for j in range(0,len(ligne)):
            t.up()
            t.goto(j*50-200,i*(-50)+200)
            t.down()
            t.width(ligne[j].getH()*2)
            t.forward(50)
            t.right(90)
            t.width(ligne[j].getD()*2)
            t.forward(50)
            t.right(90)
            t.width(ligne[j].getB()*2)
            t.forward(50)
            t.right(90)
            t.width(ligne[j].getG()*2)
            t.forward(50)
            t.right(90)
    tw.exitonclick()
    
G=Grille(3,4)   
print(affiche(G))
dessin(G)


