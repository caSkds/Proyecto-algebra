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
  Dado que se pide en orden reversado los coeficientes, el último elemento de la lista de coeficientes será el primer elemento de la lista que refleje el resultado. Dado que tenemos que operar con los coeficientes en orden (del término de grado mayor al menor hasta llegar al independiente), iteramos al revés en la lista. Empezamos agarrando el elemento que vamos a operar (`current`). Este empieza siendo el coeficiente del término de mayor grado (índice -1 de la lista de coeficientes, mismo que se agrega al primer elemento de la lista `resultado`, la cual será el tercer renglón de la división sintética).

  Comenzando con la iteración, se itera al reves en la lista de coeficientes para permitir que se opere del elemento de mayor grado al menor. A la lista `desarrollo` agregamos el elemento que estamos operando actualmente multiplicado por la raíz. El elemento actual ahora será si mismo multiplicado por la raíz, sumado al coeficiente correspondiente del polinomio original. Añadimos este elemento a la lista resultado y el ciclo se repite.
<details>
  <summary>
    Código
  </summary>
  
  ```
  resultado =[]
resultado.append(coeficientes[-1])
#holds current third line synthetic value
current = coeficientes[-1]


# synthetic division
for i in range(len(coeficientes)-1,0,-1):
    desarrollo.append(current*root)
    current = current*root + coeficientes[i-1]
    resultado.append(current)
```
</details>
  
  #### Dando formato a la salida

  Para la salida se imprime lo siguiente:
  - 3 listas, cada una correspondiente al primer, segundo y tercer renglón de la división sintética
  - Mensaje acorde a si la raíz dada si fue raíz o no del polinomio
  - En caso de ser la raíz dada, el prorgama imprime el polinomio factorizado por la raíz

    Se eligió que se imprimieran 3 listas, pues hay demasiada variedad en los decimales que pueden surgir en una fracción, haciendo la creación de strings correspondientes a los resultados cuando menos impráctico y confuso. Al imprimirlo en listas, se puede comparar más fácilmente elemento a elemento para su mejor interpretación.

    Lo más importante del formato fue que hubiera una i para la parte compleja. Esto se tiene que hacer así pues la clase `complex`en python comunmente usa j para rerpresentar ala parte compleja. Para esto se creó la función `formatOutput(linea,fuente, inico=0,paso=1)`. Esto se hizo así pues la misma función sería usada para los 3 renglones de la división sintética. La función toma la lista a la que se le quiera añadir los elementos (`linea`), de donde quiere que se obtengan los elemenots dados (`fuente`) así como un indice desde el cual se iniciaría a revisar (`inicio`, que por defecto es 0, el primer elemento de la lista) así como una variable `paso`. Si su valor es -1 se iterará en la fuente al revés, de lo contrario se iterará normalmente. La necesidad de esto viene de la lista de coeficientes.

     La función de `formatOutput`es tomar cada elemento de la fuente y transformarlo a una string que represente un elemento similar a `a+bi` y se añada a la lista que será la salida. Para esto se evalua si la parte real o imaginaria son 0 (para solo poner la parte real o imaginaria en caso de que solo exista una). Si la real es 0, solo se añade la imaginaria más la letra i. Si la parte imaginaria es 0 se añade la real tal como es. En caso de haber ambas y que la imaginaria sea menor a 0, se añaden las 2 tal como son a la string que será mostrada a la salida seguido de una i. De no ser así se añade el signo + en medio.

<details>
  <summary>
        Código de `formatOutput`
  </summary>

```
  #formatting the result list 
thirdLine = []
def formatOutput(linea, fuente, inicio=0,paso=1):
    reversed=[]
    if paso ==-1:
        reversed  = fuente[::-1]
    else:
        reversed = fuente
    
    for i in reversed[inicio:]:
        if i == zero:
            linea.append("0.0")
        elif i.imag ==0:
            linea.append(str(i.real))
        elif i.real ==0: 
            linea.append(str(i.imag) + "i")
        elif i.imag <0:
            linea.append( str(i.real)  + str(i.imag) + "i")
        else:
            linea.append(str(i.real) + "+" + str(i.imag) + "i")
formatOutput(firstLine,coeficientes,0,-1)
formatOutput(secondLine,desarrollo,1)
formatOutput(thirdLine, resultado)
```
</details>

    

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



