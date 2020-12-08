# -*- coding: utf-8 -*-

import os

import controller.candidatoController as CandidatoController
import model.candidato as Candidato

controlador_candidato = CandidatoController.CandidatoController()

def clean():  # Metodo para limpiar pantalla
    os.system("cls")

def caratula():
    clean()
    print("==".center(150, "="))
    print("\tIPC 2")
    print("\tJOSE ANDRES FLORES BARCO")
    print("\t201801287")
    print("==".title().center(150, "="))

def menu():
    opcionMenu = 0
    caratula()
    while True:
        print(" Menu ".title().center(150, "="))
        print("\t1) - LECTURA DE ARCHIVO CSV:")
        print("\t2) - CALCULO DE DATOS:")
        print("\t3) - GENERACION DE ARCHIVO JSON:")
        print("\t4) - SALIR:".title())
        print("")

        # solicituamos una opción al usuario
        opcionMenu = input("ESCRIBIR NUMERO DE LA OPCION >> ")
        print("".center(150, "_"))
        if opcionMenu == "1":
            ordenarInformacion()
        elif opcionMenu == "2":
            continue
        elif opcionMenu == "3":
            continue
        elif opcionMenu == "4":
            break
        else:
            print("")
            input("NO SE PULSO NINGUNA OPCION CORRECTA...\nPULSA CUALQUIER TECLA PARA CONTINUAR")

# METODO PARA LEER EL ARCHIVO CSV
def leerArchivo():
    temp = ""
    direccion = input("ESCRIBIR DIRECCION DEL ARCHIVO CSV >> ")
    with open(direccion, "r", encoding="utf-8") as f: 
        for line in f.readlines():
            temp += line

    return temp

def ordenarInformacion():
    informacion = leerArchivo()
    temp = informacion.split('\n')
    temp.pop(0)

    for datos in temp:
        if(datos != ''):
            dato = datos.split(',')
            candidato = Candidato.Candidato()
            candidato.setId(dato[0])
            candidato.setNombre(dato[1])
            candidato.setApellido(dato[2])
            candidato.setEdad(dato[3])
            candidato.setPuesto(dato[4])
            candidato.setSalario(dato[5])
            
            print('')
            print('CANDIDATO ------------------------------------------------------')
            print(f'ID: {candidato.getId()}')
            print(f'NOMBRE: {candidato.getNombre()}')
            print(f'APELLIDO: {candidato.getApellido()}')
            print(f'EDAD: {candidato.getEdad()}')
            print(f'PUESTO AL QUE APLICA: {candidato.getPuesto()}')
            print(f'PRETENCION SALARIAL: {candidato.getSalario()}')

            print(controlador_candidato.find(candidato.getId()))
            if(controlador_candidato.find(candidato.getId()) == False):
                controlador_candidato.add(candidato)
                print('ESTADO: ACEPTADO')
            else:
                print('ESTADO: NO ACEPTADO')

            

    print("")
    input("PULSA CUALQUIER TECLA PARA CONTINUAR")




    