#### Função para validar se a entrada é um valor numerico #####
def inputNumber(message):

    while True:
        try:
            userinput = int(input(message))
        except ValueError:
            print("This is not a whole number.")
            
        else:
            return userinput
            break

###################################################################


#### Função para validar divisão por zero #####
def inputzero(message):

    while True:
        try:
            userinput = int(input(message))
        except ValueError:
            print("The number can not be zero.")
            
        else:
            return userinput
            break


###################################################################




############ Main Program ##########################################


while True:
    try:

        print("\n Programa de calculador simples\n")
        input_list = ["Soma [+]", "Subtração [-]", "Multiplicação [*]", "Divisao [/]"]
        valor = input("Select the input: " + ' '.join(input_list) + "\n")

        if (valor == "+") or (valor == "-") or (valor == "*") or (valor == "/") :

            x = inputNumber("Digite um valor para X: ")
            y = inputNumber("Digite um valor para Y: ")

            if valor == "+":  z = x + y
            elif valor =="-": z = x - y
            elif valor =="*": z = x * y
            
            elif valor =="/": 
                if y == 0:
                    print("Y can not be zero.")
                    exit()
                z = x / y


            print ("O valor de Z = "+str(z))
            
        else:
            print("Operação invalida.")
            exit()

    except KeyboardInterrupt:
        print ("\n\nClosed Program")
        exit()
