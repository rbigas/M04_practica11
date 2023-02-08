#Esta funcion pide al usuario que inserte 2 numeros y el programa te dira el mas grande.
def numMayor():
    a = input("Escribe el primer numero: ")
    b = input("Escribe el segundo numero: ")
    if(a > b):
        print("El numero {a} es mayor que el numero {b}.".format(a=a,b=b))
    elif(b > a):
        print("El numero {b} es mayor que el numero {a}.".format(a=a,b=b))