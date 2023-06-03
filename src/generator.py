import json
import os
import random
import sys

DECIMALS = 3

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

def main():
    if len(sys.argv) != 4:
        print("Error: se debe invocar con: ./generator <samples_name> <samples_number> <bin_size>")
        return

    samples_name = sys.argv[1]
    samples_number = int(sys.argv[2])
    bin_size = int(sys.argv[3])

    sample = {}
    sample["config"] = {
                        "samples_number": samples_number,
                        "bin_size": bin_size
                    }
    
    samples = generate_same_size_samples(samples_number, bin_size)
    sample["samples"] = samples

    json_dump_sample = json.dumps(sample, indent=4)

    filepath = f'../samples/{samples_name}/samples_number={samples_number}-bin_size={bin_size}.json'

    if not os.path.exists(filepath):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(f'{filepath}', 'w+') as file:
        file.write(json_dump_sample)

    print(filepath)

if __name__ == "__main__":
    main()