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

    return mochila

# El valor de cada elemento es igual a su peso
# Complejidad (a priori): O(E * W)
# Dado que es un algoritmo pseudopolinomial, porque W es un numero entero,
# Y la complejidad depende del tamaño de las variables, entonces, si
# m = log2(W) => O(E * 2^m). La complejidad es exponencial en la longitud de la entrada,
# pero el tiempo de ejecucion es polinomial respecto al valor.
def mochila_dp(elementos: list, W: int):
    M = [[0 for _ in range(W+1)] for _ in range(len(elementos)+1)] # O(W * E)

    for k in range(len(elementos)): # O(E)
        i = k+1 # O(1)
        for w in range(1, W+1): # O(W)

            if w < elementos[k]: # O(1)
                M[i][w] = M[i-1][w] # O(1)
            else:
                M[i][w] = max(
                    M[i-1][w], # O(1)
                    elementos[k] + M[i-1][w - elementos[k]] # O(1)
                    ) # O(1)
    
    mochila = [] # O(1)
    piv_x = len(M[0]) - 1 # O(1)
    piv_y = len(M) - 1 # O(1)

    while piv_y > 0 and piv_x > 0: # O(E + W)
        if M[piv_y][piv_x] > M[piv_y-1][piv_x]: # O(1)
            mochila.append(elementos[piv_y-1]) # O(1)
            piv_x -= elementos[piv_y-1] # O(1)
        piv_y -= 1 # O(1)

    return mochila
        
