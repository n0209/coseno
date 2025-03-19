import math
grados = float(input("Ingrese el ángulo en grados: "))
radianes = math.radians(grados)
coseno = math.cos(radianes)
print(f"El coseno de {grados}° es {coseno:.4f}")