def mayor(n1,n2):
    
    if(n1>n2):
        print("El numero mayor es: ",n1)
    elif(n1<n2):
        print("El numero mayor es: ",n2)
    else:
        print("Hay algun error con tus números")

      
def menor(n1,n2):
    
    if(n1>n2):
        print("El numero menor es: ",n2)
    elif(n1<n2):
        print("El numero menor es: ",n1)
    else:
        print("Hay algun error con tus números")

def menu(funcion):
    if(funcion=='1'):
        print("-------MAYOR--------")
        n1=input("Ingrese el primer numero a comprar: ")
        n2=input("Ingrese el segundo numero a comprar: ")
        mayor(n1,n2)
    elif (funcion=='2'):    
        print("-------MENOR--------")    
        n1=input("Ingrese el primer numero a comprar: ")
        n2=input("Ingrese el segundo numero a comprar: ")
        menor(n1,n2)
    else:
        print("Algo hiciste mal")


print("MENU DE FUNCIONES")
print("1) Saber mayor")
print("2) Saber menor\n")
funcion=input("Ingrese lo que desea saber:\n")
menu(funcion)

