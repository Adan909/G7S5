temp = int(input("Dime la temperatura del servidor (Celcius): "))
uso = int(input("Dime el uso del cpu (porcentaje): "))
if temp >80 or uso > 95:
    print("Iniciando protocolo de emergencia")
else:
    print("Todo en orden")