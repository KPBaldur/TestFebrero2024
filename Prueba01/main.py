#Se define la matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def suma_diagonal(matriz):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][i]
    return suma

#Se realiza al suma diagonal e imprime el resultado de la operacion
resultado = suma_diagonal(matriz)
print("La suma de la diagonal de la matriz es:", resultado)