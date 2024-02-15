#PRIMERA PRUEBA EN PYTHON
print("Primera prueba:")

#Se define la matriz (tenemos una matriz cuadrada de 3 x 3)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

def suma_diagonal(matriz): #Se define una funcion para tomar un parametro de la matriz que se espera que sea una lista de listas que represente una matriz
    suma = 0 #Iniciamos una variable llamada "suma" con un valor de 0 para almacenar el resultado
    for i in range(len(matriz)):   #Ejecutamos un bucle for que iterara la longitud de la matriz sobre las filas de la matriz
        suma += matriz[i][i]    #Por cada iteracion del bucle, se agrega el elemento de la matris correspondiente a la diagonal principal 
    return suma # Y finalmente obtenemos el resultado de la suma de las matriz obtenida 

#Se realiza al suma diagonal e imprime el resultado de la operacion
resultado = suma_diagonal(matriz)
print("La suma de la diagonal de la matriz es:", resultado)


#SEGUNDA PRUEBA EN PYTHON
print("Segunda Prueba:")

#Definimos el array
array = ['2', 'CASA', 'PRUEBA', '9', '-1']

def suma_numero(array):
    suma = 0
    for element in array:
        if element.isdigit():
            suma += int(element)
        else:
            print("No es un numero:", element)
        return suma
result = suma_numero(array)
print("La suma total de los numeros en el Array es:", result)