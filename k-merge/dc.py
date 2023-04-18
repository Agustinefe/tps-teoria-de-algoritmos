import random as rnd
import time
import matplotlib.pyplot as plt

def merge(arr1, arr2):
    # Ambos ya estan ordenados
    i = 0
    j = 0
    arr = []

    while i < len(arr1) and j < len(arr2):

        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1

    rest, k = (arr2, j) if i == len(arr1) else (arr1, i)

    for idx in range(k, len(rest)):
        arr.append(rest[idx])

    return arr



def k_merge_rec(arrs, i, f):
    if i == f:
        return arrs[i]
    
    mid = (i + f) // 2

    arr1 = k_merge_rec(arrs, i, mid)
    arr2 = k_merge_rec(arrs, mid+1, f)

    return merge(arr1, arr2)


def k_merge(arrs):
    return k_merge_rec(arrs, 0, len(arrs)-1)

# Crea una matriz de ejemplo con K arreglos de h elementos aleatorios
def generate_sample_array(K, h):
    arr = []
    for _ in range(K): arr.append(sorted(rnd.sample(range(0, 100), h)))

    return arr

# Ejecuta el algoritmo "samples" veces para calcular los tiempos de ejecucion y devolver un promedio
def get_mean_time(K, h, samples=100):
    times = []
    arr = generate_sample_array(K, h)

    for _ in range(samples):
        start = time.time()
        k_merge(arr)
        end = time.time()
        times.append(end - start)

    return sum(times) / samples


x = []
y = []

# Crea las listas de coordenadas (x, y) para plotear luego
# Si K = i, entonces lo que se incrementa son la cantidad de arreglos
# Si h = 1, entonces lo que se incrementa es el tamaño de los arreglos
for i in range(1, 101):
    x.append(i)
    y.append(get_mean_time(i, 10, samples=10000))

print(y)

plt.plot(x, y)
plt.show()