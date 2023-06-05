import datetime
import os
import sys
import json
import time
from copy import deepcopy
from distutils.util import execute

from algorithms import backtracking_solution, approximation_solution, greedy_approximation_solution


def execute(sample, algorithm):
    """
    Ejecuta el algoritmo con la muestra dada y devuelve un diccionario
    con: tiempo de ejecución, cantidad de bins y cantidad de elementos
    """
    start = time.time()
    solution = algorithm(sample)
    end = time.time()
    
    return {"time": end - start, "bins": solution, "bins_number": len(solution)}


def simulate(samples, f, algorithm_name):
    """
    Ejecuta el algoritmo f con cada muestra de samples y devuelve un
    diccionario con los resultados
    """
    result = {}

    samples_number = samples["config"]["samples_number"]

    for i in range(samples_number):
        solution_i = execute(deepcopy(samples["samples"][str(i)]), f)
        result[str(i)] = solution_i
        print(f'\tIteración {str(i)} de algoritmo {algorithm_name} terminada en {result[str(i)]["time"]} segundos')

    return result


def main():
    # sys.setrecursionlimit(2000)
    if len(sys.argv) != 4:
        print("Error: se debe invocar con: ./simulator <datos.json> <samples_name> <E>|<A>|<A2>")
        return

    filepath = sys.argv[1]
    samples_name = sys.argv[2]
    algorithm = sys.argv[3]

    with open(filepath, 'r') as json_file:
        samples = json.load(json_file)
    
    config = samples["config"]

    results = {}
    results["config"] = config
    start = time.time()
    
    f = None
    algorithm_name = None

    match algorithm:
        case "E":
            f = backtracking_solution
            algorithm_name = "backtracking"
        case "A":
            f = approximation_solution
            algorithm_name = "approximation"
        case "A2":
            f = greedy_approximation_solution
            algorithm_name = "greedy"
        case _:
            print("Error: se debe invocar con: ./simulator <datos.json> <E>|<A>|<A2>")
            return

    results["results"] = simulate(samples, f, algorithm_name)
    end = time.time()

    print(f"Tiempo que perdiste de tu vida esperando a que termine esta simulación: {str(datetime.timedelta(seconds=end-start))}")

    json_dump_results = json.dumps(results, indent=4)

    filename = filepath.split("/")[-1]
    filepath = f'../results/{samples_name}/{algorithm_name}/{filename}'

    if not os.path.exists(filepath):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, 'w+') as file:
        file.write(json_dump_results)


if __name__ == "__main__":
    main()