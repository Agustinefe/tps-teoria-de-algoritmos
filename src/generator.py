import json
import random


DECIMALS = 3
INITIAL_SIZE = 100


def generate_sample(m):
    """
    Genera una muestra de m elementos aleatorios entre a y 1
    """
    a = 1 / (10 ** DECIMALS)
    T = [round(random.uniform(a, 1), DECIMALS) for _ in range(m)]
    return T


def generate_same_size_samples(samples_number, bin_size):
    """
    Genera samples_number muestras de bin_size elementos
    """
    bins = {}

    for i in range(samples_number):
        sample = generate_sample(bin_size)
        bins[i] = sample

    return bins

"""
def generate_multiple_sizes_samples(samples_number, bin_size, growth_factor=1):
    # growth_factor=1 -> todos elementos iguales

    samples = {}

    bin_sizes = [INITIAL_SIZE * growth_factor ** i for i in range(samples_number)]

    for size in bin_sizes:
        bins = []
        for _ in range(samples_number):
            sample = generate_sample(size)
            bins.append(sample)
        samples[str(size)] = bins
    
    return samples
"""

def main():
    with open("simconfig.json", "r") as config_file:
        config = json.load(config_file)

    sample = {}
    sample["config"] = config
    
    samples = generate_same_size_samples(config["samples_number"], config["bin_size"])

    sample["samples"] = samples
    json_dump_sample = json.dumps(sample, indent=4)

    filepath = f'../samples/greedy/samples_number={config["samples_number"]}-bin_size={config["bin_size"]}.json'
    with open(f'{filepath}', 'w+') as file:
        file.write(json_dump_sample)
    print(filepath)


if __name__ == "__main__":
    main()