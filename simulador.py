import datetime
import json, time
from algorithms.mochila import *
from contrabando import pasar_aduana
from generador import generate_packets_and_briberies2
from copy import deepcopy
import sys


P_global = 1


def dp_knapsack(packets, briberies):
    return pasar_aduana(packets, briberies, mochila_dp)

def greedy_knapsack(packets, briberies):
    return pasar_aduana(packets, briberies, mochila_greedy)

def execute(packets, briberies, algorithm):
    start = time.time()
    solution = algorithm(packets, briberies)
    end = time.time()
    
    return (end - start, solution)


def simulate_E_variation(config):

    res = {}
    if config["do_greedy_knapsack"]: res["greedy_knapsack"] = {}
    if config["do_dp_knapsack"]: res["dp_knapsack"] = {}

    for e in range(config['start'], config['stop'], config['step']):
        w = 10*e
        packets, briberies = generate_packets_and_briberies2(P_global, e, w, B=w-100)

        if "greedy_knapsack" in res.keys():
            res["greedy_knapsack"][str(e)] = execute(deepcopy(packets), briberies, greedy_knapsack)
            print(f'\tFinished iteration {e} for greedy_knapsack in time {res["greedy_knapsack"][str(e)][0]}')

        if "dp_knapsack" in res.keys():
            res["dp_knapsack"][str(e)] = execute(deepcopy(packets), briberies, dp_knapsack)
            print(f'\tFinished iteration {e} for dp_knapsack in time {res["dp_knapsack"][str(e)][0]}')

        print(f'Finished iteration {e}')

    return res

def simulate_W_variation(config):
    
    res = {}
    if config["do_greedy_knapsack"]: res["greedy_knapsack"] = {}
    if config["do_dp_knapsack"]: res["dp_knapsack"] = {}

    for w in range(config['start'], config['stop'], config['step']):

        packets, briberies = generate_packets_and_briberies2(P_global, 10, 2*w, B=1)

        if "greedy_knapsack" in res.keys():
            res["greedy_knapsack"][str(w)] = execute(deepcopy(packets), briberies, greedy_knapsack)
            print(f'\tFinished iteration {w} for greedy_knapsack in time {res["greedy_knapsack"][str(w)][0]}')

        if "dp_knapsack" in res.keys():
            res["dp_knapsack"][str(w)] = execute(deepcopy(packets), briberies, dp_knapsack)
            print(f'\tFinished iteration {w} for dp_knapsack in time {res["dp_knapsack"][str(w)][0]}')

        print(f'Finished iteration {w}')

    return res

def do_simulation(config):
    simulation = eval(f'simulate_{config["var"]}_variation')
    return simulation(config)

def simulate_from_config():
    # Configuracion de la simulacion
    with open("simconfig.json", "r") as config_file:
        config = json.load(config_file)

    # Guardado de los parametros en el json
    results = {}
    results["config"] = config
    start = time.time()
    results["results"] = do_simulation(config)
    end = time.time()

    print(f"Tiempo que perdiste de tu vida esperando a que termine esta simulación: {str(datetime.timedelta(seconds=end-start))}")

    # Stringificacion del json
    json_dump_results = json.dumps(results, indent=4)

    # Escritura del json
    filename = time.strftime("%Y-%m-%d_%H-%M-%S")
    with open(f'results/{filename}.json', 'w+') as file:
        file.write(json_dump_results)

def simulate_sample(samples):
    res = {}
    if samples["config"]["do_greedy_knapsack"]: res["greedy_knapsack"] = {}
    if samples["config"]["do_dp_knapsack"]: res["dp_knapsack"] = {}

    sequence = range(samples["config"]["start"], samples["config"]["stop"], samples["config"]["step"])

    for sample, w in zip(samples["sample"], sequence):
        if "greedy_knapsack" in res.keys():
            res["greedy_knapsack"][str(w)] = execute(deepcopy(sample["packets"]), sample["briberies"], greedy_knapsack)
            print(f'\tFinished iteration {w} for greedy_knapsack in time {res["greedy_knapsack"][str(w)][0]}')

        if "dp_knapsack" in res.keys():
            res["dp_knapsack"][str(w)] = execute(deepcopy(sample["packets"]), sample["briberies"], dp_knapsack)
            print(f'\tFinished iteration {w} for dp_knapsack in time {res["dp_knapsack"][str(w)][0]}')

    return res

def simulate_from_sample():
    filepath = sys.argv[1]
    with open(filepath, 'r') as json_file:
        samples = json.load(json_file)
    
    # Guardado de los parametros en el json
    results = {}
    results["config"] = samples["config"]
    start = time.time()
    results["results"] = simulate_sample(samples)
    end = time.time()

    print(f"Tiempo que perdiste de tu vida esperando a que termine esta simulación: {str(datetime.timedelta(seconds=end-start))}")

    # Stringificacion del json
    json_dump_results = json.dumps(results, indent=4)

    # Escritura del json
    filename = time.strftime("%Y-%m-%d_%H-%M-%S")
    with open(f'results/{filename}.json', 'w+') as file:
        file.write(json_dump_results)




def main():

    if len(sys.argv) == 1:
        simulate_from_config()
    else:
        simulate_from_sample()


if __name__ == "__main__":
    main()