# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 07:31:47 2021

@author: Emilio Porras
"""
from zooAnimales.animal import Animal

class Mamifero(Animal):
    _listado = list()
    caballos = 0
    leones = 0
    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        _pelaje = pelaje
        _patas = patas
        self._listado.append(self)
        
    @classmethod    
    def cantidadMamiferos(cls):
        return len(cls._listado)
    
    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        cls.caballos += 1
        return Mamifero(nombre, edad, "pradera", genero, True, 4)
    
    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        cls.leones += 1
        return Mamifero(nombre, edad, "selva", genero, True, 4)
        
    