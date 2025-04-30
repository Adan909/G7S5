print("Bienvenido al sistema de propina!")
Monto = int(input("Por favor, digite el monto a pagar: "))
num = int(input("Como considera que fue su servicio?\n1. Bueno\n2. Malo \n"))


if num == 1:
    propina = Monto * 0.15
    print(f"Su propina es de: {propina}")
elif num == 2:
    propina = Monto * 0.05
    print(f"Su propina es de: {propina}")
else: 
    print("Opcion no valida")
    


