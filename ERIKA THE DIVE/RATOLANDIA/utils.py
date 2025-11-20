from config import *

def encontrar(matrix, simbolo):
    for i in range(ALTO):
        for j in range(ANCHO):
            if matrix[i][j] == simbolo:
                return (i, j)
    return None


def mostrar(matrix):
    for fila in matrix:
        print(" ".join(fila))
    print()


def es_valido(x, y, lab):
    return (
        0 <= x < ALTO and
        0 <= y < ANCHO and
        lab[x][y] != PARED
    )
