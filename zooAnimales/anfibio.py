# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 07:31:49 2021

@author: Emilio Porras
"""

from zooAnimales.animal import Animal

class Anfibio(Animal):
    _listado = list()
    ranas = 0
    salamandras = 0
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        _colorPiel = colorPiel
        _venenoso = venenoso
        self._listado.append(self)
        
    @classmethod    
    def cantidadMamiferos(cls):
        return len(cls._listado)
    
    @classmethod
    def crearRana(cls, nombre, edad, genero):
        cls.ranas += 1
        return Anfibio(nombre, edad, "selva", genero, "rojo", True)
    
    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        cls.salamandras += 1
        return Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)