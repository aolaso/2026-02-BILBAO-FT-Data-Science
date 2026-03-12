# funciones_mini.py

def crear_tablero():
    # Creamos una lista vacía
    tablero = []
    # Hacemos un bucle para crear 10 filas
    for i in range(10):
        # Cada fila es una lista con 10 espacios en blanco
        fila = [" "] * 10
        tablero.append(fila)
    return tablero # Devolvemos el tablero terminado

def mostrar(tablero):
    # Imprimimos los números de arriba para que el usuario no se pierda
    print("  0 1 2 3 4 5 6 7 8 9")
    for i, fila in enumerate(tablero):
        # Imprimimos el número de fila y los elementos separados por un espacio
        print(i, " ".join(fila))

def disparar(tablero, f, c):
    # Comprobamos si en esa coordenada hay un barco ("B")
    if tablero[f][c] == "B":
        tablero[f][c] = "X" # Marcamos con X si es 'Tocado'
        return True
    else:
        tablero[f][c] = "o" # Marcamos con 'o' si es 'Agua'
        return False