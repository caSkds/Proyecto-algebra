# Funciones para manejar polinomios, sistemas de ecuaciones, matrices y números complejos

def ingresar_polinomio():
    """
    Función para ingresar un polinomio.
    Retorna una lista de coeficientes desde el término de mayor grado hasta el término independiente.
    """
    grado = int(input("Ingrese el grado del polinomio: "))
    coeficientes = []
    print("Ingrese los coeficientes desde el término de mayor grado hasta el término independiente:")
    for i in range(grado, -1, -1):
        coef = float(input(f"Coeficiente de x^{i}: "))
        coeficientes.append(coef)
    return coeficientes

def ingresar_matriz():
    """
    Función para ingresar una matriz.
    Retorna una lista de listas donde cada sublista representa una fila de la matriz.
    """
    filas = int(input("Ingrese el número de filas de la matriz: "))
    columnas = int(input("Ingrese el número de columnas de la matriz: "))
    matriz = []
    print("Ingrese los elementos de la matriz:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = float(input(f"Elemento [{i+1}][{j+1}]: "))
            fila.append(elemento)
        matriz.append(fila)
    return matriz

def dividir_sintetica(coeficientes, raiz):
    """
    Realiza la división sintética de un polinomio por (x - raiz).
    Retorna una lista con los coeficientes del polinomio resultante.
    """
    print(f"\nDividiendo el polinomio por (x - {raiz}) utilizando división sintética:")
    resultado = []
    temporal = coeficientes[0]  # Inicializa con el coeficiente líder
    resultado.append(temporal)
    print(f"Paso 1: {temporal}")
    for coef in coeficientes[1:]:
        temporal = temporal * raiz + coef  # Calcula el siguiente coeficiente
        resultado.append(temporal)
        print(f"Paso siguiente: {temporal}")
    return resultado

def evaluar_raices(coeficientes):
    """
    Evalúa posibles raíces de un polinomio usando el teorema de las raíces racionales.
    """
    posibles_raices = encontrar_posibles_raices(coeficientes)  # Obtiene posibles raíces
    raices_encontradas = []
    for raiz in posibles_raices:
        print(f"\nEvaluando la posible raíz: {raiz}")
        resultado = dividir_sintetica(coeficientes, raiz)  # Realiza división sintética
        residuo = resultado[-1]  # Último elemento es el residuo
        if residuo == 0:
            print(f"El valor {raiz} es una raíz del polinomio.")
            raices_encontradas.append(raiz)
            # Obtener el polinomio reducido
            polinomio_reducido = resultado[:-1]
            print("Polinomio reducido después de la división sintética:")
            imprimir_polinomio(polinomio_reducido)
        else:
            print(f"El valor {raiz} no es una raíz del polinomio.")
    if not raices_encontradas:
        print("No se encontraron raíces racionales.")
    return raices_encontradas

def encontrar_posibles_raices(coeficientes):
    """
    Encuentra posibles raíces racionales de un polinomio usando el teorema de las raíces racionales.
    """
    from math import gcd
    def factores(n):
        """
        Retorna una lista de factores positivos de n.
        """
        n = abs(n)
        if n == 0:
            return [0]
        return [i for i in range(1, n+1) if n % i == 0]
    
    term_ind = coeficientes[-1]  # Término independiente
    coef_lead = coeficientes[0]   # Coeficiente líder
    factores_ind = factores(int(term_ind)) if term_ind != 0 else [0]
    factores_lead = factores(int(coef_lead)) if coef_lead != 0 else [1]
    posibles = set()
    for p in factores_ind:
        for q in factores_lead:
            if q != 0:
                posibles.add(p/q)   # Agrega p/q
                posibles.add(-p/q)  # Agrega -p/q
    return sorted(posibles)

def imprimir_polinomio(coeficientes):
    """
    Imprime el polinomio de manera legible.
    """
    grado = len(coeficientes) -1
    polinomio = ""
    for i, coef in enumerate(coeficientes):
        if coef == 0:
            continue  # Omite términos con coeficiente cero
        exponente = grado - i
        if polinomio != "" and coef > 0:
            polinomio += " + "  # Agrega '+' si es positivo y no es el primer término
        elif coef < 0:
            polinomio += " - "  # Agrega '-' si es negativo
        else:
            polinomio += ""
        coef_abs = abs(coef)
        if exponente == 0:
            polinomio += f"{coef_abs}"  # Término independiente
        elif exponente ==1:
            polinomio += f"{coef_abs}x"  # Término lineal
        else:
            polinomio += f"{coef_abs}x^{exponente}"  # Términos de mayor grado
    print(polinomio if polinomio else "0")  # Imprime el polinomio o '0' si está vacío

def gauss_jordan(matriz, b):
    """
    Resuelve un sistema de ecuaciones lineales usando el método de Gauss-Jordan.
    """
    n = len(matriz)  # Número de ecuaciones
    # Crear matriz aumentada combinando coeficientes y términos independientes
    for i in range(n):
        matriz[i].append(b[i])
    
    print("\nAplicando el método de Gauss-Jordan:")
    for i in range(n):
        print(f"\nPaso {i+1}:")
        # Buscar el mayor elemento en la columna i para el pivote
        max_el = abs(matriz[i][i])
        max_row = i
        for k in range(i+1, n):
            if abs(matriz[k][i]) > max_el:
                max_el = abs(matriz[k][i])
                max_row = k
        # Intercambiar filas si es necesario
        matriz[i], matriz[max_row] = matriz[max_row], matriz[i]
        print(f"Intercambio de fila {i+1} con fila {max_row+1}: {matriz}")
        # Hacer que el elemento diagonal sea 1
        diag = matriz[i][i]
        if diag == 0:
            print("No hay solución única.")
            return None
        for j in range(i, n+1):
            matriz[i][j] /= diag
        print(f"Hacer que el elemento [{i+1}][{i+1}] sea 1: {matriz[i]}")
        # Hacer que todos los demás elementos en la columna i sean 0
        for k in range(n):
            if k != i:
                factor = matriz[k][i]
                for j in range(i, n+1):
                    matriz[k][j] -= factor * matriz[i][j]
                print(f"Hacer cero el elemento [{k+1}][{i+1}]: {matriz[k]}")
    
    # Extraer soluciones de la matriz reducida
    soluciones = [matriz[i][-1] for i in range(n)]
    print("\nSoluciones del sistema:")
    for idx, sol in enumerate(soluciones):
        print(f"x{idx+1} = {sol}")
    return soluciones

def suma_matrices(A, B):
    """
    Suma dos matrices elemento a elemento.
    """
    filas = len(A)
    columnas = len(A[0])
    resultado = []
    print("\nRealizando la suma de matrices:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            suma = A[i][j] + B[i][j]  # Suma de elementos correspondientes
            fila.append(suma)
            print(f"A[{i+1}][{j+1}] + B[{i+1}][{j+1}] = {A[i][j]} + {B[i][j]} = {suma}")
        resultado.append(fila)
    return resultado

def resta_matrices(A, B):
    """
    Resta dos matrices elemento a elemento.
    """
    filas = len(A)
    columnas = len(A[0])
    resultado = []
    print("\nRealizando la resta de matrices:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            resta = A[i][j] - B[i][j]  # Resta de elementos correspondientes
            fila.append(resta)
            print(f"A[{i+1}][{j+1}] - B[{i+1}][{j+1}] = {A[i][j]} - {B[i][j]} = {resta}")
        resultado.append(fila)
    return resultado

def multiplicacion_matrices(A, B):
    """
    Multiplica dos matrices.
    """
    filas_A = len(A)
    columnas_A = len(A[0])
    filas_B = len(B)
    columnas_B = len(B[0])
    if columnas_A != filas_B:
        print("No se puede multiplicar: el número de columnas de A no es igual al número de filas de B.")
        return None
    resultado = []
    print("\nRealizando la multiplicación de matrices:")
    for i in range(filas_A):
        fila = []
        for j in range(columnas_B):
            suma = 0
            for k in range(columnas_A):
                suma += A[i][k] * B[k][j]  # Producto y suma de elementos
                print(f"A[{i+1}][{k+1}] * B[{k+1}][{j+1}] = {A[i][k]} * {B[k][j]} = {A[i][k]*B[k][j]}")
            fila.append(suma)
            print(f"Suma para elemento [{i+1}][{j+1}]: {suma}")
        resultado.append(fila)
    return resultado

def determinante(matriz):
    """
    Calcula el determinante de una matriz de forma recursiva usando el método de cofactores.
    """
    n = len(matriz)
    if n != len(matriz[0]):
        print("La matriz no es cuadrada, no tiene determinante.")
        return None
    if n == 1:
        # Determinante de 1x1
        print(f"Determinante de 1x1: {matriz[0][0]}")
        return matriz[0][0]
    if n == 2:
        # Determinante de 2x2
        det = matriz[0][0]*matriz[1][1] - matriz[0][1]*matriz[1][0]
        print(f"Determinante de 2x2: {matriz[0][0]}*{matriz[1][1]} - {matriz[0][1]}*{matriz[1][0]} = {det}")
        return det
    det = 0
    for c in range(n):
        # Calcula el cofactor para cada elemento de la primera fila
        cofactor = ((-1)**c) * matriz[0][c] * determinante(minor(matriz, 0, c))
        det += cofactor
        print(f"Cofactor para elemento [1][{c+1}]: {cofactor}")
    print(f"Determinante total: {det}")
    return det

def minor(matriz, i, j):
    """
    Obtiene la matriz menor eliminando la fila i y la columna j.
    """
    return [row[:j] + row[j+1:] for row in (matriz[:i] + matriz[i+1:])]

def matriz_inversa(matriz):
    """
    Calcula la matriz inversa usando la adjunta y el determinante.
    """
    n = len(matriz)
    det = determinante(matriz)  # Calcula el determinante
    if det == 0:
        print("La matriz no es invertible porque su determinante es 0.")
        return None
    # Crear matriz adjunta
    adjunta = []
    for i in range(n):
        fila = []
        for j in range(n):
            cofactor = ((-1)**(i+j)) * determinante(minor(matriz, i, j))
            fila.append(cofactor)
            print(f"Cofactor para elemento [{i+1}][{j+1}]: {cofactor}")
        adjunta.append(fila)
    # Transponer la matriz adjunta
    adjunta_transpuesta = transponer_matriz(adjunta)
    print("\nMatriz adjunta transpuesta (Adjunta):")
    imprimir_matriz(adjunta_transpuesta)
    # Dividir cada elemento de la adjunta transpuesta por el determinante
    inversa = []
    print("\nCalculando la matriz inversa:")
    for i in range(n):
        fila = []
        for j in range(n):
            inv = adjunta_transpuesta[i][j] / det  # División por el determinante
            fila.append(inv)
            print(f"Adjunta[{i+1}][{j+1}] / Det = {adjunta_transpuesta[i][j]} / {det} = {inv}")
        inversa.append(fila)
    return inversa

def transponer_matriz(matriz):
    """
    Transpone una matriz.
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    transpuesta = []
    for j in range(columnas):
        fila = []
        for i in range(filas):
            fila.append(matriz[i][j])  # Intercambia filas por columnas
        transpuesta.append(fila)
    return transpuesta

def imprimir_matriz(matriz):
    """
    Imprime una matriz de manera legible.
    """
    for fila in matriz:
        print(fila)

# Funciones para operaciones con números complejos

def ingresar_complejo():
    """
    Función para ingresar un número complejo.
    Retorna una lista [a, b] donde a es la parte real y b es la parte imaginaria.
    """
    print("Ingrese los componentes del número complejo:")
    a = float(input("Parte real (a): "))
    b = float(input("Parte imaginaria (b): "))
    return [a, b]

def sumar_complejos(c1, c2):
    """
    Suma dos números complejos.
    c1 y c2 son listas [a, b] representando a + bi.
    Retorna una lista [a+c, b+d].
    """
    suma_real = c1[0] + c2[0]  # Suma de partes reales
    suma_imag = c1[1] + c2[1]  # Suma de partes imaginarias
    print(f"Suma: ({c1[0]} + {c1[1]}i) + ({c2[0]} + {c2[1]}i) = {suma_real} + {suma_imag}i")
    return [suma_real, suma_imag]

def restar_complejos(c1, c2):
    """
    Resta dos números complejos.
    c1 y c2 son listas [a, b] representando a + bi.
    Retorna una lista [a-c, b-d].
    """
    resta_real = c1[0] - c2[0]  # Resta de partes reales
    resta_imag = c1[1] - c2[1]  # Resta de partes imaginarias
    print(f"Resta: ({c1[0]} + {c1[1]}i) - ({c2[0]} + {c2[1]}i) = {resta_real} + {resta_imag}i")
    return [resta_real, resta_imag]

def multiplicar_complejos(c1, c2):
    """
    Multiplica dos números complejos.
    c1 y c2 son listas [a, b] representando a + bi.
    Retorna una lista [a*c - b*d, a*d + b*c].
    """
    a, b = c1  # Desempaqueta la parte real y imaginaria del primer complejo
    c, d = c2  # Desempaqueta la parte real y imaginaria del segundo complejo
    mult_real = a * c - b * d  # Calcula la parte real del producto
    mult_imag = a * d + b * c  # Calcula la parte imaginaria del producto
    print(f"Multiplicación: ({a} + {b}i) * ({c} + {d}i) = {mult_real} + {mult_imag}i")
    return [mult_real, mult_imag]

def dividir_complejos(c1, c2):
    """
    Divide dos números complejos.
    c1 y c2 son listas [a, b] representando a + bi.
    Retorna una lista [(a*c + b*d)/(c^2 + d^2), (b*c - a*d)/(c^2 + d^2)].
    """
    a, b = c1  # Parte real e imaginaria del dividendo
    c, d = c2  # Parte real e imaginaria del divisor
    denominador = c**2 + d**2  # Calcula el denominador (c^2 + d^2)
    if denominador == 0:
        print("Error: División por cero en números complejos.")
        return None
    div_real = (a * c + b * d) / denominador  # Parte real de la división
    div_imag = (b * c - a * d) / denominador  # Parte imaginaria de la división
    print(f"División: ({a} + {b}i) / ({c} + {d}i) = {div_real} + {div_imag}i")
    return [div_real, div_imag]

def imprimir_complejo(c):
    """
    Imprime un número complejo en formato a + bi.
    c es una lista [a, b].
    """
    a, b = c
    if b >= 0:
        print(f"{a} + {b}i")
    else:
        print(f"{a} - {-b}i")

def operaciones_complejos():
    """
    Función que maneja las operaciones con números complejos.
    Permite al usuario elegir entre suma, resta, multiplicación y división.
    """
    print("\n--- Operaciones con Números Complejos ---")
    print("1. Suma de números complejos")
    print("2. Resta de números complejos")
    print("3. Multiplicación de números complejos")
    print("4. División de números complejos")
    print("5. Volver al menú principal")
    opcion = input("Seleccione una opción: ")
    
    if opcion in ['1', '2', '3', '4']:
        # Ingresar los dos números complejos
        print("\nIngrese el primer número complejo:")
        c1 = ingresar_complejo()
        print("\nIngrese el segundo número complejo:")
        c2 = ingresar_complejo()
        
        if opcion == '1':
            # Suma de complejos
            resultado = sumar_complejos(c1, c2)
            print("Resultado de la suma:")
            imprimir_complejo(resultado)
        
        elif opcion == '2':
            # Resta de complejos
            resultado = restar_complejos(c1, c2)
            print("Resultado de la resta:")
            imprimir_complejo(resultado)
        
        elif opcion == '3':
            # Multiplicación de complejos
            resultado = multiplicar_complejos(c1, c2)
            print("Resultado de la multiplicación:")
            imprimir_complejo(resultado)
        
        elif opcion == '4':
            # División de complejos
            resultado = dividir_complejos(c1, c2)
            if resultado:
                print("Resultado de la división:")
                imprimir_complejo(resultado)
    
    elif opcion == '5':
        # Volver al menú principal
        return
    
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
        # Llamada recursiva para intentar de nuevo
        operaciones_complejos()

def menu():
    """
    Menú principal del programa que permite al usuario seleccionar diferentes operaciones.
    """
    while True:
        print("\n--- Calculadora de Polinomios, Sistemas de Ecuaciones, Matrices y Números Complejos ---")
        print("1. Evaluar raíces de un polinomio (División Sintética)")
        print("2. Resolver un sistema de ecuaciones (Gauss-Jordan)")
        print("3. Operaciones con matrices")
        print("4. Operaciones con números complejos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            # Evaluar raíces de un polinomio
            polinomio = ingresar_polinomio()
            imprimir_polinomio(polinomio)
            evaluar_raices(polinomio)
        
        elif opcion == '2':
            # Resolver un sistema de ecuaciones por Gauss-Jordan
            print("\nResolución de un sistema de ecuaciones por Gauss-Jordan:")
            filas = int(input("Ingrese el número de variables (ecuaciones): "))
            matriz = []
            b = []
            for i in range(filas):
                print(f"\nEcuación {i+1}:")
                fila = []
                for j in range(filas):
                    coef = float(input(f"Coeficiente de x{j+1}: "))
                    fila.append(coef)
                matriz.append(fila)
                const = float(input("Término independiente: "))
                b.append(const)
            imprimir_matriz(matriz)
            soluciones = gauss_jordan(matriz, b)
        
        elif opcion == '3':
            # Operaciones con matrices
            print("\nOperaciones con matrices:")
            print("a. Suma de matrices")
            print("b. Resta de matrices")
            print("c. Multiplicación de matrices")
            print("d. Determinante de una matriz")
            print("e. Matriz inversa")
            sub_opcion = input("Seleccione una sub-opción: ")
            
            if sub_opcion.lower() in ['a', 'b', 'c']:
                # Suma, Resta o Multiplicación de matrices
                print("\nIngrese la primera matriz:")
                A = ingresar_matriz()
                print("\nIngrese la segunda matriz:")
                B = ingresar_matriz()
                if sub_opcion.lower() == 'a':
                    # Suma de matrices
                    if len(A) != len(B) or len(A[0]) != len(B[0]):
                        print("Las matrices deben tener las mismas dimensiones para la suma.")
                    else:
                        resultado = suma_matrices(A, B)
                        print("Resultado de la suma:")
                        imprimir_matriz(resultado)
                elif sub_opcion.lower() == 'b':
                    # Resta de matrices
                    if len(A) != len(B) or len(A[0]) != len(B[0]):
                        print("Las matrices deben tener las mismas dimensiones para la resta.")
                    else:
                        resultado = resta_matrices(A, B)
                        print("Resultado de la resta:")
                        imprimir_matriz(resultado)
                elif sub_opcion.lower() == 'c':
                    # Multiplicación de matrices
                    resultado = multiplicacion_matrices(A, B)
                    if resultado:
                        print("Resultado de la multiplicación:")
                        imprimir_matriz(resultado)
            
            elif sub_opcion.lower() in ['d', 'e']:
                # Determinante o Inversa de una matriz
                print("\nIngrese la matriz:")
                A = ingresar_matriz()
                if sub_opcion.lower() == 'd':
                    # Determinante de una matriz
                    det = determinante(A)
                    if det is not None:
                        print(f"El determinante de la matriz es: {det}")
                elif sub_opcion.lower() == 'e':
                    # Matriz inversa
                    inv = matriz_inversa(A)
                    if inv:
                        print("La matriz inversa es:")
                        imprimir_matriz(inv)
            else:
                print("Opción no válida.")
        
        elif opcion == '4':
            # Operaciones con números complejos
            operaciones_complejos()
        
        elif opcion == '5':
            # Salir del programa
            print("Saliendo del programa. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# Ejecutar el menú principal cuando se ejecuta el script
if __name__ == "__main__":
    menu()
