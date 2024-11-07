def menu():
    print("Bienvenido a la calculadora, por favor seleccione la opción ")
    print("Opción 1: evaluación de raíz de un polinomio por división sintética")
    print("Opción 2: evaluación de un sistema de ecuaciones por Gauss-Jordan")
    print("Opción 3: operaciones con matrices")
    print("Opción 4: salir")

opciones = [1,2,3,4]
opcion = 0
def pedir_opcion():
    global opciones
    global opcion
    while True:
        try:
            opcion = int(input("Seleccione unaopcion: "))
            if opcion in opciones:
                break
            else:
                print("Opcion no valida")
        except:
            print("Opcion no valida")
while True:
    menu()
    pedir_opcion()
    if opcion ==1:
        exec(open("syntheticDiv.py").read())
    elif opcion == 2:
        exec(open("GaussJordan.py").read())
    elif opcion == 3:
        exec(open("AngelTocayoCode.py").read())
    else: 
        print("Gracias por usar la calculadora")
        break
    

