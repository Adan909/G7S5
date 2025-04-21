rango_inicial = int(input("Escribe el inicio del rango: "))
rango_final = int(input("Escribe el fin del rango: "))


if (rango_inicial < rango_final):
    numero = int(input("Dime un numero: "))
    if(numero >= rango_inicial and numero <= rango_final):
        print("El numero está dentro del rango")
    else:
        print("El numero está fuera del rango")
else:
    print("El rango final no puede ser menor que el inicial")