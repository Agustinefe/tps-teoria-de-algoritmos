import random

def cantidad_obtenida_es_correcta(p, cantidad_esperada):
    return sum(valor[1] for valor in p) == cantidad_esperada

def generar_paquetes(productos, cantidad_maxima):
    num_productos_distintos = len(productos)

    paquetes = []

    restantes = cantidad_maxima
    while restantes > 0:
        producto = productos[random.randint(0, num_productos_distintos) - 1]
        # Divido por dos el num de productos distintos arbitrariamente para asegurar
        # que haya mayor cantidad de tuplas en el resultado
        a = restantes // 2 or 1
        cantidad = random.randint(1, a)
        restantes -= cantidad
        paquetes.append((producto, cantidad))

    return paquetes

def generar_listado_de_paquetes():
    cantidad_de_paquetes = 20
    productos = ['Vodka', 'Cigarrillos']
    cantidad_productos = 50
    listado_de_paquetes = []
    for i in range(cantidad_de_paquetes):
        p = generar_paquetes(productos, cantidad_productos)
        listado_de_paquetes.append(p)
        #print(p)
        #print(len(p))
        #print(cantidad_obtenida_es_correcta(p, cantidad_productos))
    return listado_de_paquetes

def main():
    listado_de_paquetes = generar_listado_de_paquetes()
    for p in listado_de_paquetes:
        print(p)
        print()


if __name__ == "__main__":
    main()