BIN_CAPACITY = 1


def backtracking_solution(T):
    return

def approximation_solution(T): # O(n)
    """
    Se va insertando los elementos de T en bins linealmente, si algún elemento no
    entra en el bin actual, se crea uno nuevo.
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
    Ordena los elementos de T de mayor a menor y luego los va insertando en bins
    linealmente, si algún elemento no entra en el bin actual, se crea uno nuevo.
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