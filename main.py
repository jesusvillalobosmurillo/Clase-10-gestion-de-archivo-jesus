# Proyecto: Trabajo fundementos de Python
# Estudiante: [Jesus Villalobos Murillo]
# Fecha de Inicio: [26/03/25]
# Fecha de Entrega: [26/03/25]
# Descripción: Vamos a crear una lista de compras

# from analisis_datos.carga_datos import generar_lista_compras
# from analisis_datos.estadisticas import media
from analisis_datos import *

lista_compras = generar_lista_compras()

print (lista_compras)

precios = [precio for _, precio in lista_compras]

print (precios)

print(f'La media de compras:', media(precios))

print (f'La mediana de las compras es:', mediana(precios))