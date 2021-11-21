# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 08:19:48 2021

@author: Emilio Porras
"""

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
    
    def getNombre(self):
        return self._nombre
    
    def getUbicacion(self):
        return self._ubicacion
    
    def getZona(self):
        return self._zonas
    
    def setNombre(self, x):
        self._nombre = x
        
    def setUbicacion(self, x):
        self._ubicacion = x
        
    def setZonas(self, x):
        self._zonas = x