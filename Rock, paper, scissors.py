# Juego de Rock, Paper or Scissors

import random
import time
import sys
print("Bienvenido a Rock, Paper or Scissors :)")
time.sleep(1)
print("Tiene tres opciones: Piedra, papel o tijera")
time.sleep(2)
print("Para salir del juego, escriba \"Salir\"")
time.sleep(2)
numero_random = random.randint(1, 3)
rock = 1
paper = 2
scissors = 3
pregunta_inicio = input("Escriba \"Jugar\" para iniciar a jugar: ")
volver_empezar = "Volvamos a empezar"
cont = 1

jugada_anterior = None
# Para Iniciar el juego
while True:
    if pregunta_inicio.lower() == 'jugar':
        print("Recuerda que solo tienes 3 oportunidades, asi que aprovechalas bien")
        while cont <= 3:
            while True:
                numero_random = random.randint(1, 3)
                if numero_random != jugada_anterior:
                    break

            if numero_random == rock:
                print("El sistema te lanza Piedra")
            elif numero_random == paper:
                print("El sistema te lanza Papel")
            elif numero_random == scissors:
                print("El sistema te lanza tijeras")
            seleccion_user = input("Ingrese su opcion correspondiente: ")
            seleccion = seleccion_user.lower()
            if seleccion == "salir":
                print("Saliendo del juego...")
                print("Ha salido satisfactoriamente del juego :)")
                sys.exit()
            # este es para roca, que le gana el papel
            if numero_random == rock and seleccion == "papel":
                print("Mierda, me ganaste :( ")
                print()
            elif numero_random == rock and (seleccion == "tijera" or seleccion == "tijeras" or seleccion == "piedra"):
                print("Te gane compare, tienes que practicar mas :) ")
                print()
            # esta es para papel, que le gana la tijera
            elif numero_random == paper and (seleccion == "tijeras" or seleccion == "tijera"):
                print("Mierda, me ganaste :( ")
                print()
            elif numero_random == paper and (seleccion == "papel" or seleccion == "piedra"):
                print("Te gane compare, tienes que practicar mas :) ")
                print()
            # esta es para tijera, que le gana la piedra
            elif numero_random == scissors and seleccion == "piedra":
                print("Mierda, me ganaste :( ")
                print()
            elif numero_random == scissors and (seleccion == "papel" or seleccion == "tijeras" or seleccion == "tijera"):
                print("Te gane compare, tienes que practicar mas :) ")
                print()

            cont += 1
        while cont > 3:
            print('Quieres volver a empezar??')
            pregunta = input("SI / NO : ")
            print()
            if pregunta.lower() == "si":
                cont = 1
                print(volver_empezar)
                break
            else:
                print("Saliendo del juego...")
                print("Ha salido satisfactoriamente del juego :)")
                sys.exit()

    elif pregunta_inicio.lower() == 'salir':
        print("Saliendo del juego...")
        print("Ha salido satisfactoriamente del juego :)")
        sys.exit()
