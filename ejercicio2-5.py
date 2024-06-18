import numpy as np
from scipy.sparse import random, csr_matrix
from multiprocessing import Pool, cpu_count

def multiply_rows(args):
    row, matrix2 = args
    return row.dot(matrix2)

# Crear dos matrices sparse aleatorias
filas, columnas = 1000, 1000
density = 0.01

matrix1 = random(filas, columnas, density=density, format='csr')
matrix2 = random(filas, columnas, density=density, format='csr')

# Multiplicar las matrices sparse en paralelo por filas
num_cores = cpu_count()
with Pool(num_cores) as pool:
    args = [(matrix1.getrow(i), matrix2) for i in range(filas)]
    resultados = pool.map(multiply_rows, args)

# Convertir los resultados a matrices dispersas
resultados_dispersos = [csr_matrix(result) for result in resultados]

# Combinar los resultados en una matriz sparse única
resultado_sparse = sum(resultados_dispersos)

# Imprimir dimensiones de la matriz resultante
print(f"Dimensiones de la matriz resultante: {resultado_sparse.shape}")
