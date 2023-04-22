import matplotlib.pyplot as plt
import numpy as np
import sys, json, os

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

def plot_execution_time(results, title, filepath):
    """
    Realiza un grafico del resultado de alguna simulacion
    """
    x = []
    y = []

    for k, v in results['results'].items():
        x.append(int(k))
        y.append(np.median(v))


    plt.plot(x, y)
    plt.xlabel(f"Muestras ({results['times']})")
    plt.ylabel("Tiempo de ejecución (mediana) (s)")
    plt.title(title)

    save_plot(get_filename(filepath), "plot")
    plt.show()

def plot_diff_time(results, title, filepath):
    """
    Realiza un grafico de las diferencias entre resultados de la simulacion
    """
    y = []

    for v in results['results'].values():
        y.append(np.median(v))

    y = diff(y)
    plt.plot(y)
    plt.xlabel("Ejecuciones")
    plt.ylabel("Diffs entre ejecuciones (s)")
    plt.title(title)

    save_plot(get_filename(filepath), "diff")
    plt.show()

def get_filename(path):
    return path.split('\\')[-1].replace(".json", "")

def save_plot(dirname, plotname):
    if not os.path.exists(f'plots/{dirname}'):
        os.makedirs(f'plots/{dirname}')
    
    plt.savefig(f'./plots/{dirname}/{plotname}')

def stringify_algorithm(algorithm):
    if algorithm == 'k_merge_dc':
        return "D&C"
    elif algorithm == 'k_merge_heap':
        return "Heaps"
    else:
        return "??"
    

def main():

    # Lectura del json (indicado por terminal) con resultados de alguna simulacion
    filepath = sys.argv[1]
    with open(filepath, 'r') as json_file:
        results = json.load(json_file)

    # Ploteo
    plot_execution_time(results, f"Complejidad del algoritmo k-merge con {stringify_algorithm(results['algorithm'])}, variando {results['var']}", filepath)
    plot_diff_time(results, f"Complejidad del algoritmo k-merge con {stringify_algorithm(results['algorithm'])} (diffs), variando {results['var']}", filepath)
    #plot_execution_time(results, "Complejidad del algoritmo k-merge con heap")

main()

# Esta es una muestra vieja que obtuve al correr el algoritmo con el range(1, 10000000, 1000000)
# Correlo de nuevo para replicarlo.
# Al calcular su diff, si este presenta un leve crecimiento, entonces la complejidad no puede ser O(n)
"""
#y = [5.117814302444458, 11.093862295150757, 17.533334732055664, 24.108925580978394, 31.016116857528687, 37.93633460998535, 45.00921845436096, 51.83584809303284, 59.26834273338318, 66.73365044593811]
y = [0.0, 5.117377161979675, 11.228312492370605, 17.63421893119812, 23.955934643745422, 31.06106674671173, 37.911049127578735, 44.651437878608704, 51.895089626312256, 59.28847134113312, 66.75569880008698]
x = diff(y)
print(x)
plt.plot(x)
plt.show()
"""