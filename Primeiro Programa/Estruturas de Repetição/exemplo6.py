pares = 0
impares = 0
for cont in range(5):
    numeros = int(input("Digite um número: "))
    if numeros % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
        
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")

