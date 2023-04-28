from algorithms.mochila import mochila_dp, mochila_greedy
from generador import generar_paquetes
from copy import deepcopy

def pasar_aduana(paquetes: dict, soborno: dict, algoritmo):
    for producto, cantidad in soborno.items(): # O(S)
        paquetes[producto] = algoritmo(paquetes[producto], sum(paquetes[producto]) - cantidad) # Suma: O(P)
    
    return paquetes

def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))

def compare(res1: dict, res2: dict):

    if len(res1.keys()) != len(res2.keys()):
        return False
    
    for k1, v1 in res1.items():
        if (not k1 in res2.keys()) or (sum(res2[k1]) != sum(v1)):
            return False
        
    return True


def main():

    productos = list(map(str, [x for x in range(5)]))
    fallas = 0

    trys = 100000

    for i in range(trys):
        paquetes, soborno = generar_paquetes(productos, 100)
        paquetes1 = deepcopy(paquetes)
        paquetes2 = deepcopy(paquetes)
        soborno1 = deepcopy(soborno)
        soborno2 = deepcopy(soborno)

        greedy = pasar_aduana(paquetes1, soborno1, mochila_greedy)
        dp = pasar_aduana(paquetes2, soborno2, mochila_dp)

        if not compare(greedy, dp):
            fallas += 1

    print(f"Fallas: {str(fallas)} ({str(fallas / trys)})")

    #print("Greedy: " + format(pasar_aduana(paquetes1, soborno1, mochila_greedy)))
    #print("Programacion dinamica: " + format(pasar_aduana(paquetes2, soborno2, mochila_dp)))

main()