import sys
import time

from algorithms import backtracking_solution, approximation_solution, greedy_approximation_solution


def main():
    if len(sys.argv) != 3:
        print("Error: se debe invocar con: ./tdatp2 <E>|<A>|<A2> <datos.txt>")
        return

    option = sys.argv[1]
    filename = sys.argv[2]

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except IOError:
        print(f"Error: no se pudo abrir el archivo {filename}")
        return

    n = int(lines[0])
    T = [float(line.strip()) for line in lines[2:]]

    solution_map = {
        'E': backtracking_solution,
        'A': approximation_solution,
        'A2': greedy_approximation_solution,
    }

    start, end = None, None

    solution = None
    if option in solution_map:
        start = time.time()
        solution = solution_map[option](T)
        end = time.time()
    else:
        print("Error: las opciones válidas son: <E>|<A>|<A2>")
        return
    
    print(f"{solution}: {len(solution)}")
    print((end-start) * 1000)

    return


if __name__ == "__main__":
    main()