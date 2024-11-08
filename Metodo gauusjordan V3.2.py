# metodo de gaus jordan alv

#se usa para calcular los valores de un sistema de ecuaciones de "n x m" dimensiones

import numpy as nump

from fractions import Fraction

#Funcion para definir los elementos

def metodoMatriz():
    #se define primero la cantidad de ecuaciones que desea el usuario
    numelemto = int(input("Ingrese el numero de ecuaciones a realizar y cantidad de variables: "))
    matElem=[]
    
    for i in range(numelemto):
     print(f"Introduzca los coeficientes de tu ecuacion (del x mas elevado al independiente) {i+1} separandolos por espacios")
     numElem = input().split()

     ecuacionInd = [Fraction(x) for x in numElem] #debe de convertir los elementos a fracciones para que funcione lo de abajo "NO MOVER"
     matElem.append(ecuacionInd)

    #momento de hacer que jale con fracciones (inspiracion divina ven a mi)
    #la funcion np ayudara a hacer que el array de "matElem" puedra trabajar con elementos de fracion si a/b
    matElem_np = nump.array(matElem, dtype=object)
    numElem = numeroElemento
    return matElem_np, numeroElemento

def gauss_jordan_fracc(matriz, n):
   for i in range(n):
      elementoUno = matriz[i][i]
      if elementoUno == 0:
         raise ValueError("el sistema que ingresaste no tiene forma de ralizarse a/0 = IND") #se usa el raise para parar el programa, usar print causa conflictos xd
      
      matriz[i] = matriz[i] / elementoUno #divide entre el elemento de valor 1
      
      for j in range(n): #hace 0 en los "triangulos"
         if i != j:
            factor = matriz[i][j] 
            matriz[j] = matriz[j] - factor * matriz[i]
            solucion = matriz[:, -1]
   return solucion

if __name__ == "__main__":
    print("Metodo chido de division de gauss jordan V 3.2 la revancha de raise errorvalue")
    metodo, numeroElemento = metodoMatriz()
    
    try:
       soluciones = gauss_jordan_fracc(metodo, numeroElemento)
       print("\n La solucion a su sitema es: ")
       for i, solus in enumerate(soluciones): #enumera las soluciones que se encuentran
            print(f"x del conjunto {i+1} es {solus}")
    except ValueError as f:
       print(f"Error en {f}")
