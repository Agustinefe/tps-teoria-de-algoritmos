def obtener_soborno(cantidades_disponibles, cantidad_solicitada):
    """
    cantidades_disponibles es una lista ordenada, ej. [1, 2, 5, 7, 10]
    cantidad_solicitada es un entero positivo, ej. 6
    """
    paquetes_acum = []
    acum = 0

    cantidades_disponibles.sort() # O(n log(n))

    for cantidad in cantidades_disponibles: # O(n)
        if cantidad >= cantidad_solicitada:
            return [cantidad]
        acum += cantidad
        paquetes_acum.append(cantidad)
        if acum >= cantidad_solicitada:
            return paquetes_acum

    return []

def greedy1(paquetes, pedido): # O(n * m * log(m))
    """
    paquetes = {'Cigarrillos': [1, 1, 2, 4, 8], 'Vodka': [1, 3, 5, 15]}
    pedido = {'Vodka': 6, 'Cigarrillos': 6}
    """
    sobornos_disponibles = {}
    for producto in paquetes: # O(m)
        soborno_disponible = obtener_soborno(paquetes[producto], pedido[producto]) # O(n * log(n))
        sobornos_disponibles[producto] = soborno_disponible
    return sobornos_disponibles