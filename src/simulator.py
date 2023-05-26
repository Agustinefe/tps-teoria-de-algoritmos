import datetime
import sys
import json
import time
from copy import deepcopy
from distutils.util import execute

from algorithms import backtracking_solution


def execute(sample, algorithm):
    """
    Ejecuta el algoritmo con la muestra dada y devuelve un diccionario
    con: tiempo de ejecución, cantidad de bins y cantidad de elementos
    """
    start = time.time()
    solution = algorithm(sample)
    end = time.time()
    
    return {"time": end - start, "bins": solution, "bins_number": len(solution)}


def simulate(samples, f):
    """
    Ejecuta el algoritmo f con cada muestra de samples y devuelve un
    diccionario con los resultados
    """
    result = {}

    samples_number = samples["config"]["samples_number"]

    for i in range(samples_number):
        solution_i = execute(deepcopy(samples["samples"][str(i)]), f)
        result[str(i)] = solution_i
        print(f'\tFinished iteration {str(i)} for backtracking in time {result[str(i)]["time"]}')

    return result


def main():
    # sys.setrecursionlimit(2000)
    if len(sys.argv) != 2:
        print("Error: se debe invocar con: ./simulator <sample.json>")
        return

    filepath = sys.argv[1]
    print(filepath)
    with open(filepath, 'r') as json_file:
        samples = json.load(json_file)
    
    config = samples["config"]

    results = {}
    results["config"] = config
    start = time.time()
    results["results"] = simulate(samples, backtracking_solution)
    end = time.time()

    print(f"Tiempo que perdiste de tu vida esperando a que termine esta simulación: {str(datetime.timedelta(seconds=end-start))}")

    json_dump_results = json.dumps(results, indent=4)

    filename = filepath.split("/")[-1]
    with open(f'../results/{filename}', 'w+') as file:
        file.write(json_dump_results)


if __name__ == "__main__":
    main()