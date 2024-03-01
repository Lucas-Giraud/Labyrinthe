# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 14:30:24 2022

@author: Lucas
"""

from Partie_2 import*
import turtle as t
t.speed

"""
Question a
"""

def trou_grille(grille, chemin):#modifie les attributs trou de case pour indiquer quel mur est percé
    if chemin[0]=="e1":
        grille[0][0].setTH(True)
    else:
        grille[0][0].setTG(True)       
    ligne=grille[len(grille)-1]  
    if chemin[len(chemin)-1]=="s1":
        ligne[len(ligne)-1].setTD(True)
    else:
        ligne[len(ligne)-1].setTB(True)    
    for i in range(1,len(chemin)-2):
        c1=chemin[i]
        c2=chemin[i+1]
        t=c1-c2
        for j in range(0,len(grille)):
            ligne=grille[j]
            for k in range(0,len(ligne)):
                if i==len(chemin)-3 and j==len(grille)-1 and k==len(ligne)-1:
                    if t==-1:
                        ligne[k].setTG(True)
                    elif t==-len(ligne):
                        ligne[k].setTH(True)
                if c1==j*len(ligne)+k:
                    if t==-len(ligne):
                        ligne[k].setTB(True)
                        grille[j+1][k].setTH(True)
                    elif t==-1:
                        ligne[k].setTD(True)
                        grille[j][k+1].setTG(True)
                    elif t==1:
                        ligne[k].setTG(True)
                        grille[j][k-1].setTD(True)
                    elif t==len(ligne):
                        ligne[k].setTH(True)
                        grille[j-1][k].setTB(True)
        
"""
Question b
"""

def dessin_v2(G):#dessine chaque mur de chaque case avec la bonne epaisseur et un trou au milieu si il attribut trou de case a True
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
            if ligne[j].getTH():
                t.forward(15)
                t.up()
                t.forward(20)
                t.down()
                t.forward(15)
            else:
                t.forward(50)
            t.right(90)
            t.width(ligne[j].getD()*2)
            if ligne[j].getTD():
                t.forward(15)
                t.up()
                t.forward(20)
                t.down()
                t.forward(15)
            else:
                t.forward(50)
            t.right(90)
            t.width(ligne[j].getB()*2)
            if ligne[j].getTB():
                t.forward(15)
                t.up()
                t.forward(20)
                t.down()
                t.forward(15)
            else:
                t.forward(50)
            t.right(90)
            t.width(ligne[j].getG()*2)
            if ligne[j].getTG():
                t.forward(15)
                t.up()
                t.forward(20)
                t.down()
                t.forward(15)
            else:
                t.forward(50)
            t.right(90)
    tw.exitonclick()


        

"""test
grille=Grille(3,3)
affiche(grille)
graphe=Graphe(grille)
chem11, p11=chemin(graphe,"e1","s1")
chem12, p12=chemin(graphe,"e1","s2")
chem21, p21=chemin(graphe,"e2","s1")
chem22, p22=chemin(graphe,"e2","s2")

L,cout=chemin_court(chem11, chem12, chem21, chem22, p11, p12, p21, p22)
print("Le chemin le plus court est "+str(L)+" avec un coût de "+str(cout))
trou_grille(grille, L)
dessin_v2(grille)
t.done
"""