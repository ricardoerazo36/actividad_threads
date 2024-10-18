
#
# Este script define un hilo que se encarga de calcular la posicion 'n' en la 
# serie de Fibonacci.
#
# Autor: John Sanabria - john.sanabria@correounivalle.edu.co
# Fecha: 2023-01-10
#
from fibonacci import fibo
from time import time
import multiprocessing
import sys

num_cpus = multiprocessing.cpu_count() # CPUs disponibles
modules = 144 // num_cpus # Saber de a cuantos elementos le toca a cada trabajador
vector_fibo = [33] * 144 # Arreglo de 144 elementos inicializados en 33

class FiboWorker(multiprocessing.Process):

  def __init__(self, n, pid):
    multiprocessing.Process.__init__(self)
    self.n = n
    self._pid = pid

  def run(self):
    for i in range(self._pid * modules, ((self._pid + 1) * modules) - 1): # Dependiendo de los nucleos cada constructor le corresponde unas posiciones determinadas
      vector_fibo[i] = fibo(vector_fibo[i])
      print(f"[{self._pid}][{i}] Fibonacci de {self.n} es {vector_fibo[i]}")

def main():
  ts = time() # se toma tiempo 

  print(f"Calculando el fibonacci {33} en {num_cpus} CPUs")
  procesos = [] # Vector de procesos
  
  for x in range(num_cpus): # Ciclo para crear trabajadores
    print(f"Trabajador {x} comienza")
    worker = FiboWorker(33,x)
    worker.start()
    procesos.append(worker)

  for x in range(num_cpus): # Ciclo para esperar por trabajadores
    print(f"Esperando por trabajador {x}")
    procesos[x].join()

  print(f"Tomo {time() - ts}")


if __name__ == "__main__":
  main()
