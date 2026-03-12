'''
====================================================
ARCHIVO 4 DE 4: main.py
====================================================

¿Para qué sirve este archivo?
Este es el PROGRAMA PRINCIPAL. Es el único archivo
que ejecutas directamente desde la terminal:

    python3 main.py

main.py importa todo lo que hemos creado en los
otros tres archivos y coordina el flujo del juego.

Flujo del programa:
  1. Bienvenida
  2. Crear los dos tableros vacíos
  3. Colocar los barcos en cada tablero
  4. Bucle principal: turnos hasta que alguien gane
====================================================
'''

from variables import DIMENSIONES, BARCOS
from clases    import Tablero
from funciones import bienvenida, colocar_barcos, turno_jugador, turno_maquina


# ==================================================
# FUNCIÓN PRINCIPAL: main()
# ==================================================

def main():

    # --------------------------------------------------
    # PASO 1: BIENVENIDA
    # --------------------------------------------------

    bienvenida()


    # --------------------------------------------------
    # PASO 2: CREAR LOS TABLEROS VACÍOS
    # --------------------------------------------------
    # Tablero() solo crea la cuadrícula vacía (todo AGUA).
    # Los barcos los colocamos en el siguiente paso.

    print("\n  Preparando los tableros...")

    tablero_jugador = Tablero("Tú",      DIMENSIONES)
    tablero_maquina = Tablero("Maquina", DIMENSIONES)


    # --------------------------------------------------
    # PASO 3: COLOCAR LOS BARCOS
    # --------------------------------------------------
    # colocar_barcos() recibe un tablero y el diccionario
    # de barcos, y los coloca aleatoriamente.
    # También actualiza las vidas del tablero (20 en total).

    colocar_barcos(tablero_jugador, BARCOS)
    colocar_barcos(tablero_maquina, BARCOS)

    print("  Tableros listos. Cada jugador tiene " + str(tablero_jugador.vidas) + " vidas.")


    # --------------------------------------------------
    # PASO 4: BUCLE PRINCIPAL DEL JUEGO
    # --------------------------------------------------
    # El while True corre indefinidamente.
    # Salimos con "break" cuando alguien gana.
    # La variable "turno" decide de quién es cada vuelta.

    turno = "jugador"   # el jugador humano empieza siempre primero

    while True:


        # ---- TURNO DEL JUGADOR ----

        if turno == "jugador":

            acerto = turno_jugador(tablero_maquina, tablero_jugador)

            if tablero_maquina.esta_hundido() == True:
                print("\n" + "=" * 50)
                print("  ¡HAS GANADO! Has hundido todos los barcos enemigos.")
                print("=" * 50)
                break

            if acerto == True:
                turno = "jugador"   # acertó -> repite
            else:
                turno = "maquina"   # falló  -> le toca a la máquina


        # ---- TURNO DE LA MÁQUINA ----

        elif turno == "maquina":

            acerto = turno_maquina(tablero_jugador)

            if tablero_jugador.esta_hundido() == True:
                print("\n" + "=" * 50)
                print("  HAS PERDIDO ☠️ La maquina ha hundido todos tus barcos.")
                print("=" * 50)
                break

            if acerto == True:
                turno = "maquina"   # acertó -> repite
            else:
                turno = "jugador"   # falló  -> vuelve el jugador


    print("\n  Gracias por jugar. Hasta la proxima!")


# ==================================================
# PUNTO DE ENTRADA
# ==================================================
# Cuando ejecutas "python3 main.py", Python pone
# __name__ = "__main__" automáticamente.
# El if lo detecta y llama a main() para arrancar. - CLAUDE IA

if __name__ == "__main__":
    main()
