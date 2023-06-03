BIN_CAPACITY = 1


def number_to_base(n, b, s):
    if n == 0:
        return [0] * s
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    if len(digits) < s:
        digits.extend([0] * (s - len(digits)))
    return digits[::-1]

def bin_packing(T, k, c=1):
    # T = [0.1, 0.7, 0.3, 0.1, 0.9, 0.4, 0.5]
    # n = 7, puedo iterar hasta 6
    # o sea: 2^7 - 1 = 127
    M = [[] for i in range(k)]
    s = len(T)
    for i in range(0, (k ** s) - 1):
        b = number_to_base(i, k, s)
        for bin_number,t in zip(b, T):
            M[bin_number].append(t)
        
        if all([sum(bin) <= c for bin in M]):
            return M
        else:
            M = [[] for i in range(k)]
    return None

def brute_force_solution(T):
    for i in range(1, len(T) + 1):
        M = bin_packing(T, i)
        if M:
            return M


def backtracking(T, index, n, solucion_parcial, soluciones):
    """
    Realiza una búsqueda por backtracking para encontrar la
    mínima cantidad de subconjuntos disjuntos de T cuyos
    elementos sumen n o menos.
    """
    if not T:
        return True

    # Si encuentro una solución, la agrego a las soluciones
    if sum(solucion_parcial) == n:
        soluciones.append(solucion_parcial)
        for x in solucion_parcial:
            T.remove(x)
        return True

    # Si llegué al final de T con una solucion_parcial válida, la agrego a las soluciones
    if sum(solucion_parcial) <= n and index == len(T):
        soluciones.append(solucion_parcial)
        for x in solucion_parcial:
            T.remove(x)
        return True
    
    # Si por esta rama me paso, dejo de probar
    if sum(solucion_parcial) > n:
        return False
    
    # Si no me paso, exploro esa rama
    for i in range(index, len(T)):
        solucion_parcial.append(T[i])
        if backtracking(T, i+1, n, solucion_parcial, soluciones):
            return backtracking(T, 0, n, [], soluciones)
        else:
            solucion_parcial.pop()
    return False


def backtracking_solution(T):
    """
    Obtiene la solución exacta al problema del empaquetamiento
    de minimización realizando un llamado a un función que lo
    resuelve por backtraking.
    """
    soluciones = []
    backtracking(T, 0, BIN_CAPACITY, [], soluciones)
    return soluciones


def approximation_solution(T): # O(n)
    """
    Se va insertando los elementos de T en bins linealmente, si algún
    elemento no entra en el bin actual, se crea uno nuevo.
    """
    bins = []
    current_bin = []
    current_sum = 0

    for item in T: # O(n)
        if current_sum + item > BIN_CAPACITY:
            bins.append(current_bin)
            current_bin = [item]
            current_sum = item
        else:
            current_bin.append(item)
            current_sum += item

    bins.append(current_bin)

    return bins


def greedy_approximation_solution(T): # O(n * log(n))
    """
    Ordena los elementos de T de mayor a menor y luego los va
    insertando en bins linealmente, si algún elemento no entra
    en el bin actual, se crea uno nuevo.
    """
    T.sort(reverse=True) # O(n * log(n))

    bins = []
    current_bin = []
    current_sum = 0

    for item in T: # O(n)
        if current_sum + item > BIN_CAPACITY:
            bins.append(current_bin)
            current_bin = [item]
            current_sum = item
        else:
            current_bin.append(item)
            current_sum += item

    bins.append(current_bin)

    return bins

def main():
    # result = bin_packing([0.1, 0.7, 0.3, 0.1, 0.9, 0.4, 0.5], 3)
    return

if __name__ == '__main__':
    main()
    