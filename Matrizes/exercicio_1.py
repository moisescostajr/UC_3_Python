linhas = int(input("Digite a quantidade de linhas da matriz: "))
colunas = int(input("Digite a quantidade de colunas da matriz: "))

notas = []

for linha in range(linhas):
    linha_notas = []

    for coluna in range(colunas):
        valor = float(input(f"Digite as notas da matriz: "))
        linha_notas.append(valor)

    notas.append(linha_notas)

maior = notas[0][0]
menor = notas[0][0]
pares = []

for linha in range(len(notas)):
    for coluna in range(len(notas[linha])):
        valor = notas[linha][coluna]

        if valor > maior:
            maior = valor

        if valor < menor:
            menor = valor

        if valor % 2 == 0:
            pares.append(valor)

print("\nMatriz Completa")
for linha in notas:
    print(linha)

print("\nMaior número da matriz:", maior)
print("Menor númeroda matriz:", menor)

print("Todos os números pares:")
for numero in pares:
    print(numero)