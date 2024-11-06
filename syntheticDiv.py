import complexInput as cO

#Raiz a evaluar
root = complex(0,0)
#salida de raiz
raiz = ""

#N. de terminos
nTerminos = 0
#lista con coeficientes
coeficientes=[]
#Resultado, tercer linea de la division sintetica
resultado =[]
#zero complex 
zero = complex(0,0)
#tercer línea
thirdLine=[]
#segunda linea
secondLine=[]
secondLine.append(" ")
#primer linea
firstLine=[]
#desarrollo
desarrollo=[]


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



resultado =[]
resultado.append(coeficientes[-1])
#holds current third line synthetic value
current = coeficientes[-1]


# synthetic division
for i in range(len(coeficientes)-1,0,-1):
    desarrollo.append(current*root)
    current = current*root + coeficientes[i-1]
    resultado.append(current)


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


#formatting the root 
def formatRoot():
    global raiz
    global root
    if root == zero:
        raiz = '0'
    elif root.imag ==0:
        raiz = str(root.real)
    elif root.real ==0: 
        raiz = str(root.imag) + "i"
    elif root.imag <0:
        raiz =  str(root.real)  + str(root.imag) + "i"
    else:
        raiz = str(root.real) + "+" + str(root.imag) + "i"

formatRoot()

def imprimir_proceso():
    print(firstLine)
    print(secondLine)
    print(thirdLine)    
imprimir_proceso()

#dar formato a numeros copmlejos individuales:
def formatNumber(numero: complex):
    global zero
    nuevoNum = []

    if numero == zero:
        nuevoNum.append ('0')
    elif numero.imag ==0:
        nuevoNum.append(str(numero.real))
    elif numero.real ==0: 
        nuevoNum.append(str(numero.imag) + "i")
    elif numero.imag <0:
        nuevoNum.append( str(numero.real)  + str(numero.imag) + "i")
    else:
        nuevoNum.append(str(numero.real) + "+" + str(numero.imag) + "i")
    salida= " ".join(nuevoNum)
    return salida

# imprime el polinomio final
def polinomio_Final(resultado):
    global root
    global zero
    elementosPolinomioFinal = []
    elementosRestantes = []
    # Se encarga del primer elemento
    elementosPolinomioFinal.append("(x")
    root = root*-1
    formatRoot()
    if root.imag==0 and root.real>0 or root.real ==0 and root.imag>0:
        elementosPolinomioFinal.append(" + ")
    elif root == zero:
        elementosPolinomioFinal.append(" - ")
    elif root.real>0:
        elementosPolinomioFinal.append(" + ")
    elementosPolinomioFinal.append(raiz)
    elementosPolinomioFinal.append(")")
    # Se encarga de raices con más elemenots
    while True:
        if len(resultado )== 2:
            break
        else:
            j=0
            for i in range(len(resultado)-2,-1,-1):
                
                elementosRestantes.append("(")
                elementosRestantes.append(formatNumber(resultado[j]))
                elementosRestantes.append(")")
                elementosRestantes.append("x^")
                elementosRestantes.append(str(i))
                elementosRestantes.append(" + ")
                j = j+1
            elementosRestantes.pop()
            elementosRestantes.append(")")
            
        break

    for i in elementosRestantes :
        elementosPolinomioFinal.append(i)
    PolinomioFinal = "".join(elementosPolinomioFinal)
    return PolinomioFinal        







def imprimir_resultado():
    global root
    if resultado[-1] == zero:
        root = root*-1
        formatRoot()
        print(raiz, " es raíz del polinomio")
        print(polinomio_Final(resultado))
    else:
        print(raiz +" no es raíz del polinomio")
imprimir_resultado()
