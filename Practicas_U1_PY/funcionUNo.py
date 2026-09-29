import datetime

def saludar():
    print("Hola, bienvenidos")

saludar()

def mostrar_hora():
    hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"La hora actual es: {hora_actual}")

mostrar_hora()

# Now() Consulta en el reloj hora del SO
# Strftime para convertir la fecha en texto, usando el formato establecido
# f-string la letra f indica a python que procese el texto
# e inserte las variables dentro de las llaves
# {hora_actual} se toma el valor almacenado en la variable de hora_actual
# y lo reemplaza ahí mismo
