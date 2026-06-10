pessoas = []

for i in range(5):
    nome = input(f"Nome da pessoa {i+1}? ")
    idade = int(input(f"Idade de {nome}?"))
    pessoas.append([nome, idade])

menor = 0
for i in range(len(pessoas)):
    if pessoas[i][1] < pessoas[menor][1]:
        menor = 1

for pessoa in pessoas:
    print(pessoa)
print(f"A pessoa mais nova é {pessoas[menor][0]}")