num = int(input("Dime el primer numero: "))
num2 = int(input("Dime el segundo numero: "))
op = int(input("Que operacion desea realizar?\n 1.Suma\n 2.Resta\n 3.Multiplicacion\n 4.Division\n"))
if op == 1:
    print(f"El resultado de tu suma es {num + num2}")
elif op == 2:
    print(f"El resultado de tu resta es {num - num2}")
elif op == 3:
    print(f"El resultado de tu multiplicacin es {num * num2}")
elif op == 4:
    print(f"El resultado de tu division es {num / num2}")
else:
    print("Error")