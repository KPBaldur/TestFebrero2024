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



# Definir el arreglo
arreglo = ['2', 'CASA', 'PRUEBA', '9', '-1']


def suma_numeros(arreglo): #Seguimos con la misma logica que en el ejercicio anterior
    suma = 0    #Creamos la variable suma iniciando con un valor 0
    for elemento in arreglo:
        if elemento.isdigit():  # Verificar si el elemento es un dígito
            suma += int(elemento) 
        else:
            print("No es un número:", elemento)  #Generamos un parametro para discriminar si el elemento en el arreglo es o no un numero
    return suma if suma != 0 else None  # Si no se encontraron números, devolver None



# Sumar los números en el arreglo e imprimir el resultado
resultado = suma_numeros(arreglo)
if resultado is not None:  # Verificar si la suma no es None
    print("La suma total de los números en el arreglo es:", resultado)
else:
    print("No se encontraron números en el arreglo.")
