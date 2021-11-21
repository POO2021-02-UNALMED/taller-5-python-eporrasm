# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 07:27:06 2021

@author: Emilio Porras
"""
from gestion import *

class Animal:
    _totalAnimales = 0
    def __init__(self, nombre, edad, habitat, genero):
        _nombre = nombre
        _edad = edad
        _habitat = habitat
        _genero = genero
        _zona = None
        self._totalAnimales += 1
        
    def setZona(self, zona):
        self._zona = zona
        
    @staticmethod
    def totalPorTipo():
        return "Mamiferos: {}\nAves: {}\nReptiles: {}\nPeces: {}\nAnfibios: {}".format(
                Mamifero.cantidadMamiferos(), Ave.cantidadAves(), Reptil.cantidadReptiles(),
                Pez.cantidadPeces(), Anfibio.cantidadAnfibios()) 
				
    def toString(self):
        if self._zona == None:
            return "Mi nombre es "+str(self._nombre)+", tengo una edad de "+str(self._edad)+", habito en "+self._habitat+" y mi genero es "+str(self._genero)
        else:
            return "Mi nombre es "+str(self._nombre)+", tengo una edad de "+str(self._edad)+", habito en "+self._habitat+" y mi genero es "+str(self._genero)+", la zona en la que me ubico es "+str(self._zona)+" en el "+str(self._zona.getZoologico())
    