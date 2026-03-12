# main_mini.py
import funciones_mini # IMPORTANTE: Traemos las herramientas del otro archivo

# Iniciamos el tablero llamando a la función
tablero = funciones_mini.crear_tablero()

# Colocamos los barcos en posiciones fijas como pide el ejercicio
# Barco de 4 horizontal
tablero[1][0], tablero[1][1], tablero[1][2], tablero[1][3] = "B", "B", "B", "B"
# Barco de 3 vertical
tablero[3][3], tablero[4][3], tablero[5][3] = "B", "B", "B"

print("--- MINI HUNDIR LA FLOTA ---")

# Bucle para disparar
while True:
    funciones_mini.mostrar(tablero) # Enseñamos el tablero
    
    # Pedimos coordenadas
    f = int(input("Introduce fila (0-9): "))
    c = int(input("Introduce columna (0-9): "))
    
    # Ejecutamos la lógica del disparo
    acierto = funciones_mini.disparar(tablero, f, c)
    
    if acierto:
        print("¡TOCADO!")
    else:
        print("Agua. Fin de la prueba.")
        break # El mini ejercicio dice que paremos al fallar