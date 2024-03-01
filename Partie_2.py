# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 11:47:38 2022

@author: Lucas
"""

from Partie_1 import*

"""
Question b
"""

def Graphe(G):
    Gr=dict()#créer dico
    ligne=G[0]
    lg=len(G)
    l=len(ligne)
    Gr["e1"]=[(0,G[0][0].getH())]#met les deux entrées et l'epaisseur de mur associée
    Gr["e2"]=[(0,G[0][0].getG())]
    Gr["s1"]=[]#les deux sorties sans valeur car on ne peux pas entrer par elles
    Gr["s2"]=[]
    for i in range(0,lg):#parcours de la grille et ajout de l'epaisseur des murs adjacents à la case
        ligne=G[i]
        for j in range(0,l):
            if i==0 and j==0:#coin haut gauche
                Gr[i*l+j]=[ ((i*l+j+1),ligne[j].getD()),(((i+1)*l+j),ligne[j].getB()) ]
            elif i==0 and j==l-1:#coin haut droit
                Gr[i*l+j]=[ (((i+1)*l+j),ligne[j].getB()),((i*l+j-1),ligne[j].getG()) ]
            elif i==lg-1 and j==l-1:#coin bas droit
                Gr[i*l+j]=[ (((i-1)*l+j),ligne[j].getH()),((i*l+j-1),ligne[j].getG()),("s1",ligne[j].getD()),("s2",ligne[j].getB())]
            elif i==lg-1 and j==0:#coin bas gauche
                Gr[i*l+j]=[ ((i*l+j+1),ligne[j].getD()),(((i-1)*l+j),ligne[j].getH()) ]
            elif i==0 and j>0:#ligne haut
                Gr[i*l+j]=[ ((i*l+j+1),ligne[j].getD()),(((i+1)*l+j),ligne[j].getB()),((i*l+j-1),ligne[j].getG()) ]
            elif i==lg-1 and j>0:#ligne bas
                Gr[i*l+j]=[ (((i-1)*l+j),ligne[j].getH()),((i*l+j+1),ligne[j].getD()),((i*l+j-1),ligne[j].getG()) ]
            elif i>0 and j==0:#colone gauche
                Gr[i*l+j]=[ (((i-1)*l+j),ligne[j].getH()),((i*l+j+1),ligne[j].getD()),(((i+1)*l+j),ligne[j].getB()) ]
            elif i>0 and j==l-1:#colone droit
                Gr[i*l+j]=[ (((i-1)*l+j),ligne[j].getH()),(((i+1)*l+j),ligne[j].getB()),((i*l+j-1),ligne[j].getG()) ]
            elif i>0 and j>0:#le reste
                Gr[i*l+j]=[ (((i-1)*l+j),ligne[j].getH()),((i*l+j+1),ligne[j].getD()),(((i+1)*l+j),ligne[j].getB()),((i*l+j-1),ligne[j].getG()) ]
    return Gr

"""
Question d
"""

def minimum(dico):
    m=float('inf')
    i=list(dico.keys())[0]#ajouté pour eviter erreur transfo graphe en liste des clés et prend le premier 
    for k in dico:
        if dico[k] < m:
            m=dico[k]
            i=k
    return i

def chemin(G,deb,fin):#Dijkstra + A* sans heurisitique
    D={}
    poubelle={}
    if fin=="s1":
        poubelle["s2"]=[]
    else:
        poubelle["s1"]=[]
    d={k: float('inf') for k in G} 
    d[deb]=0 
    P={}
    while fin in d: 
        k=minimum(d) 
        for i in range(len(G[k])): 
            v, c = G[k][i]
            if (v not in D) and (v not in poubelle):
                if d[v]>d[k]+c:
                    d[v]=d[k]+c
                    P[v]=k
        D[k]=d[k] 
        del(d[k])
    return D,P

def chemin_court(chem11,chem12,chem21,chem22,p11,p12,p21,p22):#regarde quel chemin est plus court en comparant les couts totaux de chaque chemin
    s11=chem11["s1"]
    s12=chem12["s2"]
    s21=chem21["s1"]
    s22=chem22["s2"]
    
    if (s11<=s12 and s11<s21 and s11<s22) or (s11==s12 and s21==s22 and s12==s21) or (s11<s12 and s11==s21 and s12==s22) or (s11<s12 and s11==s22 and s12==s21):
        return transfo(p11),s11
    elif (s12<=s11 and s12<s21 and s12<s22) or (s11>s12 and s11==s21 and s12==s22) or (s11>s12 and s11==s22 and s12==s21):
        return transfo(p12),s12
    elif s21<s11 and s21<s12 and s21<=s22:
        return transfo(p21),s21
    elif s22<s11 and s22<s12 and s22<=s21:
        return transfo(p22),s22

    
def transfo(pre):#renvoie le chemin sous forme d'une liste
    k=list(pre.keys())
    c=[k[len(k)-1]]
    chemin=[]
    i=-1
    while c[i]!=0:#rempli c avec le précédent de chaque case qui compose le chemin en partant de la fin 
        i+=1
        c.append(pre[c[i]])
    for i in range(len(c)-1,-1,-1):#retourne la liste pour avoir le chemin dans le bon sens 
        chemin.append(c[i])
    
    return chemin

def coo(chemin,grille):
    chem=[chemin[0]]
    for i in range(1,len(chemin)-1):
        c=chemin[i]
        for j in range(0,len(grille)):
            ligne=grille[j]
            for k in range(0,len(ligne)):
                if c==j*len(ligne)+k:
                    chem.append((j,k))
    chem.append(chemin[len(chemin)-1])
    return chem
 
#affiche tout pour test 
grille=Grille(3,3)
affiche(grille)
graphe=Graphe(grille)
print(graphe)
chem11, p11=chemin(graphe,"e1","s1")
chem12, p12=chemin(graphe,"e1","s2")
chem21, p21=chemin(graphe,"e2","s1")
chem22, p22=chemin(graphe,"e2","s2")
L,cout=chemin_court(chem11, chem12, chem21, chem22, p11, p12, p21, p22)
print("Le chemin le plus court est "+str(L)+" avec un coût de "+str(cout))

#ca c etait pour m'aider a voir si mes fonctions marchaient
print("chem11 "+str(chem11))
print("chem12 "+str(chem12))
print("chem21 "+str(chem21))
print("chem22 "+str(chem22))
print("p11 "+str(p11))
print("p12 "+str(p12))
print("p21 "+str(p21))
print("p22 "+str(p22))
dessin(grille)
t.done()
