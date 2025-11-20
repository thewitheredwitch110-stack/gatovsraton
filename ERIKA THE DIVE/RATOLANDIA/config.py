# ================================
# CONFIGURACIÓN GENERAL
# ================================
import random

ANCHO = 23
ALTO = 14

# Quesos por partida
CANTIDAD_QUESOS = random.randint(2, 4)

# Símbolos
PARED = "#"
VACIO = "."
RATON = "R"
GATO = "G"
QUESO = "Q"
ENTRADA = "E"
SALIDA = "S"

# Movimiento normal
MOVS = [(-1,0),(1,0),(0,-1),(0,1)]  # arriba, abajo, izq, der

# Movimiento de salto (ratón solo si comió queso)
MOVS_SALTO = [(-2,0),(2,0),(0,-2),(0,2)]
