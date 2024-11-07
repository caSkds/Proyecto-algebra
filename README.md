# Proyecto-algebra
Proyecto de álgebra de Daniel, César y Ángel

## Requisitos 
El programa usa Python 3.13.0 disponible en https://www.python.org/downloads/
, así como la librería Numpy
`pip install numpy`

## Rúbrica de evaluación


## División sintética

  ### Formato de datos
  La división sintética usa el método `get_Input()` del archivo `complexInput.py`. Por tanto el formato de los datos (para pedir las raíces y/o coeficienteS) es el mismo que el que se explica más abajo en el reporte, en la sección de `complexInput.py`. Para pedir el número de términos se pide un solo número natural mayor a 1. 
  ### Explicación del código
  Lo primero que hace el código es pedir el número de términos. Para una mejor experiencia de usuario (y esto se hará cada que se pida una entrada) se encapsula la entrada dentro de un ciclo while. Este tiene dentro un bloque try/except, y solo en caso de obtener una entrada válida se sale del ciclo while. 
  

  #### Pidiendo número de términos y términos
  Primero se pide el número de términos, verificando que no sea menor o igual a 1, de lo contrario se interpreta como un error y se repite el ciclo. A partir de aquí, usando el método `get_Input()`se pide la raíz a evaluar. Posteriormente se usa un ciclo for para pedir justo el número de coeficientes como términos, pidiendo primero el término independiente, seguido del lineal y del cuadrático o más (en caso de haber). Estos términos se añaden a la lista `coeficientes`. 
  <details>
    <summary>
      Código 
    </summary>
    
```
    # Solicita el número de térmionos
while True:
    try:
        nTerminos = int(input("Introduce el n de terminos: "))
        if nTerminos <= 1:
            print("Debe introducir un entero mayor a 1")
            raise Exception
        break
    except :
        print("Debe introducir un numero entero")

#Luego se pide la raíz a evaluar
while True:
    try:
        root = cO.get_Input("Introduce la raiz a evaluar: ")

        break
    except :
        print("Debe introducir un número")

#Se piden los coeficientes
coeficientes = []
desarrollo=[]
desarrollo.append(" ")
for i in range(nTerminos):
    while True:
        try:
            print("Introduce el coeficiente de x^" + str(i) + ": ")
            coeficientes.append(cO.get_Input(""))
            break
        except :
            print("Debe introducir un número")
```
- Cabe aclarar que la lista `desarrollo` será importante para desarrollar el segundo renglón de la división sintética
  </details>
  

  #### Realizando la división sintética
  Dado que se pide en orden reversado los coeficientes, el último elemento de la lista de coeficientes será el primer elemento de 
  ### Ejercicios de prueba

## Método Gauss-Jordan
  ### Formato de datos
  ### Explicación del código
  ### Ejercicios de prueba

## Operaciones con matrices
  ### Formato de datos
  ### Explicación del código
  ### Ejercicios de prueba

  ## complexInput.py

 ###  Formato de datos
 
  Puede escribirse solo la parte real como si fuera un número normal o como fracción, poniendo una diagonal entre el numerador y denominador. Puede escribirse solo la parte imaginaria añadiendo i después del número, de nuevo pudiendo poner fracciones. De tener parte real e imaginaria se deben de escribir primero la parte real, seguido de la parte imaginaria. No debe de incluir espacios y seguido de la parte iamginaria debe de colocarse la letra i.

  ### Explicación del código


## Conclusiones

### Daniel
-  ¿Qué realicé? (individual)
-  ¿Qué aprendí?
-  ¿Qué nos limitó?
-  ¿Cuál fue mi experiencia del trabajo en equipo?
-  ¿Cómo fue la comunicación (no el medio)?
-  ¿Qué debo mejorar?
### César
-  ¿Qué realicé? (individual)
-  ¿Qué aprendí?
-  ¿Qué nos limitó?
-  ¿Cuál fue mi experiencia del trabajo en equipo?
-  ¿Cómo fue la comunicación (no el medio)?
-  ¿Qué debo mejorar?

### Ángel
-  ¿Qué realicé? (individual)
-  ¿Qué aprendí?
-  ¿Qué nos limitó?
-  ¿Cuál fue mi experiencia del trabajo en equipo?
-  ¿Cómo fue la comunicación (no el medio)?
-  ¿Qué debo mejorar?



