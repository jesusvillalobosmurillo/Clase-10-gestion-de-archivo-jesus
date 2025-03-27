# En este modulo se crea la lista de compras
import random

def generar_lista_compras():
    canasta_basica = {
        'Arroz' : 1800,
        'Azúcar' : 2200,
        'Harina' : 1200,
        'Tomate' : 2500,
        'Frijoles' : 1400,
        'Papas' : 3800,
        'Leche' : 1000,
        'Cerveza' : 1000,
        'Cáfe' : 5000,
        'Fideos' : 800,
        'Jabón' : 1500,
        'Huevos' : 3500,
        'Naranjas' : 2500,
        'Sal' : 800,
    }
    #Aqui voy a seleccionar aleatoreamente 5 prductos de la canasta basica
    seleccion = random.sample(list(canasta_basica.items()), k=5)
    return seleccion
