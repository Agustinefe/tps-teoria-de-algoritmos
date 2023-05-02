import json
import random
import time


def generate_elements_sample(E, W=None):
    if W:
        sample = [1] * E     
        for i in range(E, W) : sample[random.randint(0, E-1)] += 1
        return sample
    else:
        return [random.randint(1, 1000) for _ in range(E)]

def generate_bribery(W):
    return random.randint(0, W)

def generate_elements_sample2(E=None, W=None):

    if W and E:
        sample = [1] * E     
        for i in range(E, W) : sample[random.randint(0, E-1)] += 1
        return sample

    if W:
        sample = [1] * 10   
        for _ in range(10, W) : sample[random.randint(0, 9)] += 1
        return sample
    
    return [random.randint(1, 1000) for _ in range(E)]

def generate_packets_and_briberies(P, E, W):
    """
    P: amount of distinct products
    E: max amount of packets, for each product
    W: max amount of individual products to keep (for each product)
    """
    products = [str(p) for p in range(P)]
    packets = {}
    briberies = {}

    for product in products:

        packets[product] = [random.randint(1, 1000) for _ in range(E)]
        tot_e = sum(packets[product])
        bribery = tot_e - W
        if bribery > 0:
            briberies[product] = bribery

    return packets, briberies

def generate_E_sample(sequence):
    samples = []

    for e in sequence:
        packets, briberies = generate_packets_and_briberies(1, e, 100)
        samples.append({"packets": packets, "briberies": briberies})

    return samples

def generate_W_sample(sequence):
    samples = []
    for w in sequence:
        packets, briberies = generate_packets_and_briberies(1, 100, w)
        samples.append({"packets": packets, "briberies": briberies})

    return samples

def generate_random_sample(sequence):
    samples = []
    for _ in range(1000):
        e = random.choice(sequence)
        w = random.choice(sequence)
        packets, briberies = generate_packets_and_briberies(1, e, w)
        samples.append({"packets": packets, "briberies": briberies})

    return samples


def main():
    # Configuracion de la simulacion
    with open("simconfig.json", "r") as config_file:
        config = json.load(config_file)

    sample = {}
    sample["config"] = config

    generator = eval(f"generate_{config['var']}_sample")
    sample["sample"] = generator(range(config["start"], config["stop"], config["step"]))

    # Stringificacion del json
    json_dump_sample = json.dumps(sample, indent=4)

    # Escritura del json
    filename = time.strftime("%Y-%m-%d_%H-%M-%S")
    with open(f'samples/{filename}.json', 'w+') as file:
        file.write(json_dump_sample)
    


if __name__ == "__main__":
    main()