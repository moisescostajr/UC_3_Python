notas = [
    [5.0, 4.5, 7.0, 5.2, 6.1],
    [2.1, 6.5, 8.0, 7.0, 6.7],
    [8.6, 7.0, 9.1, 8.7, 9.3]
]

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


"""
maior = max(max(linha) for linha in notas)
menor = min(min(linha) for linha in notas)

print("Maior número:", maior)
print("Menor número:", menor)
"""