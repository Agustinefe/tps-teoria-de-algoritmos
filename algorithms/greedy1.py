def obtener_soborno(cantidades_disponibles, cantidad_solicitada):
    """
    cantidades_disponibles es una lista ordenada, ej. [1, 2, 5, 7, 10]
    cantidad_solicitada es un entero positivo, ej. 6
    """
    paquetes_acum = []
    acum = 0

    cantidades_disponibles.sort() # O(E log(E))

    for cantidad in cantidades_disponibles: # O(E)
        if cantidad >= cantidad_solicitada:
            return [cantidad]
        acum += cantidad
        paquetes_acum.append(cantidad)
        if acum >= cantidad_solicitada:
            return paquetes_acum

    return []

def greedy1(paquetes, pedido): # O(P * E * log(E))
    """
    paquetes = {'Cigarrillos': [1, 1, 2, 4, 8], 'Vodka': [1, 3, 5, 15]}
    pedido = {'Vodka': 6, 'Cigarrillos': 6}
    """
    sobornos_disponibles = {}
    for producto in paquetes: # O(P)
        soborno_disponible = obtener_soborno(paquetes[producto], pedido[producto]) # O(E * log(E))
        sobornos_disponibles[producto] = soborno_disponible
    return sobornos_disponibles