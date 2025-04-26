lado1= int(input("Escribe el lado 1 del triángulo: "))
lado2= int(input("Escribe el lado 2 del triángulo: "))
lado3= int(input("Escribe el lado 3 del triángulo: "))
if lado1 == lado2 and lado2 == lado3 and lado1 == lado3:
    print("El triángulo es equilátero")
elif lado1 == lado2 and lado1 != lado3 or lado2 == lado3 and lado2 != lado1 or lado1 == lado3 and lado1 != lado2:
    print("El triángulo es isósceles")
elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print("El triángulo es escaleno")
else:
    print("Error en la comparación de lados")
