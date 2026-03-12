'''
====================================================
ARCHIVO 3 DE 4: funciones.py
====================================================

¿Para qué sirve este archivo?
Aquí guardamos todas las funciones del juego.

Funciones que hay aquí:
  colocar_barcos()    -> coloca los barcos en un tablero
  bienvenida()        -> imprime el mensaje inicial
  pedir_coordenadas() -> pide fila y columna al jugador
  turno_jugador()     -> gestiona el turno del humano
  turno_maquina()     -> gestiona el turno de la máquina

¿Por qué no meter todo en main.py?
Porque si metemos todo en main.py ese archivo se
convierte en un bloque enorme imposible de leer.
Separando las funciones aquí, main.py queda limpio
y corto, y cada función tiene una tarea concreta.
====================================================
'''

import random   # para elegir posiciones y coordenadas aleatorias

from variables import DIMENSIONES, AGUA, BARCO, IMPACTO, FALLO, ORIENTACIONES


# ==================================================
# FUNCIÓN: colocar_barcos
# ==================================================

def colocar_barcos(tablero, barcos):
    '''
    Coloca todos los barcos del diccionario "barcos" en el
    tablero que recibe, de forma completamente aleatoria.

    Para cada barco del diccionario, repite este proceso:
      1. Elige una fila, columna y orientación al azar
      2. Calcula qué casillas ocuparía el barco desde ahí
      3. Comprueba que esas casillas sean válidas:
           - que no se salgan del tablero
           - que no haya otro barco encima
      4. Si no son válidas, vuelve al paso 1
      5. Si son válidas, pinta el barco en la cuadricula

    También suma las vidas: cada casilla con barco = 1 vida.

    Parámetros:
      tablero → el objeto Tablero donde colocar los barcos
      barcos  → el diccionario con nombre y eslora de cada barco

    NOTA: Al principio no comprobaba si la posición era válida.
    Los barcos se salían del tablero (casilla fila=11 que no existe)
    y se solapaban unos encima de otros. Lo arreglé añadiendo
    las comprobaciones antes de pintar cada barco.
    '''

    for nombre, eslora in barcos.items():
        # Para cada barco del diccionario, buscamos una posición válida

        colocado = False   # chivato: True cuando el barco ya está en el tablero

        while colocado == False:   # seguimos intentando hasta encontrar sitio

            # PASO 1: elegir posición y dirección al azar
            fila        = random.randint(0, DIMENSIONES - 1)   # número entre 0 y 9
            col         = random.randint(0, DIMENSIONES - 1)   # número entre 0 y 9
            orientacion = random.choice(ORIENTACIONES)          # "H" o "V"

            # PASO 2: calcular las casillas que ocuparía el barco
            # "H" Horizontal: fila no cambia, columna sube (col+0, col+1, col+2...)
            # "V" Vertical:   col no cambia, fila sube    (fila+0, fila+1, fila+2...)
            casillas = []

            if orientacion == "H":
                for i in range(eslora):
                    casillas.append((fila, col + i))
            else:
                for i in range(eslora):
                    casillas.append((fila + i, col))

            # PASO 3: comprobar que todas las casillas son válidas
            posicion_valida = True   # asumimos que sí, hasta encontrar un problema

            for (f, c) in casillas:
                if f >= DIMENSIONES or c >= DIMENSIONES:   # ¿se sale del tablero?
                    posicion_valida = False
                    break
                if tablero.grid[f][c] != AGUA:       # ¿hay otro barco encima?
                    posicion_valida = False
                    break

            # PASO 4 y 5: si es válida, pintamos el barco
            if posicion_valida == True:
                for (f, c) in casillas:
                    tablero.grid[f][c] = BARCO             # marcamos la casilla como barco
                tablero.vidas = tablero.vidas + eslora   # sumamos las vidas de este barco
                colocado = True                          # salimos del while


# ==================================================
# FUNCIÓN: bienvenida
# ==================================================

def bienvenida():
    '''
    Imprime el mensaje de bienvenida y las instrucciones.
    Solo se llama una vez, al principio de main.py.
    '''

    print("\n" + "🌊" * 50)
    print("  ⛴️ BIENVENIDX A HUNDIR LA FLOTA ⛴️ ")
    print("🌊" * 50)
    print("")
    print("INSTRUCCIONES:")
    print("  El tablero es de 10x10. Coordenadas del 0 al 9.")
    print("  Introduce fila y columna para disparar al enemigo.")
    print("")
    print("  Simbolos del tablero:")
    print("    ~  = agua donde nadie ha disparado todavía")
    print("    O  = tu barco (intacto)")
    print("    X  = impacto (barco tocado)")
    print("    .  = fallo (cayó al agua)")
    print("")
    print("  Si aciertas repites turno.")
    print("  Los dos jugadores tienen 20 vidas")
    print("  Gana quien hunda todos los barcos del rival.")
    print("")
    print("=" * 50)
    input("  Pulsa ENTER para comenzar...")


