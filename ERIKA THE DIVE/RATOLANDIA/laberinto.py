import random
from config import *

# ================================
# GENERAR LABERINTO ALEATORIO
# ================================

def generar_laberinto():
    # Laberinto vacío
    lab = [[VACIO for _ in range(ANCHO)] for _ in range(ALTO)]

    # Bordes
    for x in range(ALTO):
        for y in range(ANCHO):
            if x == 0 or x == ALTO-1 or y == 0 or y == ANCHO-1:
                lab[x][y] = PARED

    # Paredes internas aleatorias
    for _ in range((ANCHO * ALTO) // 6):
        rx = random.randint(1, ALTO-2)
        ry = random.randint(1, ANCHO-2)
        lab[rx][ry] = PARED

    # Entrada y salida
    entrada = (1, 1)
    salida = (ALTO-2, ANCHO-2)
    lab[entrada[0]][entrada[1]] = RATON
    lab[salida[0]][salida[1]] = SALIDA

    # Gato
    lab[ALTO-3][ANCHO-3] = GATO

    # Quesos
    for _ in range(CANTIDAD_QUESOS):
        while True:
            qx = random.randint(1, ALTO-2)
            qy = random.randint(1, ANCHO-2)
            if lab[qx][qy] == VACIO:
                lab[qx][qy] = QUESO
                break

    return lab


# Versión lógica (# y .)
def laberinto_logico(matrix):
    logico = []
    for fila in matrix:
        nueva = []
        for c in fila:
            if c == PARED:
                nueva.append(PARED)
            else:
                nueva.append(VACIO)
        logico.append(nueva)
    return logico
