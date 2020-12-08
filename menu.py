# -*- coding: utf-8 -*-

import os

def clean():  # Metodo para limpiar pantalla
    os.system("cls")

def caratula():
    clean()
    print("==".center(150, "="))
    print("\tIPC2")
    print("\tJose Andres Flores Barco")
    print("\t201801287")
    print("==".title().center(150, "="))

def menu():
    opcionMenu = 0
    caratula()
    while True:
        print(" Menu ".title().center(150, "="))
        print("\t1) - Lectura de archivo CSV:")
        print("\t2) - Cálculo de Datos:")
        print("\t3) - Generación de archivo JSON.:")
        print("\t4) - Salir:".title())
        print("")

        # solicituamos una opción al usuario
        opcionMenu = input("inserta un numero valor >> ")
        print("".center(150, "_"))
        if opcionMenu == "1":
            continue
        elif opcionMenu == "2":
            continue
        elif opcionMenu == "3":
            continue
        elif opcionMenu == "4":
            break
        else:
            print("")
            input(
                "No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")