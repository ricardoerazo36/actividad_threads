from fibonacci import fibo
from time import time
import multiprocessing
import sys

def main():
    ts = time() # se toma tiempo
   
    vectorFibo = [33] * 144 # Arreglo de 144 elementos inicializados en 33
    for x in range(144):
        old_value = vectorFibo[x]
        vectorFibo[x] = fibo(vectorFibo[x])
        
        print(f"[{x}] Fibonacci de {old_value} es {vectorFibo[x]}\n")

    print(f"Tomó {time() - ts}")

if __name__ == "__main__":
  main()
