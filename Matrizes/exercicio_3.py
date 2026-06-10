notas = [[5.9, 4.5, 7.0, 5.2, 6.1],
          [2.1, 6.5, 5.0, 7.0, 6.7],
          [8.6, 7.0, 9.1, 8.7, 9.3]]

cont = soma = 0

for linhas in range(len(notas)):
    for colunas in range(len(notas[linhas])):
        soma = soma + notas[linhas][colunas]
        cont = cont + 1
media = soma / cont
print(f"{media:.2f}")