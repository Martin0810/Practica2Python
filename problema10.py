nombres_meses = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

def convertir_fecha(fecha):
    partes_fecha = fecha.split()

    if len(partes_fecha) == 3:
        mes = partes_fecha[0]
        dia = partes_fecha[1].replace(',', '')
        año = partes_fecha[2]
    else:
        mes, dia, año = fecha.split('/')

    num_mes = nombres_meses.index(mes) + 1

    fecha_formateada = f"{año}-{num_mes:02d}-{int(dia):02d}"

    return fecha_formateada

fecha_ingresada = input("Ingrese una fecha en formato mes-día-año: ")

fecha_formateada = convertir_fecha(fecha_ingresada)

print("Fecha ingresada:", fecha_ingresada)
print("Fecha formateada:", fecha_formateada)