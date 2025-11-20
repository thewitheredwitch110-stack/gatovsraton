from config import *
from utils import *
from minimax import minimax, profundidad_por_turno
import copy

salto_activo = False  # ratón tiene salto 1 turno después de comer queso

# ================================
# MOVIMIENTO DEL RATÓN
# ================================
def mover_raton(matrix, lab, turno, control_jugador):
    global salto_activo

    rx, ry = encontrar(matrix, RATON)
    gx, gy = encontrar(matrix, GATO)

    max_prof = profundidad_por_turno(turno)

    # Limpiar casilla actual del ratón
    matrix[rx][ry] = VACIO

    # ---------------------------------------
    # CONTROL DEL JUGADOR (SI ÉL ES RATÓN)
    # ---------------------------------------
    if control_jugador:
        while True:
            mov = input("Tu movimiento (W/A/S/D): ").lower()

            if mov == "w":
                dx, dy = -1, 0
            elif mov == "s":
                dx, dy = 1, 0
            elif mov == "a":
                dx, dy = 0, -1
            elif mov == "d":
                dx, dy = 0, 1
            else:
                print("Entrada inválida.")
                continue

            nx, ny = rx + dx, ry + dy

            if es_valido(nx, ny, lab):
                break
            else:
                print("Movimiento bloqueado por pared.")
    else:
        # ---------------------------------------
        # IA controla al ratón
        # ---------------------------------------
        movimientos = MOVS.copy()

        # Si hay salto → agregar movimientos extra
        if salto_activo:
            movimientos += MOVS_SALTO

        mejor_val = -float("inf")
        nx, ny = rx, ry

        for dx, dy in movimientos:
            nx2, ny2 = rx + dx, ry + dy
            if not es_valido(nx2, ny2, lab):
                continue

            val = minimax((nx2, ny2), (gx, gy), 0, max_prof, False, lab)
            if val > mejor_val:
                mejor_val = val
                nx, ny = nx2, ny2

    # Qué había en la casilla de destino ANTES de poner al ratón
    destino = matrix[nx][ny]

    # Si hay queso → habilita salto para el siguiente turno
    if destino == QUESO:
        salto_activo = True
    else:
        salto_activo = False

    # Si llegó a la salida → gana y termina el juego
    if destino == SALIDA:
        matrix[nx][ny] = RATON
        return True  # ratón escapó

    matrix[nx][ny] = RATON
    return False  # todavía no escapó


# ================================
# MOVIMIENTO DEL GATO
# ================================
def mover_gato(matrix, lab, turno, control_jugador):
    rx, ry = encontrar(matrix, RATON)
    gx, gy = encontrar(matrix, GATO)

    matrix[gx][gy] = VACIO

    max_prof = profundidad_por_turno(turno)

    # CONTROL JUGADOR GATO
    if control_jugador:
        while True:
            mov = input("Tu movimiento (W/A/S/D): ").lower()

            if mov == "w":
                dx, dy = -1, 0
            elif mov == "s":
                dx, dy = 1, 0
            elif mov == "a":
                dx, dy = 0, -1
            elif mov == "d":
                dx, dy = 0, 1
            else:
                print("Entrada inválida.")
                continue

            nx, ny = gx + dx, gy + dy

            if es_valido(nx, ny, lab):
                break
            else:
                print("Movimiento bloqueado por pared.")
    else:
        # IA controla al gato
        mejor_val = float("inf")
        nx, ny = gx, gy

        for dx, dy in MOVS:
            gx2, gy2 = gx + dx, gy + dy
            if not es_valido(gx2, gy2, lab):
                continue

            val = minimax((rx, ry), (gx2, gy2), 0, max_prof, True, lab)
            if val < mejor_val:
                mejor_val = val
                nx, ny = gx2, gy2

    destino = matrix[nx][ny]

    if destino == RATON:
        print("😼 ¡El gato atrapó al ratón!")
        matrix[nx][ny] = GATO
        return True  # gato ganó

    matrix[nx][ny] = GATO
    return False  # aún no lo atrapó
