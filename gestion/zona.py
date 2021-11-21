# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 08:19:49 2021

@author: Emilio Porras
"""
from zooAnimales import *

class Zona:
    def __init__(self, nombre=None, zoo=None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = list()
        
    def agregarAnimales(self, animal):
        self._animales.append(animal)
        animal.setZona(self)
        
    def cantidadAnimales(self):
        return len(self._animales)
    
    def getNombre(self):
        return self._nombre
    
    def getZoologico(self):
        return self._zoo
    
    def getAnimales(self):
        return self._animales
    
    def getZoo(self):
        return self._zoo
    
    def setZoo(self, x):
        self._zoo = x
        
    def setNombre(self, x):
        self._nombre = x
        
    def setAnimales(self, x):
        self._animales = x