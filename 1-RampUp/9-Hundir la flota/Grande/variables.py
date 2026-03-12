'''
====================================================
ARCHIVO 1 DE 4: variables.py
====================================================

¿Para qué sirve este archivo?
Aquí guardamos todas las CONSTANTES del juego.

Una constante es un valor que NUNCA cambia mientras
el programa corre. Por ejemplo: el tablero siempre
mide 10x10. Eso no cambia nunca.

¿Por qué meterlas en un archivo separado?
Porque si mañana quiero que el tablero sea de 8x8,
solo cambio el número aquí, en un solo sitio.
El resto del programa lo coge automáticamente.
Sin este archivo, tendría que buscar el número 10
en todos mis otros archivos y cambiarlo en cada uno.
Eso es un lío y además me dejaría alguno sin cambiar.

Este archivo lo importan los otros tres archivos.
====================================================
'''


# --------------------------------------------------
# SECCIÓN 1: TAMAÑO DEL TABLERO
# --------------------------------------------------

DIMENSIONES = 10   # el tablero tiene 10 filas y 10 columnas (como el juego real)


# --------------------------------------------------
# SECCIÓN 2: LOS SÍMBOLOS QUE SE VEN EN EL TABLERO
# --------------------------------------------------
'''
Cuando imprimimos el tablero por pantalla, cada casilla
muestra un símbolo distinto dependiendo de su estado.

He usado espacios alrededor de cada símbolo (" ~ " en vez de "~") - (vivan las virgulillas)
para que las casillas no queden pegadas y se lea mejor.

Al principio usé letras (A para agua, B para barco...) pero
los símbolos son más intuitivos de un vistazo y me estaba volviendo loco si no. 
'''

AGUA    = " ~ "   # casilla de mar donde aún no ha caído ningún disparo
BARCO   = " O "   # casilla donde hay un barco tuyo (tú lo ves, el enemigo no)
IMPACTO = " X "   # disparo que acertó en un barco -> tocado
FALLO   = " · "   # disparo que cayó al agua -> fallo


# --------------------------------------------------
# SECCIÓN 3: LOS BARCOS DEL JUEGO
# --------------------------------------------------
'''
Este diccionario define qué barcos hay en la partida.

  clave (key)   -> nombre del barco   (un texto)
  valor (value) -> eslora/longitud del barco   (cuántas casillas ocupa)

En total hay 10 barcos que ocupan 20 casillas en total:
  4 lanchas      × 1 casilla  =  4 casillas
  3 destructores × 2 casillas =  6 casillas
  2 cruceros     × 3 casillas =  6 casillas
  1 portaaviones × 4 casillas =  4 casillas
                               = 20 casillas en total -> por lo que tenemos 20 vidas

NOTA: Al principio guardé los barcos en una lista simple:
  BARCOS = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
Funcionaba para colocarlos, pero cuando quería imprimir
mensajes como "has hundido el Portaaviones" era imposible
saber qué barco era cuál. Cambié a diccionario para tener
nombres y poder escribir mensajes claros. - Gracias Claude 🤖❤️
'''

BARCOS = {
    "Lancha 1":     1,    # el barco más pequeño, ocupa 1 sola casilla
    "Lancha 2":     1,    # igual que el anterior
    "Lancha 3":     1,    # igual que el anterior
    "Lancha 4":     1,    # igual que el anterior
    "Destructor 1": 2,    # ocupa 2 casillas
    "Destructor 2": 2,    # ocupa 2 casillas
    "Destructor 3": 2,    # ocupa 2 casillas
    "Crucero 1":    3,    # ocupa 3 casillas
    "Crucero 2":    3,    # ocupa 3 casillas
    "Portaaviones": 4,    # el barco más grande, ocupa 4 casillas
}


# --------------------------------------------------
# SECCIÓN 4: LAS ORIENTACIONES PARA COLOCAR BARCOS
# --------------------------------------------------
'''
Cuando colocamos un barco en el tablero, necesitamos
saber en qué dirección "crece" ese barco desde su
casilla de inicio. (O es lo que yo creo, pero no estoy del todo seguro ahora, después de hablar con compañerxs)

Solo usamos dos direcciones (como una cruz):
  "H" = Horizontal -> el barco crece hacia la derecha
  "V" = Vertical   -> el barco crece hacia abajo

Ejemplo con un barco de eslora 3 que empieza en fila=2, col=3:
  Horizontal -> ocupa (2,3), (2,4), (2,5)   <- columna sube, fila sigue igual
  Vertical   -> ocupa (2,3), (3,3), (4,3)   <- fila sube, columna sigue igual

NOTA: Al principio tenía 4 orientaciones: N, S, E, O
(Norte, Sur, Este, Oeste), porque si no no entendía como hacerlo y me estaba volviendo loco. Pero era demasiado complicado
para lo que necesitaba. Con H y V es suficiente para
colocar los barcos en cualquier posición del tablero
y el código es mucho más fácil de entender.
'''

ORIENTACIONES = ["H", "V"]   # H = horizontal,  V = vertical
