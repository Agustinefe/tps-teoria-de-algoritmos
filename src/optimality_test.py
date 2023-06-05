import random
from math import ceil, floor
from algorithms import backtracking_solution, approximation_solution
from time import time
from generator import generate_random_sample

EPSILON = 0.00000002

def flatten(l):
    return [item for sublist in l for item in sublist]

# k <= 1
def generate_vector_that_sums_k(size):
    vec = [1] * size

    for _ in range(0, 100-size):
        idx = random.randint(0, size-1)
        vec[idx] += 1 

    return list(map(lambda x: x / 100, vec))

def generate_bin_distribution(n, k):
    j = k
    nums = []
    for _ in range(n-1):
        num = random.randint(2, round(k/n))
        nums.append(num)

    nums.append(k - sum(nums))
    random.shuffle(nums)
    return nums

def generate_sample(n_bins, sizeof_T):

    possible_solution = []
    bin_sizes = generate_bin_distribution(n_bins, sizeof_T)
    for size in bin_sizes:
        possible_solution.append(generate_vector_that_sums_k(size))

    return possible_solution


def sim():

    #for t in range(4, 16):
    for t in range(15, 16):
        #for b in range(2, floor(t/2)):
        for b in range(6, 7):
            start = time()
            for i in range(1000):
                print(f'{i}) Tamaño: {t}, en {b} bins')
                resultado = generate_sample(b, t)
                print(f'Optimo: {resultado}')
                print()
                T = flatten(resultado)
                random.shuffle(T)
                start_b = time()
                solucion = backtracking_solution(T)
                end_b = time()
                print(end_b - start_b)
                print(f'Resultado: {solucion}: {len(solucion)}')
                if len(solucion) <= len(resultado) and all((sum(l) >= 1-EPSILON and sum(l) <= 1+EPSILON) for l in solucion):
                    print(f"Resultado optimo!")
                    print()
                else:
                    print(f'Resultado no optimo: deberia ser {sum(T)}; dio {len(solucion)}')
                    print(list(map(lambda x: sum(x), solucion)))
                    print(f'Resultado optimo: {resultado}')
                    return
            end = time()
            print(end - start)
            


#sim()

count = 0
max_rel = 1
for i in range(0, 100000):

    T = generate_sample(6, 12)
    sample = flatten(T)
    random.shuffle(sample)
    backtracking = backtracking_solution(sample)
    approximation = approximation_solution(sample)
    relation = len(approximation) / len(backtracking)
    if (relation > 1.5):
        print(f"{i}) ALERTA: HUBO UNO DE MAS DE 1.5")
        print(f'Aproximacion: {approximation}')
        print(f'Optimo: {backtracking}')
        print(f'Relacion: {relation}')
        if relation > max_rel:
            max_rel = relation

        print(f'Maxima relacion hasta ahora: {max_rel}')

        count += 1


print(f'Flasheos totales: {count}')
print(f'Maxima relacion: {max_rel}')









