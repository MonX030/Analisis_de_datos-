def calcular_descuento(precio_original, porcentaje):
    descuento = precio_original * (porcentaje / 100)
    precio_final = precio_original - descuento
    return precio_final

total = calcular_descuento(800, 15)
print(f"El precio final con el descuento es: ${total}")
