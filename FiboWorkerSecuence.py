from fibonacci import fibo
from time import time
import multiprocessing
import sys

ts = time()

def main():
    max_fibo = 33
    if len(sys.argv) != 1:
        max_fibo = int(sys.argv[1])
    num_cpus = multiprocessing.cpu_count() # CPUs disponibles
    vectorFibo = []
    for x in range(144):
        vectorFibo.append(fibo(max_fibo))
        print(f"El número fibonacci para la posición [{x}] es {fibo(max_fibo)}\n")

    print(f"Tomó {time() - ts}")

if __name__ == "__main__":
  main()
