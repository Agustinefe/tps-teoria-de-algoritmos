import random as rnd
import time
import matplotlib.pyplot as plt
from algorithms.k_merge_dc import k_merge_dc
from algorithms.k_merge_heap import k_merge_heap


def generate_sample_array(K, h):
    """
    Crea una matriz de ejemplo con K arreglos de h elementos aleatorios
    """
    arr = []
    for _ in range(K): arr.append(sorted(rnd.sample(range(0, 100), h)))
    return arr

def get_mean_time(K, h, f, samples=100):
    """
    Ejecuta el algoritmo "samples" veces para calcular los tiempos de
    ejecucion y devolver un promedio
    """
    times = []
    arr = generate_sample_array(K, h)

    for _ in range(samples):
        start = time.time()
        f(arr)
        end = time.time()
        times.append(end - start)

    return sum(times) / samples

def plot_execution_time_mean(f, title):
    """
    Crea las listas de coordenadas (x, y) para plottear luego
    Si K = i, entonces lo que se incrementa es la cantidad de arreglos
    Si h = 1, entonces lo que se incrementa es el tamaño de los arreglos
    """
    x = []
    y = []

    for i in range(1, 101):
        x.append(i)
        y.append(get_mean_time(i, 10, f, samples=10000))

    print(y)

    plt.plot(x, y)
    plt.xlabel("Samples")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.title(title)
    plt.show()


plot_execution_time_mean(k_merge_dc, "Complejidad del algoritmo k-merge con D&C")
plot_execution_time_mean(k_merge_heap, "Complejidad del algoritmo k-merge con heap")