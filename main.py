# Importando el modulo os
import os
from data.datos import lista_menu
from programas.Sumas import sumar2
from juego.juegos import juego_1

# Limpiar la Terminal
os.system("cls")

estado = True

# Bucle que depende de la variable de estado
while estado:
    print("+----------------------------------------------------------------------+")
    print("| ALEJANDRO                                             2025     v .1 |")
    print("|                                                                     |")       
    print(f"|[1]: {lista_menu[0]}")
    print(f"|[2]: {lista_menu[1]}")
    print(f"|[3]: {lista_menu[2]}")
    print(f"|[4]: {lista_menu[3]}")
    print(f"|[0]: Salir")
    # Recupera el dato ingresado
    
    opc = int(input("|[?]: "))

    # Pregunta si el dato ingresado es una de las opciones disponibles 
    if opc == 0:
        estado = False
    
    elif opc == 1:
        sumar2()   
    
    elif opc == 4:
        juego_1()

   
    # Limpiar la Terminal
    #os.system("cls")


print("[Saliendo del programa...]")