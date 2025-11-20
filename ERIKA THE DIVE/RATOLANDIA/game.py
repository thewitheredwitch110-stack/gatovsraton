
from laberinto import generar_laberinto, laberinto_logico
from entidades import mover_raton, mover_gato
from utils import mostrar

# ================================
# INICIO DEL JUEGO
# ================================

matrix = generar_laberinto()
lab = laberinto_logico(matrix)

print("🐭 Raton vs Gato 😼")
print("Laberinto generado automáticamente.\n")

# Elegir personaje
while True:
    pj = input("¿Querés jugar como Ratón (R) o Gato (G)? ").upper()
    if pj in ("R", "G"):
        break
    print("Opción inválida.")

control_raton = (pj == "R")
control_gato = (pj == "G")

print("\nTablero inicial:\n")
mostrar(matrix)

# ================================
# CICLO DE JUEGO (HASTA GANAR/PERDER)
# ================================

turno = 0

while True:
    print(f"🎲 TURNO {turno + 1}")

    # 1) Mueve el ratón
    escapo = mover_raton(matrix, lab, turno, control_raton)
    lab = laberinto_logico(matrix)
    mostrar(matrix)

    if escapo:
        print("🎉 ¡El ratón logró salir del laberinto!")
        break

    # 2) Mueve el gato
    atrapado = mover_gato(matrix, lab, turno, control_gato)
    lab = laberinto_logico(matrix)
    mostrar(matrix)

    if atrapado:
        print("💀 Fin del juego: el gato atrapó al ratón (o desapareció alguien).")
        break

    turno += 1
