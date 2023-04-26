def obtener_paquetes_disponibles_para_sobornar(cantidades_disponibles, cantidad_solicitada):
    """
    cantidades_disponibles es una lista ordenada, ej. [1, 2, 5, 7, 10]
    cantidad_solicitada es un entero positivo, ej. 6
    """
    paquetes_acum = []
    acum = 0
    for cantidad in cantidades_disponibles:
        if cantidad >= cantidad_solicitada:
            return cantidad
        acum += cantidad
        paquetes_acum.append(cantidad)
        if acum >= cantidad_solicitada:
            return paquetes_acum
    return "❌"

def obtener_soborno(paquetes_por_producto_ordenados, sobornos_solicitados):
    """
    paquetes_por_producto es un diccionario,
    ej. {'Cigarrillos': [1, 1, 2, 4, 8], 'Vodka': [1, 3, 5, 15]}
    sobornos_solicitados es un diccionario, ej. {'Vodka': 6, 'Cigarrillos': 6}
    """
    sobornos_disponibles = {}
    for producto in paquetes_por_producto_ordenados:
        soborno_disponible = obtener_paquetes_disponibles_para_sobornar(paquetes_por_producto_ordenados[producto], sobornos_solicitados[producto])
        sobornos_disponibles[producto] = soborno_disponible
    return sobornos_disponibles

def ordenar_paquetes_por_producto(paquetes_por_producto):
    """
    paquetes es una lista de tuplas, ej. [('Vodka', 3), ('Vodka', 9), ('Cigarrillos', 17)]
    """
    for producto in paquetes_por_producto:
        paquetes_por_producto[producto].sort() # in place
    return paquetes_por_producto
