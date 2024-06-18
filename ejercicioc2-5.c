#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

// Definir dimensiones de la matriz
#define FILAS 1000
#define COLUMNAS 1000

// Función para multiplicar matrices sparse
void multiply_matrices(double **matriz1, double **matriz2, double **resultado) {
    #pragma omp parallel for
    for (int i = 0; i < FILAS; i++) {
        for (int j = 0; j < COLUMNAS; j++) {
            resultado[i][j] = 0;
            for (int k = 0; k < COLUMNAS; k++) {
                resultado[i][j] += matriz1[i][k] * matriz2[k][j];
            }
        }
    }
}

int main() {
    // Inicializar matrices
    double *matriz1 = (double *)malloc(FILAS * sizeof(double *));
    double *matriz2 = (double *)malloc(FILAS * sizeof(double *));
    double *resultado = (double *)malloc(FILAS * sizeof(double *));

    if (matriz1 == NULL || matriz2 == NULL || resultado == NULL) {
        fprintf(stderr, "Error de asignación de memoria para las matrices principales.\n");
        return 1;
    }

    for (int i = 0; i < FILAS; i++) {
        matriz1[i] = (double *)malloc(COLUMNAS * sizeof(double));
        matriz2[i] = (double *)malloc(COLUMNAS * sizeof(double));
        resultado[i] = (double *)malloc(COLUMNAS * sizeof(double));

        if (matriz1[i] == NULL || matriz2[i] == NULL || resultado[i] == NULL) {
            fprintf(stderr, "Error de asignación de memoria para las filas.\n");
            return 1;
        }
    }

    // Rellenar matrices con valores aleatorios
    for (int i = 0; i < FILAS; i++) {
        for (int j = 0; j < COLUMNAS; j++) {
            matriz1[i][j] = (double)(rand() % 10);
            matriz2[i][j] = (double)(rand() % 10);
        }
    }

    // Multiplicar matrices con OpenMP
    multiply_matrices(matriz1, matriz2, resultado);

    // Imprimir dimensiones de la matriz resultante
    printf("Dimensiones de la matriz resultante: %d x %d\n", FILAS, COLUMNAS);

    // Liberar memoria
    for (int i = 0; i < FILAS; i++) {
        free(matriz1[i]);
        free(matriz2[i]);
        free(resultado[i]);
    }
    free(matriz1);
    free(matriz2);
    free(resultado);

    return 0;
}
