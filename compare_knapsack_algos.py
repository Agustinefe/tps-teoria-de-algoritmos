import json
from algorithms.greedy import solucion
from generador import generate_elements_sample
from time import time, strftime
from algorithms.mochila import *

def simulate_algorithm(arr, W, algorithm):
    start = time()
    res = algorithm(arr, W)
    end = time()
    return res, end - start

def simulate_knapsack(n, W, iterations, check_greedy):
    times_greedy = []
    times_dp = []

    for i in range(iterations):
        arr = generate_elements_sample(n, W)

        greedy, greedy_time = simulate_algorithm(arr.copy(), W, mochila_greedy)
        print("\tFinished iteration (greedy) " + str(i+1) + " in time " + str(greedy_time))

        dp, dp_time = simulate_algorithm(arr.copy(), W, mochila_dp)
        print("\tFinished iteration (dynamic programming) " + str(i+1) + " in time " + str(dp_time))

        if check_greedy:
            times_greedy.append([greedy_time, sum(greedy) == sum(dp)])
        else:
            times_greedy.append(greedy_time)
        times_dp.append(dp_time)

    return times_greedy, times_dp


def simulate_n_variation(sequence, times, check_greedy):
    result = {
        "greedy": {},
        "dp": {}
    }

    for i in sequence:
        times_greedy, times_dp = simulate_knapsack(i, 10, times, check_greedy)
        print("Finished " + str(i))
        result["greedy"][str(i)] = times_greedy
        result["dp"][str(i)] = times_dp

    return result

def simulate_W_variation(sequence, times, check_greedy):
    result = {
        "greedy": {},
        "dp": {}
    }

    for i in sequence:
        times_greedy, times_dp = simulate_knapsack(10, i, times, check_greedy)
        print("Finished " + str(i))
        result["greedy"][str(i)] = times_greedy
        result["dp"][str(i)] = times_dp

    return result

def do_simulation(sequence, times, var, check_greedy=False):
    variation = eval(f"simulate_{var}_variation")
    return variation(sequence, times, check_greedy)

def main():
    # Configuracion de la simulacion
    with open("simconfig_knapsack.json", "r") as config_file:
        config = json.load(config_file)

    # Guardado de los parametros en el json
    results = {}
    results["start"] = config["start"]
    results["stop"] = config["stop"]
    results["step"] = config["step"]
    results["times"] = config["times"]
    results["var"] = config["var"]   
    results["check_greedy"] = config["check_greedy"] 
    results["results"] = do_simulation(
        range(config["start"], config["stop"], config["step"]), 
        config["times"], 
        config["var"],
        config["check_greedy"]
        )

    # Stringificacion del json
    json_dump_results = json.dumps(results, indent=4)

    # Escritura del json
    filename = strftime("%Y-%m-%d_%H-%M-%S")
    with open(f'results/compare_knapsack_algos/{filename}.json', 'w+') as file:
        file.write(json_dump_results)


if __name__ == "__main__":
    main()