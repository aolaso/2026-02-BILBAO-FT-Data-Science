'''
====================================================
ARCHIVO 2 DE 4: clases.py
====================================================

¿Para qué sirve este archivo?
Aquí definimos la clase TABLERO.

¿Qué es una clase?
Es como un molde para crear objetos.
La clase Tablero es el molde, y con ese molde
creamos dos objetos distintos en main.py:
  - tablero_jugador  (el tablero del humano)
  - tablero_maquina  (el tablero de la máquina)

Cada objeto tiene sus propios datos y sus
propias funciones para operar con ellos.

IMPORTANTE: Esta clase NO coloca los barcos.
La colocación la hace la función colocar_barcos()
que está en funciones.py. Así esta clase queda
más sencilla y fácil de entender. (Estuve leyendo con IA posibles formas de hacerlo con _ para hacerlo privado en Python, pero no me enteré de nada)
====================================================
'''

# Traemos las constantes que definimos en variables.py
from variables import AGUA, BARCO, IMPACTO, FALLO


# ==================================================
# DEFINICIÓN DE LA CLASE TABLERO
# ==================================================

class Tablero:
    '''
    Representa el tablero de juego de UN jugador.

    Cada tablero tiene dos cuadrículas de 10x10:

      self.grid  -> el tablero REAL.
                   Aquí se colocan los barcos y se
                   registran los impactos recibidos.

      self.vista -> el tablero de SEGUIMIENTO.
                   Aquí anotamos los disparos que
                   NOSOTROS hemos hecho al enemigo.
                   Sin barcos enemigos visibles.

    ¿Por qué dos cuadrículas?
    Al principio usé solo self.grid para todo.
    El error: al disparar al enemigo, sus barcos
    aparecían en mi tablero de seguimiento. Y claro eso era trampa.
    Separar en dos cuadrículas lo resolvió.
    '''


    # --------------------------------------------------
    # CONSTRUCTOR: __init__
    # --------------------------------------------------

    def __init__(self, jugador_id, dimensiones):
        '''
        Se ejecuta automáticamente cuando hacemos Tablero(...).
        Solo crea los tableros vacíos y cuenta las vidas.

        Parámetros:
          jugador_id  -> texto que identifica al dueño ("Tú" o "Máquina")
          dimensiones -> tamaño del tablero (10)
        '''

        self.jugador_id  = jugador_id    # nombre del dueño del tablero
        self.dimensiones = dimensiones   # tamaño (10)
        self.vidas       = 0             # se actualizará al colocar los barcos


        # ---- CREAR self.grid VACÍO ----
        # Una lista de 10 listas, cada una con 10 casillas de AGUA
        # Es una tabla de 10 filas × 10 columnas toda llena de " ~ "

        self.grid = []

        for fila in range(self.dimensiones):        # repetimos 10 veces (una por fila)
            fila_nueva = []
            for col in range(self.dimensiones):     # repetimos 10 veces (una por columna)
                fila_nueva.append(AGUA)             # cada casilla empieza siendo AGUA
            self.grid.append(fila_nueva)


        # ---- CREAR self.vista VACÍO ----
        # Mismo proceso: otra cuadrícula de 10x10 toda de AGUA
        # Esta la usamos para anotar nuestros propios disparos al enemigo

        self.vista = []

        for fila in range(self.dimensiones):
            fila_nueva = []
            for col in range(self.dimensiones):
                fila_nueva.append(AGUA)
            self.vista.append(fila_nueva)


    # --------------------------------------------------
    # MÉTODO: recibir_disparo
    # --------------------------------------------------

    def recibir_disparo(self, fila, col):
        '''
        Procesa un disparo recibido en la casilla (fila, col).

        Si había BARCO  -> marca IMPACTO, resta 1 vida, devuelve True
        Si había AGUA   -> marca FALLO,   devuelve False

        True  = acertó = el que disparó repite turno
        False = falló  = cambia el turno
        '''

        if self.grid[fila][col] == BARCO:
            self.grid[fila][col] = IMPACTO       # marcamos como tocado
            self.vidas = self.vidas - 1          # restamos una vida
            return True                          # acertó -> repite

        else:
            self.grid[fila][col] = FALLO         # marcamos como fallo
            return False                         # falló -> cambia turno


    # --------------------------------------------------
    # MÉTODO: marcar_vista
    # --------------------------------------------------

    def marcar_vista(self, fila, col, impacto):
        '''
        Anota el resultado de un disparo propio en self.vista.

        Cuando disparamos al enemigo, guardamos aquí el resultado
        para no repetir casillas y para poder verlo en pantalla.

        impacto = True  -> pintamos X (acertamos)
        impacto = False -> pintamos · (fallo)
        '''

        if impacto == True:
            self.vista[fila][col] = IMPACTO
        else:
            self.vista[fila][col] = FALLO


    # --------------------------------------------------
    # MÉTODO: imprimir_grid
    # --------------------------------------------------

    def imprimir_grid(self, grid, titulo):
        '''
        Imprime una cuadrícula por pantalla con números
        de fila y columna para orientarse.

        Recibe:
          grid   -> qué cuadrícula imprimir (self.grid o self.vista)
          titulo -> texto que aparece encima del tablero

        NOTA: Al principio imprimía sin números de fila ni columna.
        Era imposible saber a qué coordenadas correspondía cada casilla.
        Los añadí y el problema se resolvió.
        '''

        print("\n" + "=" * 40)
        print("  " + titulo)
        print("=" * 40)

        # Números de columna arriba del todo (0, 1, 2 ... 9)
        print("     ", end="")
        for col in range(self.dimensiones):
            print(" " + str(col) + " ", end="")
        print()

        print("     " + "---" * self.dimensiones)   # línea separadora

        # Cada fila con su número a la izquierda
        numero_fila = 0
        for fila in grid:
            print("  " + str(numero_fila) + " |", end="")
            for casilla in fila:
                print(casilla, end="")
            print()
            numero_fila = numero_fila + 1


    # --------------------------------------------------
    # MÉTODO: mostrar_tableros
    # --------------------------------------------------

    def mostrar_tableros(self):
        '''
        Muestra los dos tableros que necesita ver el jugador
        al inicio de cada turno:
          1. Su tablero real (para ver los impactos recibidos)
          2. Su seguimiento (para planificar el próximo disparo y ver cómo vas) 
        '''

        self.imprimir_grid(self.grid, "TU TABLERO (" + self.jugador_id + ")")
        self.imprimir_grid(self.vista, "TU SEGUIMIENTO (disparos al enemigo)")


    # --------------------------------------------------
    # MÉTODO: esta_hundido
    # --------------------------------------------------

    def esta_hundido(self):
        '''
        Devuelve True si este jugador no tiene vidas -> ha perdido.
        Devuelve False si aún le quedan barcos -> sigue jugando.
        '''

        return self.vidas <= 0
