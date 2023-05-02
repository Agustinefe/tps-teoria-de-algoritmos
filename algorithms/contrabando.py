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
