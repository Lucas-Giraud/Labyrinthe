# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 16:10:01 2022

@author: Lucas
"""

class Case:
    def _init_(self):
        self._haut = None
        self._droit =None
        self._bas = None
        self._gauche = None
        self._trouH=None
        self._trouD=None
        self._trouB=None
        self._trouG=None
        
    def getH(self):
        return self._haut
    
    def getD(self):
        return self._droit
    
    def getB(self):
        return self._bas

    def getG(self):
        return self._gauche
    
    def getTH(self):
        return self._trouH
    
    def getTD(self):
        return self._trouD
    
    def getTB(self):
        return self._trouB
    
    def getTG(self):
        return self._trouG
    
    def setH(self,v):
        self._haut = v
        
    def setD(self,v):
        self._droit = v
        
    def setB(self,v):
        self._bas = v
        
    def setG(self,v):
        self._gauche = v
            
    def setTH(self,b):
        self._trouH = b
        
    def setTD(self,b):
        self._trouD = b
        
    def setTB(self,b):
        self._trouB = b
        
    def setTG(self,b):
        self._trouG = b
        
    def stri(self):
        return "[H="+str(self._haut)+" D="+str(self._droit)+" B="+str(self._bas)+" G="+str(self._gauche)+"]"
    