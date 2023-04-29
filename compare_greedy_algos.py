import json
from time import strftime
from algorithms.mochila import mochila_greedy
from algorithms.greedy import solucion
from contrabando import pasar_aduana
from generador import generate_packets_and_briberies
import random as rnd
import time

def do_simulation(sequence, times):

    res = {
        "ours": {},
        "knapsack": {}
    }

    for e in sequence:
        packets, briberies = generate_packets_and_briberies(100, e, rnd.randint(e, e+100))

        start_ours = time.time()
        sol_ours = solucion(packets, briberies)
        end_ours = time.time()
        print(f"Finished ours in time: {end_ours-start_ours}")

        start_knapsack = time.time()
        sol_knapsack = pasar_aduana(packets, briberies, mochila_greedy)
        end_knapsack = time.time()
        print(f"Finished ours in time: {end_knapsack-start_knapsack}")

        res["ours"][str(e)] = {"time": end_ours - start_ours, "solution": sol_ours}
        res["knapsack"][str(e)] = {"time": end_knapsack - start_knapsack, "solution": sol_knapsack}
        print(f"Finished iteration {e}")

    return res


            

def main():
    # Configuracion de la simulacion
    with open("simconfig_greedy.json", "r") as config_file:
        config = json.load(config_file)

    # Guardado de los parametros en el json
    results = {}
    results["start"] = config["start"]
    results["stop"] = config["stop"]
    results["step"] = config["step"]
    results["times"] = config["times"] 
    results["results"] = do_simulation(
        range(config["start"], config["stop"], config["step"]), 
        config["times"], 
        )

    # Stringificacion del json
    json_dump_results = json.dumps(results, indent=4)

    # Escritura del json
    filename = strftime("%Y-%m-%d_%H-%M-%S")
    with open(f'results/compare_knapsack_algos/{filename}.json', 'w+') as file:
        file.write(json_dump_results)


if __name__ == "__main__":
    main()