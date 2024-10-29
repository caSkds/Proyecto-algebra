import complexInput as cO
#Primero se pide el n. de términos al usuario

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

if resultado[-1] == zero:
    raiz = '0'
elif resultado[-1].imag ==0:
    raiz = str(root.real)
elif resultado[-1].real ==0: 
    raiz = str(root.imag) + "i"
elif resultado[-1].imag <0:
    raiz =  str(root.real)  + str(root.imag) + "i"
else:
    raiz = str(root.real) + "+" + str(root.imag) + "i"


print(firstLine)
print(secondLine)
print(thirdLine)    

if resultado[-1] == zero:
    print(raiz, " es raíz del polinomio")
else:
    print(raiz +" no es raíz del polinomio")
"""
while True:
    for i in firstLine:
        print(i, end=" ")
    print("")
    for i in secondLine:
        print(i, end=" ")
    print("")
    for i in thirdLine:
        print(i, end=" ")
    print("")
    break
formatOutput(firstLine,coeficientes,0)
formatOutput(secondLine,secondLine,1)
formatOutput(tercerLinea, resultado,0)

print(firstLine)
print(secondLine)
print(tercerLinea)
    

#forms the polynomial 
def outputPolynomial(lIst):

    polyStr = ''
    for i in range(len(lIst),0,-1):
        

        if lIst[i-1] >=0:

            polyStr+= (str(lIst[i-1]) + "x^" + str(i-1))
            polyStr+= "+"
        else:
            polyStr+= (str(lIst[i-1]) + "x^" + str(i-1))
            polyStr+="-"



    return polyStr[:len(polyStr)-4]
polynomial = outputPolynomial(resultado)

#output
"""