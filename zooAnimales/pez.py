# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 07:31:49 2021

@author: Emilio Porras
"""

from zooAnimales.animal import Animal

class Pez(Animal):
    _listado = list()
    salmones = 0
    bacalaos = 0
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        self._listado.append(self)
        
    @classmethod    
    def cantidadPeces(cls):
        return len(cls._listado)
    
    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        cls.salmones += 1
        return Pez(nombre, edad, "oceano", genero, "rojo", 6)
    
    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        cls.bacalaos += 1
        return Pez(nombre, edad, "oceano", genero, "gris", 6)
    
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
        
    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def setCantidadAletas(self,x):
        self._cantidadAletas = x