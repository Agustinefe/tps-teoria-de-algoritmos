import json
from time import strftime
from algorithms.mochila import mochila_greedy
from algorithms.greedy import solucion
from generador import generate_elements_sample

def do_simulation(sequence, times):

    res = {
        "ours": {},
        "knapsack": {}
    }

    for i in sequence:
        arr = generate_elements_sample(i, i+i)
        res["ours"][str(i)] = []

        for j in range(times):
            res["ours"][str(i)].append(solucion())
            

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