def omitir_vocales(cadena):
    cadena_sin_vocales = cadena.replace('a', '').replace('A', '').replace('e', '').replace('E', '').replace('i', '').replace('I', '').replace('o', '').replace('O', '').replace('u', '').replace('U', '')
    return cadena_sin_vocales

texto_ingresado = input("Ingrese una cadena de texto: ")

resultado = omitir_vocales(texto_ingresado)

print("Texto original:", texto_ingresado)
print("Texto sin vocales:", resultado)