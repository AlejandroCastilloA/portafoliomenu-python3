import os
import readchar
from juego.mapa import cargar_mapa


estado_juego = True  

def juego_1():
    
#iniciar juego
    tecla = readchar.readchar()

    if tecla in ("w", "s", "a", "d","q"): 
        cargar_mapa(tecla) 
    elif tecla == "q":
        estado_juego = False


while estado_juego:
    juego_1()
