# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 07:31:48 2021

@author: Emilio Porras
"""
from zooAnimales.animal import Animal

class Ave(Animal):
    _listado = list()
    halcones = 0
    aguilas = 0
    
    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        _colorPlumas = colorPlumas
        self._listado.append(self)
        
    @classmethod    
    def cantidadAves(cls):
        return len(cls._listado)
    
    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        cls.halcones += 1
        return Ave(nombre, edad, "montanas", genero, "cafe glorioso")
    
    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        cls.aguilas += 1
        return Ave(nombre, edad, "montanas", genero, "blanco y amarillo")