# -*- coding: utf-8 -*-

class Candidato():

    def __init__(self):
        self.id = ""
        self.nombre = ""
        self.apellido = ""
        self.edad = 0
        self.puesto = ""
        self.salario = 0.0

# SETTERS

    def setId(self, id):
        self.id = id

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setEdad(self, edad):
        self.edad = edad

    def setPuesto(self, puesto):
        self.puesto = puesto

    def setSalario(self, salario):
        self.salario = salario

# GETTERS

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def getEdad(self):
        return self.edad
    
    def getPuesto(self):
        return self.puesto
    
    def getSalario(self):
        return self.salario