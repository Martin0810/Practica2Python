def contar_digitos():
    try:
        numero_ingresado = int(input("Ingrese un número entero: "))

        digito_a_verificar = int(input("Ingrese un dígito: "))

        numero_str = str(numero_ingresado)

        cantidad = numero_str.count(str(digito_a_verificar))

        print(f"Cantidad de veces {digito_a_verificar} en el número {numero_ingresado}: {cantidad}")

    except ValueError:
        print("Error: Ingrese un número entero válido.")

contar_digitos()