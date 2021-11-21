# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 08:19:49 2021

@author: Emilio Porras
"""
from gestion.zoologico import Zoologico

class Zona:
    def __init__(self, nombre, zoo):
        _nombre = nombre
        _zoo = zoo
        _animales = list()
        
    def agregarAnimales(self, animal):
        self._animales.append(animal)
        animal.setZona(self)
        
    def cantidadAnimales(self):
        return len(self._animales)