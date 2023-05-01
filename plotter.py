import matplotlib.pyplot as plt
import numpy as np
import sys, json, os
import platform as pl

def plot_greedys_best_result(ours, knapsack):
    
    best_result_ours = 0
    best_result_knapsack = 0

    for k, v in ours.items():
        if v[1]["0"] > sum(knapsack[k][1]["0"]):
            best_result_ours += 1
        else:
            best_result_knapsack += 1

    stats = {"Greedy1": best_result_ours, "Greedy2": best_result_knapsack}
    plt.bar(stats.keys(), stats.values(), color ='maroon', width = 0.4)

    plt.xlabel("Algoritmos")
    plt.ylabel("Veces en que dio un mejor resultado que el otro")
    plt.title("Comparacion de resultados de Greedys")
    plt.show()

def get_greedy_accuracy(greedy, dp, filepath):
    is_optimal = 0
    total = len(greedy.keys())

    for k, v in greedy.items():
        if sum(dp[k][1]["0"]) == sum(greedy[k][1]["0"]):
            is_optimal += 1
    stats = {"Greedy": is_optimal, "PD": total}
    plt.bar(stats.keys(), stats.values(), color ='maroon', width = 0.4)

    plt.xlabel("Algoritmos")
    plt.ylabel("Cantidad de soluciones óptimas")
    plt.title("Optimalidad de Greedy")
    save_plot(get_filename(filepath), "barplot")
    plt.show()


def plot_execution_time(results, filepath):
    """
    Realiza un grafico del resultado de alguna simulacion
    """

    for algo in results['results'].keys():
        x = []
        y = []
        for k, v in results['results'][algo].items():
            x.append(int(k))
            y.append(v[0])
        
        plt.plot(x, y, label=algo)

    plt.xlabel(f'Variable {results["config"]["var"]}')
    plt.ylabel("Tiempo de ejecución (s)")
    plt.title(f'Rendimiento de los algoritmos, variando {results["config"]["var"]}')
    plt.legend()
    save_plot(get_filename(filepath), "plot")
    plt.show()

def get_filename(path):
    split_char = '\\' if pl.system() == 'Windows' else '/'
    return path.split(split_char)[-1].replace(".json", "")

def save_plot(dirname, plotname):
    if not os.path.exists(f'plots/{dirname}'):
        os.makedirs(f'plots/{dirname}')
    
    plt.savefig(f'./plots/{dirname}/{plotname}')

def main():

    # Lectura del json (indicado por terminal) con resultados de alguna simulacion
    filepath = sys.argv[1]
    with open(filepath, 'r') as json_file:
        results = json.load(json_file)

    if results["config"]["var"] == "random":
        get_greedy_accuracy(results["results"]["greedy_knapsack"], results["results"]["dp_knapsack"], filepath)
        return

    # Plotteo
    plot_execution_time(results, filepath)

main()