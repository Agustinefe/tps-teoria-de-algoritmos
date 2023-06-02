import math
import time

BIN_CAPACITY = 1
EPSILON = 0.00000002
it = 1

def count(L):
    return sum(list(map(lambda l: len(l), L)))

def is_valid(M):
    if not M: return False
    return all(sum(m) <= 1+EPSILON for m in M)

def backtracking_aux(M, T, K, t):
    if count(M) == len(T): # O(T)
        return M

    for k in range(K): # O(K)
        M[k].append(T[t]) # O(1)
        if is_valid(M): # O(T)
            res = backtracking_aux(M, T, K, t+1) # T(T-1)
            if is_valid(res): # O(T)
                return res
        M[k].pop() # O(1)
    
    return None


def backtracking_solution(T):
    """
    Obtiene la solución exacta al problema del empaquetamiento
    de minimización realizando un llamado a un función que lo
    resuelve por backtraking.
    """

    base = math.ceil(sum(T)-EPSILON)
    global it
    for K in range(base, len(T)+1):
        it = 1
        M = [[] for _ in range(K)]
        if (res := backtracking_aux(M, T, K, 0)):
            return res
    return None

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
    