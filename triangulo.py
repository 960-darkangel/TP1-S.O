def tipo_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or b == c or a == c:
        return "Isósceles"
    else:
        return "Escaleno"

try:
    a = float(input("Lado A: "))
    b = float(input("Lado B: "))
    c = float(input("Lado C: "))

    if a + b > c and a + c > b and b + c > a:
        print("Tipo de triángulo:", tipo_triangulo(a, b, c))
    else:
        print("No es un triángulo válido.")
except ValueError:
    print("Por favor, ingrese solo números.")
