#Esta funcion te dice si el numero que ingresa el usuario es par o impar.
def parImpar():
    num= int(input("Escribe un numero: "))

    if num %2 == 0:
        print("El numero {num} es par".format(num=num))
    else:
        print("El numero {num} es impar".format(num=num))