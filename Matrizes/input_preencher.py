#Preencher matriz com input

matriz = []
for linha in range(3):
    nova = []
    for coluna in range(3):
        valor = float(input("nota: "))
        nova.append(valor)

    matriz.append(nova)
print(matriz)
