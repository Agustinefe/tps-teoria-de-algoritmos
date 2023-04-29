import matplotlib.pyplot as plt
import numpy as np
import sys, json, os
import platform as pl

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

    # Ploteo
    plot_execution_time(results, filepath)
   
main()