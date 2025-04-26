#Calificación cualitativa
#Solicita una calificación numérica entre 0 y 100 y muestra si es "Reprobado", "Regular", "Bueno", "Muy bueno" o "Excelente".
calificacion = int(input("Escribe tu calificación: "))
if calificacion >= 0 and calificacion < 60:
    print("Reprobado")
elif calificacion >= 60 and calificacion <= 70:
    print("Regular")
elif calificacion >= 71 and calificacion <= 85: 
    print("Bueno")
elif calificacion >= 86 and calificacion <= 95:
    print("Muy bueno")
elif calificacion >= 96 and calificacion <= 100:
    print("Excelente")
else:
    print("Calificación inválida")