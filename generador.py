import random


def cantidad_obtenida_es_correcta(paquetes, cantidad_esperada):
    return sum(sum(cantidades) for cantidades in paquetes.values()) == cantidad_esperada

def obtener_solicitud_de_soborno(cantidad_por_producto):
    sobornos_por_producto = {}
    for producto in cantidad_por_producto:
        sobornos_por_producto[producto] = random.randint(1, cantidad_por_producto[producto])
    return sobornos_por_producto

def obtener_cantidad_por_producto(paquetes):
    cantidad_por_producto = {}
    for (producto, cantidades) in paquetes.items():
        cantidad_por_producto[producto] = sum(cantidades)
    return cantidad_por_producto

def generar_paquetes(productos, cantidad_maxima):
    num_productos_distintos = len(productos)
    paquetes = {}
    restantes = cantidad_maxima
    while restantes > 0:
        producto = productos[random.randint(0, num_productos_distintos) - 1]
        # Divido por 3 el num de productos distintos arbitrariamente para
        # asegurar que haya mayor cantidad de tuplas en el resultado
        a = (restantes // 3) or 1
        cantidad = random.randint(1, a)
        restantes -= cantidad
        paquetes.setdefault(producto, []).append(cantidad)

    cantidad_por_producto = obtener_cantidad_por_producto(paquetes)
    sobornos_solicitados = obtener_solicitud_de_soborno(cantidad_por_producto)

    return paquetes,sobornos_solicitados

def generar_multiples_paquetes(productos, cantidad_maxima, n):
    listado_de_paquetes = []
    for i in range(cantidad_maxima):
        paquetes,sobornos_solicitados = generar_paquetes(productos, cantidad_maxima)
        listado_de_paquetes.append((paquetes,sobornos_solicitados))
    return listado_de_paquetes

def main():
    productos = ['Vodka', 'Cigarrillos']
    cantidad_productos = 50
    n = 100

    # Generador unitario
    # paquetes, sobornos_solicitados = generar_paquetes(productos, cantidad_productos)

    # Generador múltiple
    print(generar_multiples_paquetes(productos, cantidad_productos, n))

if __name__ == "__main__":
    main()