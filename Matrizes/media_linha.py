notas = [
    [5.0, 4.5, 7.0, 5.2, 6.1],
    [2.1, 6.5, 8.0, 7.0, 6.7],
    [8.6, 7.0, 9.1, 8.7, 9.3]
]

for linha in range(len(notas)):
    soma = 0

    for coluna in range(len(notas[linha])):
        soma = soma + notas[linha][coluna]

    media = soma / len(notas[linha])
    print(f"Média da linha {linha}: {media:.2f}")
