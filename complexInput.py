def get_Input ( inputStr):
    complexInput =""
    complexInputList=[]
    imaginaryElements = []
    realElements = []
    allowedCharacters = ["0","1","2","3","4","5","6","7","8","9",".","i", "+", "-","/"]
    imaginary =0 
    real = 0
    diagonal ="/"
    space = " "
    complexNumber = complex(0,0)
    while True:
        try:
            complexInput = input( inputStr)
            complexInputList = list(complexInput)
            #checks for spaces
            if space in complexInputList:
                print("Por favor no introduzca espacios")
                raise Exception

            #checks for multiple operators
            if len(complexInputList)>1:
                complexInputList = complexInputList[1:]
                if (complexInputList.count("+")+complexInputList.count("-"))>1 :
                    print("Por favor no introduzca mas de dos operadores")
                    raise Exception
                complexInputList = list(complexInput)
            #checking for unallowed characters
            for character in complexInputList:
                if character not in allowedCharacters:
                    print("Favor de solo introducir carácteres permitidos :0,1,2,3,4,5,6,7,8,9,.,+,-,i,/") 
                    raise Exception
            #checks for more than one decimal point, diagonal or i
            if complexInputList.count(".")>2 or complexInputList.count("i")>1 or complexInputList.count("/")>2:
                print("Por favor no introduzca dos puntos , i o diagonales")
                raise Exception   
            complexInputList = list(complexInput)
            #adding plus sign for proper distinction between real and imaginary 
            if complexInputList[0] != '-' and complexInputList[0] != '+':
                complexInputList.insert(0,'+')
    #testing for right plus addition
            #print("complexInputList with added plus:",complexInputList)
            #separating for complex numbers with both parts
            if (complexInputList.count("+") + complexInputList.count("-")) > 1:
                for index in range(1,len(complexInputList)):
                    if complexInputList[index] == "+" or complexInputList[index] == "-":
                        break
                realElements = complexInputList[:index]
                imaginaryElements = complexInputList[index:]
            else:
                if "i" in complexInputList:
                    imaginaryElements = complexInputList
                    realElements = []
                    realElements.append('0')
                else:
                    realElements = complexInputList  
                    imaginaryElements = []
                    imaginaryElements.append('0')
            if len(imaginaryElements)>1 and 'i' not in imaginaryElements:
                print("Por favor introduzca i para la parte imaginaria")
                raise Exception
    #Testing for both list parts of a complex number
            #print("real elements:", realElements, "imaginary elements:", imaginaryElements)
            #deals with unexistant 1 coeficient in imaginary elements
            if len(imaginaryElements) >1 and imaginaryElements[1] == 'i':
                imaginaryElements.insert(1,'1')
    #tests proper imaginary element separation
                #print(imaginaryElements)
            #checks for i and removes it for correct float conversion
            if len(imaginaryElements) >1:
                if 'i' in imaginaryElements:
                    imaginaryElements.pop()
                else:
                    print("Por favor introduzca i para la parte imaginaria")
                    raise Exception
            if realElements[0] == '+':
                realElements.pop(0)
    #testing the real elements and imaginary elements
            #print("newReal elements", realElements,"newImaginary elements", imaginaryElements)
            #checks for fractions
            if diagonal in realElements:
                realNum = "".join(realElements[0:realElements.index("/")])
                realDen = "".join(realElements[realElements.index("/")+1:])
                real = float(realNum)/float(realDen)
            else:
                real = (float("".join(realElements)))
            #checks for fractions
            if diagonal in imaginaryElements :
                imagNum = "".join(imaginaryElements[0:imaginaryElements.index("/")])
                imagDen = "".join(imaginaryElements[imaginaryElements.index("/")+1:])
                imaginary = float(imagNum)/float(imagDen)
            else:

                imaginary = float("".join(imaginaryElements))
    #testing for proper fraction conversion
            #print("real", real, "imaginary", imaginary)
            complexNumber = complex(real,imaginary)
    #testing for proper complex generation
            #print(complexNumber)
            return complexNumber
            
            break
        except :
            print("Por favor revise su entrada")

#get_Input()

