import copy
from config import *
from utils import es_valido

def distancia(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def evaluar(rat, gat):
    if rat == gat:
        return -1000
    return distancia(rat, gat)  # cuanto más lejos del gato, mejor

def profundidad_por_turno(turno):
    return 2 if turno < 3 else 4

def minimax(rat, gat, profundidad, max_prof, turno_raton, lab):
    if rat == gat:
        return -1000
    if profundidad >= max_prof:
        return evaluar(rat, gat)

    if turno_raton:
        mejor = -float("inf")
        for dx, dy in MOVS:
            nx, ny = rat[0] + dx, rat[1] + dy
            if not es_valido(nx, ny, lab):
                continue
            nuevo = copy.deepcopy(lab)
            val = minimax((nx, ny), gat, profundidad+1, max_prof, False, nuevo)
            mejor = max(mejor, val)
        return mejor

    else:
        peor = float("inf")
        for dx, dy in MOVS:
            gx, gy = gat[0] + dx, gat[1] + dy
            if not es_valido(gx, gy, lab):
                continue
            nuevo = copy.deepcopy(lab)
            val = minimax(rat, (gx, gy), profundidad+1, max_prof, True, nuevo)
            peor = min(peor, val)
        return peor
