numeros = []  

while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ").upper()

    if respuesta == "SI":
        try:
            numero = int(input("Ingrese el número: "))
            numeros.append(numero)
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")
    elif respuesta == "NO":
        break
    else:
        print("Respuesta no válida. Por favor, ingrese SI o NO.")

print("Números ingresados:", numeros)

numeros_pares = sum(1 for num in numeros if num % 2 == 0)
numeros_impares = len(numeros) - numeros_pares

print("Cantidad de números pares:", numeros_pares)
print("Cantidad de números impares:", numeros_impares)

