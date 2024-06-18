import numpy as np
from scipy.sparse import csr_matrix

# Crear matrices sparse de ejemplo
size = 1000

def generate_sparse_matrix(size, density=0.01):
    """Genera una matriz sparse aleatoria de tamaño dado y densidad"""
    rows = np.random.randint(0, size, int(size * size * density))
    cols = np.random.randint(0, size, int(size * size * density))
    data = np.random.rand(len(rows))
    return csr_matrix((data, (rows, cols)), shape=(size, size))

sparse_matrix1 = generate_sparse_matrix(size)
sparse_matrix2 = generate_sparse_matrix(size)

# Multiplicación de matrices sparse
result = sparse_matrix1.dot(sparse_matrix2)

# Mostrar una parte del resultado para verificar
print("Resultado de la multiplicación (una parte de la matriz):")
print(result[:10, :10].toarray())
