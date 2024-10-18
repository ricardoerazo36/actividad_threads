#
# Este script define un hilo que se encarga de calcular la posicion 'n' en la 
# serie de Fibonacci.
#
# Autor: John Sanabria - john.sanabria@correounivalle.edu.co
# Fecha: 2023-01-10
#
from threading import Thread
from fibonacci import fibo
from time import time
import multiprocessing
import sys

num_cpus = multiprocessing.cpu_count() # CPUs disponibles
modules = 144 // num_cpus # Saber de a cuantos elementos le toca a cada trabajador
vector_fibo = [33] * 144 # Arreglo de 144 elementos inicializados en 33

class FiboWorker(Thread):
  def __init__(self, n,tid):
    Thread.__init__(self)
    self.n = n
    self.tid = tid

  def run(self):
     for i in range(self.tid * modules, ((self.tid + 1) * modules) - 1): # Dependiendo de los nucleos cada constructor le corresponde unas posiciones determinadas
      vector_fibo[i] = fibo(vector_fibo[i])
      print(f"[{self.tid}][{i}] Fibonacci de {self.n} es {vector_fibo[i]}")

def main():
  
  print(f"Calculando el fibonacci {33} en {num_cpus} CPUs")
  hilos = [] # Vector de hilos
  ts = time() # se toma tiempo 
  for x in range(num_cpus): # Ciclo para crear trabajadores
    print(f"Trabajador {x} comienza")
    worker = FiboWorker(33,x)
    worker.start()
    hilos.append(worker)

  for x in range(num_cpus): # Ciclo para esperar por trabajadores
    print(f"Esperando por trabajador {x}")
    hilos[x].join()

  print(f"Tomo {time() - ts}")


if __name__ == "__main__":
  main()
