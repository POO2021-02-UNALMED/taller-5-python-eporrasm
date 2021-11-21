# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 07:31:48 2021

@author: Emilio Porras
"""
from zooAnimales.animal import Animal

class Reptil(Animal):
    _listado = list()
    iguanas = 0
    serpientes = 0
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        _colorEscamas = colorEscamas
        _largoCola = largoCola
        self._listado.append(self)
        
    @classmethod    
    def cantidadReptiles(cls):
        return len(cls._listado)
    
    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        cls.iguanas += 1
        return Reptil(nombre, edad, "humedal", genero, "verde", 3)
    
    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        cls.serpientes += 1
        return Reptil(nombre, edad, "jungla", genero, "blanco", 1)
    
    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def setListado(cls, listado):
        cls._listado = listado
        
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self,x):
        self._colorEscamas = x
        
    def getLargoCola(self):
        return self._largoCola
    
    def setLargoCola(self,x):
        self._largoCola = x