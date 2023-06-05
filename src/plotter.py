import os
import json
import platform
import statistics
import matplotlib.pyplot as plt


def calculate_relation(filename_approximation, filename_backtracking):
    axis = []

    with open(filename_approximation, "r") as json_file:
        json_data_approximation = json.load(json_file)
    with open(filename_backtracking, "r") as json_file:
        json_data_backtracking = json.load(json_file)

        bin_size = json_data_approximation['config']['bin_size']
        for r in json_data_approximation['results']:
            relation = json_data_approximation['results'][r]['bins_number'] / json_data_backtracking['results'][r]['bins_number']
            axis.append((r, relation))

    axis.sort(key=lambda x: x[0])

    x = [i[0] for i in axis]
    y = [i[1] for i in axis]

    return x,y


def calculate_time_mean(json_data):
    results = json_data['results']
    times = [solution['time'] for solution in results.values()]
    return sum(times) / len(times)
    #return statistics.median(times)


def calculate_means_for_all_files(folder_path):
    axis = []

    for filename in os.listdir(folder_path):
        with open(os.path.join(folder_path, filename)) as json_file:
            json_data = json.load(json_file)
            bin_size = json_data['config']['bin_size']
            time_mean = calculate_time_mean(json_data)
            axis.append((bin_size, time_mean))

    axis.sort(key=lambda x: x[0])

    x = [i[0] for i in axis]
    y = [i[1] for i in axis]

    return x,y


def get_filename(path):
    split_char = '\\' if platform.system() == 'Windows' else '/'
    return path.split(split_char)[-1].replace(".json", "")


def save_plot(dirname, plotname):
    if not os.path.exists(f'../plots/{dirname}'):
        os.makedirs(f'../plots/{dirname}')
    
    plt.savefig(f'../plots/{dirname}/{plotname}', bbox_inches = 'tight')


def plot_algorithms(x, y, title, file_path):
    plt.plot(x, y)
    plt.xticks(x)
    plt.xlabel('n')
    plt.ylabel('Tiempo promedio (s)')
    plt.title('Tiempo de ejecución promedio en función de n\npara backtracking (100 muestras)')
    save_plot(get_filename(file_path), title)
    plt.show()


def plot_algorithms_time_comparison(x1, y1, y2, label_1, label_2, title, file_path):
    plt.plot(x1, y1, label = label_1)
    plt.plot(x1, y2, label = label_2)
    plt.xticks(x1)
    plt.xlabel('n')
    plt.ylabel('Tiempo promedio (s)')
    plt.title('Tiempos de ejecución promedio en función de n\npara aproximaciones (100 muestras)')
    plt.legend()
    save_plot(get_filename(file_path), title)
    plt.show()


def plot_relation(x, y, title, file_path, bin_size):
    plt.plot(x, y)
    plt.xticks([i for i in range(0, 100, 10)])
    plt.xlabel('# de muestra')
    plt.ylabel('A(I)/z(I)')
    plt.title(f'A(I)/z(I) por muestra [bin_size={bin_size}] [100 muestras]')
    save_plot(get_filename(file_path), title)
    plt.show()


def extract_json_solutions(result_num, a_folder_path, b_folder_path, c_folder_path):
    a_solutions = []
    b_solutions = []
    c_solutions = []

    for filename in os.listdir(a_folder_path):
        with open(os.path.join(a_folder_path, filename)) as json_file:
            json_data = json.load(json_file)
            results = json_data['results']
            a_solutions.append(results[result_num]['bins_number'])
    
    for filename in os.listdir(b_folder_path):
        with open(os.path.join(b_folder_path, filename)) as json_file:
            json_data = json.load(json_file)
            results = json_data['results']
            b_solutions.append(results[result_num]['bins_number'])

    for filename in os.listdir(c_folder_path):
        with open(os.path.join(c_folder_path, filename)) as json_file:
            json_data = json.load(json_file)
            results = json_data['results']
            c_solutions.append(results[result_num]['bins_number'])

    return a_solutions, b_solutions, c_solutions


def plot_algorithms_solution_comparison(result_num, folder_path_1, folder_path_2, folder_path_3, algorithm1_name, algorithm2_name, algorithm3_name, save_path, title):
    results_algo1, results_algo2, results_algo3 = extract_json_solutions(result_num, folder_path_1, folder_path_2, folder_path_3)
    input_sizes = [4, 6, 8, 10, 12, 13, 14, 15, 16]

    plt.scatter(input_sizes, results_algo1, label=algorithm1_name, color='purple')
    plt.plot(input_sizes, results_algo1, color = 'purple')
    plt.scatter(input_sizes, results_algo2, label=algorithm2_name, color='orange')
    plt.plot(input_sizes, results_algo2, color = 'orange')
    plt.scatter(input_sizes, results_algo3, label=algorithm3_name, color = 'green')
    plt.plot(input_sizes, results_algo3, color = 'green')

    plt.xticks(input_sizes)
    plt.xlabel('Tamaño de conjunto de entrada')
    plt.ylabel('Cantidad de bins de la solución')
    plt.title(f'Comparación de optimalidad de algoritmos')
    plt.legend()

    save_plot(get_filename(save_path), title)

    plt.show()


def main():

    # n vs mean time - backtracking
    """
    folder_path = "../results/4-16/backtracking"
    x, y = calculate_means_for_all_files(folder_path)
    plots_path = "../plots/4-16/"
    plot_algorithms(x, y, "n-vs-mean-time-backtracking-11.png", plots_path)

    
    # n vs mean time - approximations comparison
    
    folder_path_approximation = "../results/4-16/approximation"
    folder_path_greedy = "../results/4-16/greedy"

    x1, y1 = calculate_means_for_all_files(folder_path_approximation)
    _, y2 = calculate_means_for_all_files(folder_path_greedy)
    plots_path = "../plots/4-16/"
    plot_algorithms_time_comparison(x1, y1, y2, "Approximation", "Greedy Approximation", "n-vs-mean-time-approximations.png", plots_path)
    
    greedy_result_path = "../results/4-16/greedy"
    approximation_result_path = "../results/4-16/approximation"
    backtracking_result_path = "../results/4-16/backtracking"
    plots_path = "../plots/4-16/"
    result_num = '0'
    plot_algorithms_solution_comparison(result_num, greedy_result_path, approximation_result_path, backtracking_result_path, "Greedy", "Approximation", "Backtracking", plots_path, f"solutions-comparison-{result_num}.png")
    """

    bin_size='16'
    x, y = calculate_relation(f"../results/4-16/approximation/samples_number=100-bin_size={bin_size}.json",
                             f"../results/4-16/backtracking/samples_number=100-bin_size={bin_size}.json")

    plots_path = "../plots/"
    plot_relation(x, y, f"relation-{bin_size}.png", plots_path, bin_size)
    

if __name__ == '__main__':
    main()
    
