def hanoi(n, origen, auxiliar, destino):
    # Caso base
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
        return

    # Paso 1: Mover n-1 discos de Origen a Auxiliar
    hanoi(n - 1, origen, destino, auxiliar)

    # Paso 2: Mover disco n de Origen a Destino
    print(f"Mover disco {n} de {origen} a {destino}")

    # Paso 3: Mover n-1 discos de Auxiliar a Destino
    hanoi(n - 1, auxiliar, origen, destino)


# Ejecución para 3 discos
hanoi(3, "A", "B", "C")
