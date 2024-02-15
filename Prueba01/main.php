<?php
//Primer ejercicio PHP
echo "Primer ejercicio: \n";

// Definir la matriz
$matriz = array(
    array(1, 2, 3),
    array(4, 5, 6),
    array(7, 8, 9)
);

//Generamos una funcion para recorrer la matriz por filas y columnas de la misma forma que se hizo con Python

function suma_diagonal($matriz) {
    $suma = 0;
    for ($i = 0; $i < count($matriz); $i++) { //Creamos el loop e iteracion for para recorrer la matriz
        $suma += $matriz[$i][$i];
    }
    return $suma; //Y realizamos la suma y la retornamos a nuestra respuesta
}


// Sumar la diagonal e imprimir el resultado
$resultado = suma_diagonal($matriz);
echo "La suma de la diagonal de la matriz es: $resultado\n";


//Segundo Ejercicio
// Definir el arreglo
$arreglo = array('2', 'CASA', 'PRUEBA', '9', '-1');

//Funcion para recorrer el arreglo y discriminar si es un numero o string
function suma_numeros($arreglo) {
    $suma = 0;
    foreach ($arreglo as $elemento) {
        if (is_numeric($elemento)) {  // Verificar si el elemento es un número
            $suma += $elemento;
        } else {
            echo "No es un número: $elemento\n";
        }
    }
    return $suma;
}

// Sumar los números en el arreglo e imprimir el resultado
$resultado = suma_numeros($arreglo);
echo "La suma total de los números en el arreglo es: $resultado\n";

?>