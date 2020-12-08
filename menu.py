# -*- coding: utf-8 -*-

import os
import json

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
    while True:
        caratula()
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
            calcularDatos()
        elif opcionMenu == "3":
            escribirArchivo()
        elif opcionMenu == "4":
            break
        else:
            print("")
            input("NO SE PULSO NINGUNA OPCION CORRECTA...\nPULSA CUALQUIER TECLA PARA CONTINUAR")
        clean()

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
            candidato.setId(dato[0].strip())
            candidato.setNombre(dato[1].strip())
            candidato.setApellido(dato[2].strip())
            candidato.setEdad(dato[3].strip())
            candidato.setPuesto(dato[4].strip())
            candidato.setSalario(dato[5].strip())
            
            print('')
            print('CANDIDATO ------------------------------------------------------')
            print(f'ID: {candidato.getId()}')
            print(f'NOMBRE: {candidato.getNombre()}')
            print(f'APELLIDO: {candidato.getApellido()}')
            print(f'EDAD: {candidato.getEdad()}')
            print(f'PUESTO AL QUE APLICA: {candidato.getPuesto()}')
            print(f'PRETENCION SALARIAL: {candidato.getSalario()}')

            if(controlador_candidato.find(candidato.getId()) == False):
                controlador_candidato.add(candidato)
                print('ESTADO: ACEPTADO')
            else:
                print('ESTADO: NO ACEPTADO')

            

    print("")
    input("PULSA CUALQUIER TECLA PARA CONTINUAR")

def calcularDatos():
    puestos = controlador_candidato.getPuestos()
    candidatos = controlador_candidato.get()

    for puesto in puestos:
        cantidad_candidatos = 0
        edad_promedio = 0
        salario_promedio = 0

        for candidato in candidatos:
            if(candidato.getPuesto() == puesto):
                cantidad_candidatos += 1
                edad_promedio += int(candidato.getEdad())
                salario_promedio += float(candidato.getSalario())
        if(cantidad_candidatos > 0):
            print('')
            print(puesto.upper().ljust(150, '-'))
            print(f'CANTIDAD DE CANDIDATOS: {str(cantidad_candidatos)}')
            print(f'EDAD PROMEDIO: {str(float("{:.2f}".format(edad_promedio/cantidad_candidatos)))}')
            print(f'PRETENSION SALARIAL PROMEDIO: {str(float("{:.2f}".format(salario_promedio/cantidad_candidatos)))}')


    print("")
    input("PULSA CUALQUIER TECLA PARA CONTINUAR")

# METODO PARA LEER ARCHIVO JSON
def escribirArchivo():
    data = {}
    puestos = controlador_candidato.getPuestos()
    candidatos = controlador_candidato.get()
    
    for puesto in puestos:
        cantidad_candidatos = 0
        edad_promedio = 0
        salario_promedio = 0

        for candidato in candidatos:
            if(candidato.getPuesto() == puesto):
                cantidad_candidatos += 1
                edad_promedio += int(candidato.getEdad())
                salario_promedio += float(candidato.getSalario())

        if(cantidad_candidatos > 0):
            data[puesto] = []
            data[puesto].append({
                'Candidatos': cantidad_candidatos,
                'Edad Promedio': float("{:.2f}".format(edad_promedio/cantidad_candidatos)),
                'Pretensión Salarial': float("{:.2f}".format(salario_promedio/cantidad_candidatos))
            })
            print('')
            print(puesto.upper().ljust(150, '-'))
            print(f'CANTIDAD DE CANDIDATOS: {str(cantidad_candidatos)}')
            print(f'EDAD PROMEDIO: {str(float("{:.2f}".format(edad_promedio/cantidad_candidatos)))}')
            print(f'PRETENSION SALARIAL PROMEDIO: {str(float("{:.2f}".format(salario_promedio/cantidad_candidatos)))}')

    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

    print("")
    input("PULSA CUALQUIER TECLA PARA CONTINUAR")



    