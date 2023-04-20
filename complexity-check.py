import random as rnd
import time
import matplotlib.pyplot as plt
from algorithms.k_merge_dc import k_merge_dc
from algorithms.k_merge_heap import k_merge_heap
import numpy as np

def generate_sample_array(K, h):
    """
    Crea una matriz de ejemplo con K arreglos de h elementos aleatorios
    """
    arr = []
    for _ in range(K): arr.append(sorted(rnd.sample(range(0, 10001), h)))
    return arr

def get_mean_time(K, h, f, samples=100):
    """
    Ejecuta el algoritmo "samples" veces para calcular los tiempos de
    ejecucion y devolver un promedio
    """
    times = []
    arr = generate_sample_array(K, h)

    for i in range(samples):
        start = time.time()
        f(arr)
        end = time.time()
        print("\tFinished iteration " + str(i+1) + " in time " + str(end - start))
        times.append(end - start)
        

    return sum(times) / samples

def diff(l):
    """
    Devuelve una lista con las diferencias entre cada uno de los elementos consecutivos.
    Si una muestra l respondiese a O(n), diff_l tendria los mismos numeros (aprox), 
        dado que su pendiente es constante.
    Si en cambio respondiese a O(n*log2(n)), diff_l mostraria un crecimiento en sus numeros,
        correspondiente a la derivada de n*log2(n) => log2(n) + 1/ln(2)
    """
    diff_l = []
    for i in range(1, len(l)):
        diff_l.append(l[i] - l[i-1])
    return diff_l

def plot_execution_time_mean(f, title):
    """
    Crea las listas de coordenadas (x, y) para plottear luego
    Si K = i, entonces lo que se incrementa es la cantidad de arreglos
    Si h = 1, entonces lo que se incrementa es el tamaño de los arreglos
    """
    x = []
    y = []

    for i in range(1, 10000000, 1000000):
        x.append(i)
        # Hardcodeado para evaluar i arrays de 1 elemento
        t = get_mean_time(i, 1, f, samples=1)
        print("Finished " + str(i) + " in time " + str(t))
        y.append(t)
    
    
    print(y)
    plt.plot(x, y)
    plt.xlabel("Samples")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.title(title)
    
    plt.show()

# Esta es una muestra vieja que obtuve al correr el algoritmo con el range(1, 10000000, 1000000)
# Correlo de nuevo para replicarlo.
# Al calcular su diff, si este presenta un leve crecimiento, entonces la complejidad no puede ser O(n)
#   y = [0.0, 2.4843173027038574, 5.258683919906616, 8.155308961868286, 11.233759641647339, 14.402469396591187, 17.67595934867859, 20.92929434776306, 24.05248522758484, 27.752885341644287]
#   x = diff(y)

#   plt.plot(x)
#   plt.show()

#plot_execution_time_mean(k_merge_dc, "Complejidad del algoritmo k-merge con D&C")
#plot_execution_time_mean(k_merge_heap, "Complejidad del algoritmo k-merge con heap")