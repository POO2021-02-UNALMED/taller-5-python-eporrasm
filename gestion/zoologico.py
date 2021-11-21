# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 08:19:48 2021

@author: Emilio Porras
"""
from gestion.zona import Zona

class Zoologico:
    def __init__(self, nombre, ubicacion):
        _nombre = nombre
        _ubicacion = ubicacion
        _zonas = list()
        
    def agregerZonas(self, zona):
        self._zonas.append(zona)
        
    def cantidadTotalAnimales(self):
        suma = 0
        for zona in self._zonas:
            suma += zona.cantidadAnimales()
        return suma