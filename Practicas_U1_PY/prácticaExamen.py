def suma_recursiva_matriz(matriz, fila=0, col=0):
    # Caso base: se han recorrido todas las filas de la matriz
    if fila >= len(matriz):
        return 0

    # Si se terminó de recorrer la fila actual, salta a la siguiente fila en col=0
    if col >= len(matriz[fila]):
        return suma_recursiva_matriz(matriz, fila + 1, 0)

    # Paso recursivo: suma el elemento actual y avanza a la siguiente columna
    return matriz[fila][col] + suma_recursiva_matriz(matriz, fila, col + 1)


# Matriz cuadrada de 2x2 implementada como lista de listas
matriz = [
    [1, 2],
    [3, 4],
]

total = suma_recursiva_matriz(matriz)
print(f"La suma total de la matriz es {total}")
