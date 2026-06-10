linhas = int(input("Digite quantas linhas a matriz terá: "))
colunas = int(input("Digite quantas colunas a matriz terá: "))

notas = []

for linha in range(linhas):
    linha_notas = []

    for coluna in range(colunas):
        valor = float(input("Digite as notas da matriz: "))

        linha_notas.append(valor)

maior = notas [0][0]
menor = notas [0][0]

for linha in range(len(notas)):
    for coluna in range(len(notas[linha])):
        if notas[linha][coluna] > maior:
            maior = notas[linha][coluna]

        if notas[linha][coluna] < menor:
            menor = notas[linha][coluna]

print("Maior número:", maior)
print("Menor número:", menor)

par = []
