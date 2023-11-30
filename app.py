#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

#nesesito hacer un minijuego de piedra papel o tijera que se ejecute en la consola
#crea las variables con su  valor correspondiente
piedra = 1
papel = 2
tijera = 3

player1 = 0
player2 = 0
print("Vamos a jugar piedra, papel o tijera")
#encapsula los print desde el que dice escribe el numero correspondiente a su eleccion hasta el print de tijera para poder usarlo si lo nesecito
def menu():
    print("Escribe el numero correspondiente a su eleccion:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
def menu2(p1, p2):  
    menu()

    #creo una variable que guarde la eleccion del usuario
    eleccion = int(input())

    # crea un bucle para que el usuario no pueda poner un número mayor a 3 ni menor a 1 y se vuelva a llamar a menu
    while eleccion > 3 or eleccion < 1:
        print("Ese número no es válido, vuelve a intentarlo")
        menu()
        eleccion = int(input())

    # Creo una variable que guarde la elección del oponente
    from random import randint
    eleccion_aleatoria = randint(1, 3)


    # crea la lógica del juego para saber quién gana
    if eleccion == eleccion_aleatoria:
        print("Empate")
        #muestrame la eleccion de ambos pero que se muestre el nombre de la variable no el numero
        if eleccion == 1:
            print("Ambos eligieron Piedra")
        if eleccion == 2:   
            print("Ambos eligieron Papel")
        if eleccion == 3:
            print("Ambos eligieron Tijera")
    if (
        (eleccion == 1 and eleccion_aleatoria == 2) or 
        (eleccion == 2 and eleccion_aleatoria == 3) or 
        (eleccion == 3 and eleccion_aleatoria == 1)
    ):
        #muestrame la eleccion de ambos pero que se muestre el nombre de la variable no el numero
        if eleccion == 1:
            print("Piedra vs Papel")
        if eleccion == 2:
            print("Papel vs Tijera")
        if eleccion == 3:
            print("Tijera vs Piedra")
        print("Perdiste")
        p2 += 1
        
    if (
        (eleccion == 1 and eleccion_aleatoria == 3) or 
        (eleccion == 2 and eleccion_aleatoria == 1) or 
        (eleccion == 3 and eleccion_aleatoria == 2)
    ):
        #muestrame la eleccion de ambos pero que se muestre el nombre de la variable no el numero
        if eleccion == 1:
            print("Piedra vs Tijera")
        if eleccion == 2:
            print("Papel vs Piedra")
        if eleccion == 3:
            print("Tijera vs Papel")
        print("Ganaste")
        p1 += 1
    return p1, p2
   
player1, player2 = menu2(player1, player2)
print("Tú: " + str(player1) + " | " + "Oponente: " + str(player2))


# crea un bucle para que el usuario pueda volver a jugar
while True:
    print("¿Quieres volver a jugar? (s/n)")
    respuesta = input()
    if respuesta == "s":
        player1, player2 = menu2(player1, player2)
        print("Tú: " + str(player1) + " | " + "Oponente: " + str(player2))
    elif respuesta == "n":
        print("Gracias por jugar")
        break
    else:
        print("Esa respuesta no es válida, vuelve a intentarlo")