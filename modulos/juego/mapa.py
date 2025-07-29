import os
from modulos.menu import cargar_menu
#Hacemos visible e invisible los items 
WIDTH_MAPA = 25
HEIHT_MAPA = 15

espacio_invisible = "   "
espacio_visible = "[  ]"

coordenada_personaje = [5,15]
personaje = "🡹"

def cargar_mapa(movimiento_personaje):
    
    # Menú
    #cargar_menu()
    
    os.system("cls")
    if movimiento_personaje == "w":
        personaje = "🡹"
        coordenada_personaje[0] -= 1
    elif movimiento_personaje == "s":
        personaje = "🡻"
        coordenada_personaje[0] += 1
    elif movimiento_personaje == "a":
        personaje = "🡸"
        coordenada_personaje[1] -= 1
    elif movimiento_personaje == "d":
        personaje = "🡺"
        coordenada_personaje[1] += 1
        
    
    
#Damos indicaciobes de los items
    print("+"  + "-"*75 + "+")
    for cada_final in range(HEIHT_MAPA):
        print("|", end= "")
        for cada_item in range(WIDTH_MAPA):
            if(coordenada_personaje[0] == cada_final and coordenada_personaje[1]== cada_item):
                print(f" {personaje} ", end= "")
            else: 
                print(espacio_invisible, end="")
        #Imrprime nada     
        print("|")
    print("+"  + "-"*75 + "+")