# ==================================================
# FUNCIÓN: pedir_coordenadas
# ==================================================

def pedir_coordenadas():
    '''
    Le pide al jugador que introduzca fila y columna.

    Valida dos cosas:
      1. Que el jugador escriba un número, no una letra.
         Si escribe "a", int() lanza un error ValueError.
         Lo capturamos con try/except para no romper el programa.

      2. Que el número esté entre 0 y 9 (dentro del tablero).

    Si algo falla, vuelve a preguntar (bucle while True).

    Devuelve una tupla (fila, col) con las coordenadas válidas.
    '''

    while True:   # seguimos preguntando hasta que el input sea correcto

        try:
            fila = int(input("  Introduce FILA (0-9): "))      # convertimos a entero
            col  = int(input("  Introduce COLUMNA (0-9): "))   # convertimos a entero

            if fila >= 0 and fila <= 9 and col >= 0 and col <= 9:
                return (fila, col)   # coordenadas válidas → las devolvemos
            else:
                print("  AVISO: Usa numeros del 0 al 9. Estás fuera del tablero.")

        except ValueError:
            # ValueError ocurre cuando int() recibe letras en vez de números
            # Por ejemplo: int("a") lanza ValueError
            print("  AVISO: Escribe solo números, sin letras.")


# ==================================================
# FUNCIÓN: turno_jugador
# ==================================================

def turno_jugador(tablero_maquina, tablero_jugador):
    '''
    Gestiona un turno completo del jugador humano:

      1. Muestra los dos tableros del jugador
      2. Pide coordenadas
      3. Procesa el disparo en el tablero de la máquina
      4. Anota el resultado en el seguimiento del jugador
      5. Informa del resultado

    Devuelve True si acertó (repite turno).
    Devuelve False si falló (le toca a la máquina).

    NOTA: Si el jugador dispara dos veces a la misma casilla,
    simplemente no pasa nada: recibir_disparo() ve que ya no
    hay BARCO y devuelve False (cuenta como fallo). No rompemos
    el programa, solo pierde el turno.
    '''

    print("\n" + "*" * 40)
    print("  ** TU TURNO **")
    print("*" * 40)

    tablero_jugador.mostrar_tableros()   # mostramos los tableros para que el jugador decida

    fila, col = pedir_coordenadas()   # pedimos coordenadas al jugador

    impacto = tablero_maquina.recibir_disparo(fila, col)     # procesamos el disparo
    tablero_jugador.marcar_vista(fila, col, impacto)         # anotamos en el seguimiento

    if impacto == True:
        print("\n  ¡IMPACTO en (" + str(fila) + "," + str(col) + ")! ¡Repites turno!")
        print("  Vidas del enemigo: " + str(tablero_maquina.vidas))
        return True   # el jugador repite turno

    else:
        print("\n  Agua en (" + str(fila) + "," + str(col) + "). Le toca a la máquina.")
        return False  # le toca a la máquina


# ==================================================
# FUNCIÓN: turno_maquina
# ==================================================

def turno_maquina(tablero_jugador):
    '''
    Gestiona un turno completo de la máquina.

    La máquina elige coordenadas al azar, pero nunca
    repite una casilla donde ya haya disparado.

    ¿Cómo evita repetir disparos?
    Con un bucle while que genera nuevas coordenadas
    hasta encontrar una casilla que aún sea AGUA en
    la cuadricula del jugador (= nunca disparada). - Gracias Claude ❤️🤖

    Devuelve True si acertó (repite turno).
    Devuelve False si falló (vuelve el jugador).

    NOTA: Al principio la máquina podía disparar dos veces
    a la misma casilla. El while con la comprobación lo arregló.
    '''

    print("\n" + "*" * 40)
    print("  ** TURNO DE LA MÁQUINA **")
    print("*" * 40)

    while True:
        fila = random.randint(0, DIMENSIONES - 1)   # fila aleatoria entre 0 y 9
        col  = random.randint(0, DIMENSIONES - 1)   # columna aleatoria entre 0 y 9

        # Si la casilla no tiene IMPACTO ni FALLO, es que nunca fue disparada
        if tablero_jugador.grid[fila][col] != IMPACTO and tablero_jugador.grid[fila][col] != FALLO:
            break   # casilla válida, salimos del while

    impacto = tablero_jugador.recibir_disparo(fila, col)   # procesamos el disparo

    if impacto == True:
        print("  ¡La máquina impactó en (" + str(fila) + "," + str(col) + ")!")
        print("  Tus vidas restantes: " + str(tablero_jugador.vidas))
        return True   # la máquina repite turno

    else:
        print("  La máquina falló en (" + str(fila) + "," + str(col) + "). ¡Tu turno!")
        return False  # le toca al jugador
