import math

print("-*" * 30)
print("Equação do 2º Grau")
print("ax² + bx + c = 0")
print("-*" * 30)

a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))

if a == 0:
    print("Erro: o valor de 'a' não pode ser zero, Neste caso, a equação não é do 2º grau ")
else:
    delta = b**2 - 4 * a * c

    print(f"\nDelta = {delta}")

    if delta < 0:
        print("\nNão existem raízes reais.")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"\nExiste uma raiz real (dupla):")
        print(f"  x = {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"\nExistem duas raízes reais:")
        print(f"  x1 = {x1}")
        print(f"  x2 = {x2}")