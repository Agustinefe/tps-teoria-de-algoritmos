import random as rnd
import time
import json
from algorithms.k_merge_dc import k_merge_dc
from algorithms.k_merge_heap import k_merge_heap


results = {}

def generate_sample_array(K, h):
    """
    Crea una matriz de ejemplo con K arreglos de h elementos aleatorios
    """
    arr = []
    for _ in range(K): arr.append(sorted(rnd.sample(range(0, 10001), h)))
    return arr

def execute_multiple_times(K, h, f, samples):
    """
    Ejecuta el algoritmo "samples" veces para calcular los tiempos de
    ejecucion y devolverlos
    """

    times = []
    arr = generate_sample_array(K, h)

    for i in range(samples):
        start = time.time()
        f(arr)
        end = time.time()
        print("\tFinished iteration " + str(i+1) + " in time " + str(end - start))
        times.append(end - start)

    return times


def simulate_K_variation(sequence, times, algorithm):
    """
    Ejecuta el algoritmo (times veces) realizando una variacion en la cantidad de 
    arrays determinados por sequence.
    """
    y = {}

    for i in sequence:
        # Hardcodeado para evaluar i arrays de 1 elemento
        t = execute_multiple_times(i, 1, algorithm, samples=times)
        print("Finished " + str(i))
        y[str(i)] = t
    
    return y

def simulate_h_variation(sequence, times, algorithm):
    """
    Ejecuta el algoritmo (times veces) realizando una variacion en en el tamaño del array
    determinados por sequence.
    """
    y = {}

    for i in sequence:
        # Hardcodeado para evaluar 1 array de i elementos
        t = execute_multiple_times(1, i, algorithm, samples=times)
        print("Finished " + str(i))
        y[str(i)] = t
    
    return y

def do_simulation(sequence, times, algorithm, var):
    """
    Hace un dispatch basado en la variable a simular
    """
    if var == 'K':
        return simulate_K_variation(sequence, times, algorithm)
    else:
        return simulate_h_variation(sequence, times, algorithm)

def main():

    # Definicion de parametros de simulacion
    start = 1
    stop = 2*10**7+1
    step = 2*10**6
    times = 10
    algorithm = k_merge_dc
    var = "K"

    # Guardado de los parametros en el json
    results["start"] = start
    results["stop"] = stop
    results["step"] = step
    results["times"] = times
    results["algorithm"] = "k_merge_dc"
    results["var"] = var   
    results["results"] = do_simulation(range(start, stop, step), times, algorithm, var)

    # Stringificacion del json
    json_dump_results = json.dumps(results)

    # Escritura del json
    filename = time.strftime("%Y-%m-%d_%H-%M-%S")
    with open(f'results/{filename}.json', 'w+') as file:
        file.write(json_dump_results)
        

    
main()


