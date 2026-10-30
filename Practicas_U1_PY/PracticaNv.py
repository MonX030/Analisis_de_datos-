
import numpy as np

precio_unidad = 50


# OPCIÓN 1: Utilizando NumPy 

matriz_A_np = np.array([[10, 15], 
                        [20, 5]]) # Ventas del Sábado

matriz_B_np = np.array([[5, 12], 
                        [15, 8]]) # Ventas del Domingo

# 2. Calcular el total de productos vendidos (Suma matricial A + B)
total_ventas_np = matriz_A_np + matriz_B_np

# 3. Calcular el ingreso total (Multiplicación por escalar)
ingreso_total_np = total_ventas_np * precio_unidad

# 4. Imprimir resultados en pantalla
print("=== RESULTADOS CON NUMPY ===")
print("Total de productos vendidos (Sábado + Domingo):")
print(total_ventas_np)
print("\nIngreso total en pesos (a 50 pesos por producto):")
print(ingreso_total_np)


# OPCIÓN 2: Utilizando Python Nativo (Listas de Listas)

# 1. Crear las matrices A y B como listas de listas
matriz_A_nat = [[10, 15], 
                [20, 5]]

matriz_B_nat = [[5, 12], 
                [15, 8]]

# 2. Sumar las matrices manualmente mediante iteración
total_ventas_nat = [
    [matriz_A_nat[i][j] + matriz_B_nat[i][j] for j in range(2)] 
    for i in range(2)
]

# 3. Multiplicar por el escalar (50)
ingreso_total_nat = [
    [total_ventas_nat[i][j] * precio_unidad for j in range(2)] 
    for i in range(2)
]