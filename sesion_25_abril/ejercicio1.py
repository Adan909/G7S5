edad = int(input("Escribe tu edad: "))
if edad >= 0 and edad <= 11:
    print("Eres un niño")
elif edad >= 12 and edad < 18:
    print("Eres un adolescente")
elif edad >= 18 and edad <= 65:
    print("Eres un adulto")
elif edad > 65 and edad <= 130:
    print("Eres un adulto mayor")
else:
    print("Edad invalida")