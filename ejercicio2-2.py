import numpy as np
from scipy.sparse import csr_matrix

# Ejemplo de representación de gráficos como listas de adyacencia
graph1 = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}

graph2 = {
    0: [2],
    1: [2],
    2: [0, 1]
}

def graph_to_sparse_matrix(graph, size):
    rows, cols = [], []
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            rows.append(node)
            cols.append(neighbor)
    data = np.ones(len(rows))
    sparse_matrix = csr_matrix((data, (rows, cols)), shape=(size, size))
    return sparse_matrix

# Convertir gráficos a matrices sparse
size = 3  # Tamaño de la matriz
sparse_matrix1 = graph_to_sparse_matrix(graph1, size)
sparse_matrix2 = graph_to_sparse_matrix(graph2, size)

print("Sparse Matrix 1:")
print(sparse_matrix1.toarray())

print("Sparse Matrix 2:")
print(sparse_matrix2.toarray())
