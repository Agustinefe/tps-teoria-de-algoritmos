# El valor de cada elemento es igual a su peso
# Complejidad: O(E log(E))
def mochila_greedy(elementos: list, W: int):
    mochila = [] # O(1)
    capacidad = W # O(1)

    # En orden decreciente
    elementos.sort(reverse=True) # O(E log(E))
    
    for elemento in elementos: # O(n)
        if capacidad >= elemento: # O(1)
            mochila.append(elemento) # O(1)
            capacidad -= elemento # O(1)
        elif capacidad == 0:
            return mochila

    return mochila

# El valor de cada elemento es igual a su peso
# Complejidad (a priori): O(E * W)
# Dado que es un algoritmo pseudopolinomial, porque W es un numero entero,
# Y la complejidad depende del tamaño de las variables, entonces, si
# m = log2(W) => O(E * 2^m). La complejidad es exponencial en la longitud de la entrada,
# pero el tiempo de ejecucion es polinomial respecto al valor.
def mochila_dp(elementos: list, W: int):
    """
    Creacion de la matriz de memorizacion
    """
    E = len(elementos) # O(1)
    OPT = [[0 for _ in range(W+1)] for _ in range(E+1)] # O(W * E)
    
    for e in range(1, E+1): # O(E)
        for w in range(1, W+1): # O(W)

            if w < elementos[e-1]: # O(1)
                OPT[e][w] = OPT[e-1][w] # O(1)
            else:
                OPT[e][w] = max(
                    OPT[e-1][w], # O(1)
                    elementos[e-1] + OPT[e-1][w - elementos[e-1]] # O(1)
                    ) # O(1)

    
    """
    Generacion del resultado en base a M
    """
    mochila = [] # O(1)
    e = E # O(1)
    w = W # O(1)

    while w > 0 and e > 0: # O(E)
        if OPT[e][w] > OPT[e-1][w]: # O(1)
            mochila.append(elementos[e-1]) # O(1)
            w -= elementos[e-1] # O(1)
        e -= 1 # O(1)

    return mochila