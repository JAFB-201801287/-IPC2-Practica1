# -*- coding: utf-8 -*-

class CandidatoController():
    __instance = None
    index = 0
    candidatos = []
    puestos = []

    def get(self):
        return self.candidatos

    def getPuestos(self):
        return self.puestos

# Constructor ----------------------------------------

    def __str__(self):
        return self.candidatos

    def __new__(cls):
        if CandidatoController.__instance is None:
            CandidatoController.__instance = object.__new__(cls)
        return CandidatoController.__instance

    def __init__(self):
        self.id = 0

# Metodos ---------------------------------------------

    def add(self, candidato):
        self.candidatos.append(candidato)
        self.addPuesto(candidato.getPuesto())

    def find(self, id):
        for candidato in self.candidatos:
            if(candidato.getId() == id):
                return True
        return False

    def addPuesto(self, puesto):
        if(self.findPuesto(puesto) != True):
            self.puestos.append(puesto)

    def findPuesto(self, puesto):
        for p in self.puestos:
            if(p == puesto):
                return True
        return False