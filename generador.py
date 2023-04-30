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

# Productos: 
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

#n: cantidad de diccionario
def generar_multiples_paquetes(productos, cantidad_maxima, n):
    listado_de_paquetes = []
    for i in range(cantidad_maxima):
        paquetes,sobornos_solicitados = generar_paquetes(productos, cantidad_maxima)
        listado_de_paquetes.append((paquetes,sobornos_solicitados))
    return listado_de_paquetes

def generate_elements_sample(E, W):
    sample = [1] * E     
    for i in range(E, W) : sample[random.randint(0, E-1)] += 1
    return sample

def generate_bribery(W):
    return random.randint(0, W)

def generate_packets_and_briberies(P, E, W, B=None, same_E=True, same_W=True):
    """
    P: amount of distinct products
    E: max amount of packets, for each product
    W: max amount of individual products (or what sum(E) should be), for each product
    B: amount of bribery, for each product (if None, then bribery is random)
    """
    products = [str(p) for p in range(P)]
    packets = {}
    briberies = {}

    for product in products:
        e = E if same_E else random.randint(1, E)
        w = W if same_W else random.randint(e, W)

        packets[product] = generate_elements_sample(e, w)
        bribery = B if B != None else generate_bribery(w)
        if bribery > 0:
            briberies[product] = bribery

    return packets, briberies

def main():
    print(generate_packets_and_briberies(3, 5, 5))

if __name__ == "__main__":
    main()