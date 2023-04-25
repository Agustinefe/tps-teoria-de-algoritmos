

def obtener_paquetes_para_sobornar(cantidades_disponibles, cantidad_solicitada):
    """
    cantidades_disponibles es una lista ordenada, ej. [('Vodka', 3), ('Vodka', 4), ('Vodka', 9)]
    cantidad_solicitada es un entero positivo, ej. 6
    """
    paquetes_acum = []
    acum = 0
    for cantidad in cantidades_disponibles:
        if acum >= cantidad_solicitada:
            return paquetes_acum
        if cantidad[1] >= cantidad_solicitada:
            return cantidad
        acum += cantidad[1]
        paquetes_acum.append(cantidad)
    return "La próxima arreglamos amigo, sos un pichi"


def obtener_soborno(paquetes_por_producto, sobornos_solicitados):
    """
    paquetes_por_producto es un diccionario,
    ej. {'Vodka': [('Vodka', 3), ('Vodka', 9)], 'Cigarrillos': [('Cigarrillos', 3), ('Cigarrillos', 17)]}
    sobornos_solicitados es un diccionario, ej. {'Vodka':6, 'Cigarrillos':6}
    """
    for producto in paquetes_por_producto:
        # ¿ordenamos acá o antes, como un preprocesamiento?
        print(f"Paquetes disponibles de {producto}:")
        print(paquetes_por_producto[producto])
        print(f"Unidades solicitadas por soborno: {sobornos_solicitados[producto]}")
        print(f"Paquetes a entregar:")
        print(obtener_paquetes_para_sobornar(paquetes_por_producto[producto], sobornos_solicitados[producto]))

def obtener_paquetes_por_producto(paquetes):
    """
    paquetes es una lista de tuplas, ej. [('Vodka', 3), ('Vodka', 9), ('Cigarrillos', 17)]
    """
    paquetes_por_producto = {}
    for paquete in paquetes:
        paquetes_por_producto.setdefault(paquete[0], []).append(paquete)
    for producto in paquetes_por_producto:
        paquetes_por_producto[producto].sort(key=lambda tup: tup[1]) # in place
    return paquetes_por_producto

def main():
    # [('Producto_i', 'Unidades_i')]
    paquetes = [('Vodka', 3),
                ('Vodka', 9),
                ('Cigarrillos', 17),
                ('Cigarrillos', 1),
                ('Cigarrillos', 12),
                ('Vodka', 1),
                ('Cigarrillos', 7),
                ('Vodka', 8),
                ('Cigarrillos', 4)]
    sobornos_solicitados = {'Vodka': 4, 'Cigarrillos': 12}
    paquetes_por_producto = obtener_paquetes_por_producto(paquetes)

    obtener_soborno(paquetes_por_producto, sobornos_solicitados)

if __name__ == "__main__":
    main()
