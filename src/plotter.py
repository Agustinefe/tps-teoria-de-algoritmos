import os
import json
import platform
import matplotlib.pyplot as plt



def calculate_time_mean(json_data):
    results = json_data['results']
    times = [solution['time'] for solution in results.values()]
    return sum(times) / len(times)


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


def plot_algorithms_comparison(x1, y1, y2, label_1, label_2, title, file_path):
    plt.plot(x1, y1, label = label_1)
    plt.plot(x1, y2, label = label_2)
    plt.xticks(x1)
    plt.xlabel('n')
    plt.ylabel('Tiempo promedio (s)')
    plt.title('Tiempos de ejecución promedio en función de n\npara aproximaciones (100 muestras)')
    plt.legend()
    save_plot(get_filename(file_path), title)
    plt.show()


def main():
    # n vs mean time - backtracking
    folder_path = "../results/backtracking"
    x, y = calculate_means_for_all_files(folder_path)
    plots_path = "../plots/"
    plot_algorithms(x, y, "n-vs-mean-time-backtracking.png", plots_path)

    # n vs mean time - approximations comparison
    
    folder_path_approximation = "../results/approximation"
    folder_path_greedy = "../results/greedy"
    x1, y1 = calculate_means_for_all_files(folder_path_approximation)
    _, y2 = calculate_means_for_all_files(folder_path_greedy)
    plots_path = "../plots/"
    plot_algorithms_comparison(x1, y1, y2, "Approximation", "Greedy Approximation", "n-vs-mean-time-approximations.png", plots_path)


if __name__ == '__main__':
    main()
    
