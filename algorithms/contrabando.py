from mochila import mochila_dp, mochila_greedy

def pasar_aduana(paquetes: dict, soborno: dict, algoritmo):
    for producto, cantidad in soborno.items(): # O(S)
        paquetes[producto] = algoritmo(paquetes[producto], sum(paquetes[producto]) - cantidad) # Suma: O(P)
    
    return paquetes

def main():

    paquetes1 = {
        "cigarrillos": [6, 1, 3, 100, 4, 2, 8, 7, 9],
        "vodka": [5]
    }

    soborno1 = {
        "cigarrillos": 8
    }

    paquetes2 = {
        "cigarrillos": [6, 1, 3, 100, 4, 2, 8, 7, 9],
        "vodka": [5]
    }

    soborno2 = {
        "cigarrillos": 8
    }


    print("Greedy: " + format(pasar_aduana(paquetes1, soborno1, mochila_greedy)))
    print("Programacion dinamica: " + format(pasar_aduana(paquetes2, soborno2, mochila_dp)))

main()