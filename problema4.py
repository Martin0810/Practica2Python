num_alumnos = int(input("Ingrese el número de alumnos: "))
lista_alumnos = []

for i in range(num_alumnos):
    alumno = input("Ingrese el nombre del alumno: ")
    notas = []

    for j in range(3):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {j + 1} para {alumno}: "))
                notas.append(nota)
                break
            except ValueError:
                print("Error: Por favor, ingrese una nota válida.")

    alumno_info = {"Alumno": alumno, "Notas": notas}
    lista_alumnos.append(alumno_info)

print("\nListado completo de alumnos:")
for alumno in lista_alumnos:
    print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")