matriz = [ 
    [1, 2, 3], # linha 0
    [4, 5, 6], # linha 1
    [7, 8, 9]  # linha 2
]

print(matriz)
print(matriz[2][1]) #primeiro colchete é referente a linha e o segundo é da coluna da matriz

matriz2 = [ 
    [1, 2, 3], # linha 0
    [4, 5, 6], # linha 1
]

linhas = len(matriz2) # contar quantas linhas há na matriz
colunas = len(matriz2[0]) # para contar quantas colunas, iniciar com o [0]

print(linhas)
print(colunas)