# Método de Gauss-Jordan para resolver un sistema de ecuaciones lineales V 3.3 
#se usa para calcular los valores de un sistema de ecuaciones de "n x m" dimensiones

import numpy as nump
from fractions import Fraction
import time
# Función para definir los elementos

def metodoMatriz():
    # Se define primero la cantidad de ecuaciones que desea el usuario
    numeroElementos = int(input("Ingrese el número de ecuaciones a realizar y cantidad de variables: "))
    matElem = []

    if numeroElementos == 0: #Bromita 
        print("El numero de ecuaciones no puede ser 0... iniciando desinstalacion de windows")
        for i in range(5, 0, -1):
            print(f"{i}...")
            time.sleep(1)
        raise ValueError("No puede haber ecuaciones con 0... afortunadamente no teniamos polvora")
    
    matElem = []

    for i in range(numeroElementos):
        print(f"Introduzca los coeficientes de tu ecuación (de x más elevado al independiente) {i+1} separándolos por espacios:")
        numElem = input().split()
        ecuacionInd = [Fraction(x) for x in numElem]  # Convierte los elementos a fracciones
        matElem.append(ecuacionInd)

    # Convierte la lista en un array de Numpy con elementos de tipo fracción
    # la funcion np ayudara a hacer que el array de "matElem" puedra trabajar con elementos de fracion si a/b
    matElem_np = nump.array(matElem, dtype=object)
    return matElem_np, numeroElementos  # Devuelve la matriz y el número de ecuaciones

def gauss_jordan_fracc(matriz, numeroElementos):
    for i in range(numeroElementos):
        elementoUno = matriz[i][i]
        if elementoUno == 0:
            raise ValueError("El sistema que ingresaste no tiene forma de realizarse (división por 0 = IND)")   #se usa el raise para parar el programa, usar print causa conflictos xd
        
        matriz[i] = matriz[i] / elementoUno  # Normaliza la fila dividiendo por el elemento principal
        
        for j in range(numeroElementos):  # Hace ceros en los elementos fuera de la diagonal
            if i != j:
                factor = matriz[j][i]
                matriz[j] = matriz[j] - factor * matriz[i]
    
    solucion = matriz[:, -1]  # Toma la última columna como las soluciones
    return solucion


if __name__ == "__main__":
    print("Método de Gauss-Jordan V 3.2: La revancha de ValueError")
    metodo, numeroElementos = metodoMatriz()  # Obtiene la matriz y el número de ecuaciones
    
    try:
        soluciones = gauss_jordan_fracc(metodo, numeroElementos)
        print("\nLa solución a su sistema es:")
        for i, solus in enumerate(soluciones):  # Enumera las soluciones y las imprime
            print(f"x del conjunto {i+1} es {solus}")
    except ValueError as f:
        print(f"Error: {f}")
