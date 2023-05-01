import heapq as hq

class HeapElem:
    def __init__(self, arr_num, idx, value):
        self.arr_num = arr_num
        self.idx = idx
        self.value = value

    # Sobreescritura del método de comparación
    def __lt__(self, nxt):
        return self.value < nxt.value

def k_merge_heap(arrs):
    """
    Recibe un arreglo arrs compuesto de k arreglos ordenados de
    largo h y devuelve un único arreglo ordenado cuyos elementos
    son cada uno de los elementos que poseían los k arreglos por
    los que se componía arrs originalmente.
    Ejemplo: arrs = [[1, 5, 6], [1, 3, 10], [2, 3, 8], [4, 7, 30]]
    """
    k = len(arrs) # k es cantidad de arreglos
    h = len(arrs[0]) # h largo de arreglos (mismo para todos)

    # Si arrs tiene un solo arreglo o sus arreglos están vacíos, lo devuelvo
    if k <= 0 or h <= 0:
        return arrs

    ordered_arr = []

    # Inicialización del heap con el primer elemento de cada arreglo
    mins = []
    for i in range(k):
        hq.heappush(mins, HeapElem(i, 0, arrs[i][0]))

    # Merge de los elementos de arrs usando el heap
    while mins:
        min_elem = hq.heappop(mins)
        ordered_arr.append(min_elem.value)
        if min_elem.idx + 1 < h:
            # Si el arreglo tiene más elementos, agregar el siguiente elemento al heap
            hq.heappush(mins, HeapElem(min_elem.arr_num, min_elem.idx + 1, arrs[min_elem.arr_num][min_elem.idx + 1]))

    return ordered_arr
