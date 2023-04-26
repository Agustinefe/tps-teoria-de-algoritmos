from algorithms.greedy import solucion
from generador import cantidad_obtenida_es_correcta, generar_paquetes, generar_multiples_paquetes


def ejecucion_unitaria_greedy():
    productos = ['Vodka', 'Cigarrillos']
    cantidad_productos = 50
    paquetes,sobornos_solicitados = generar_paquetes(productos, cantidad_productos)
    print(f"Paquetes generados: {paquetes}")
    sobornos_disponibles = solucion(paquetes, sobornos_solicitados)
    print(f"Soborno disponible: {sobornos_disponibles}")


def ejecucion_multiple_greedy():
    productos = ['Vodka', 'Cigarrillos']
    cantidad_productos = 50
    n = 20
    paquetes_multiples = generar_multiples_paquetes(productos, cantidad_productos, n)
    for paquetes,sobornos_solicitados in paquetes_multiples:
        print(f"Paquetes generados: {paquetes}")
        print(f"Soborno solicitado: {sobornos_solicitados}")
        cantidad_maxima_es_correcta = cantidad_obtenida_es_correcta(paquetes, cantidad_productos)
        generacion_correcta = "✅" if cantidad_maxima_es_correcta else "❌"
        print(f"Generación de paquetes correcta: {generacion_correcta}")
        sobornos_disponibles = solucion(paquetes, sobornos_solicitados)
        print(f"Soborno disponible: {sobornos_disponibles}\n")


def main():
    ejecucion_multiple_greedy()


if __name__ == "__main__":
    main()
