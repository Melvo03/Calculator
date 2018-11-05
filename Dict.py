print ("Bienvenido a mi calculadora")
option = True
while(option):
    print("Que tipo de operacion le gustaria hacer")
    print("a.Suma\nb.Resta\nc.Multiplicacion\nd.Division")

    typeofsum= input()
    if typeofsum=="a":

        number1= int(input("Por Favor ingrese el primer numero\n"))      
        number2= int(input("Por Favor ingrese el segundo numero\n"))
        print(number1 + number2)

    elif typeofsum=="b":
        number1= int(input("Por Favor ingrese el primer numero\n"))
        number2= int(input("Por Favor ingrese el segundo numero\n"))
        print(number1 - number2 )

    elif typeofsum=="c":
        number1= int(input("Por Favor ingrese el primer numero\n"))
        number2= int(input("Por Favor ingrese el segundo numero\n"))
        print(number1 * number2 )

    elif typeofsum=="d":
        number1= int(input("Por Favor ingrese el primer numero\n"))
        number2= int(input("Por Favor ingrese el segundo numero\n"))
        print(number1 / number2 )

    else:
        print("Seleccion Incorrect")
        print ("Le gustaria realizar otra operacion? (S/N)")
    opcion = True if input() == 's' or input() == 'S' else False
quit()

          
    
    
