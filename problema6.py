def fibonacci_hasta_limite(limite):
    serie = []
    num1, num2 = 0, 1

    while num1 <= limite:
        serie.append(num1)
        num1, num2 = num2, num1 + num2

    return serie

limite = 50

serie_fibonacci = fibonacci_hasta_limite(limite)

print("Serie de Fibonacci hasta", limite, ":", serie_fibonacci)