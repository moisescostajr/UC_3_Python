#Para percorrer matrizes, utilizar apenas o FOR:

matriz = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9]
]
for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        print(matriz[linha][coluna], end = "")
    print()
        
