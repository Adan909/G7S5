import datetime as dt

fecha_inicio_sesion = input("Fecha de ultimo inicio de sesion en formato YY-MM-DD: ")
fecha_inicio_sesion = dt.datetime.strptime(fecha_inicio_sesion, "%Y-%m-%d")

fecha_actual = dt.datetime.now()

print(fecha_inicio_sesion, fecha_actual)

contar_dias = (fecha_actual - fecha_inicio_sesion).days
if contar_dias > 30:
    print("Inactivo por mas de 30 dias")
else:
    print("Estamos bien")

