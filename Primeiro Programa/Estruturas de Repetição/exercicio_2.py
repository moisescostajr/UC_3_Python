'''CONSTRUA UM ALGORITMO QUE RECEBA O NOME E O PREÇO DE 5 MEDICAMENTOS DE UMA DROGARIA.
O PROGRAMA DEVE IMPRIMIR O NOME E PREÇO DO MEDICAMENTO MAIS BARATO, BEM COMO A MÉDIA ARITMÉTICA DOS PREÇOS 
INFORMADOS'''

'''medicamento_mais_barato = 0
preco_medicamento_mais_barato = 0
soma_preco_medicamentos = 0

for cont in range(5):
    nome_medicamento = input("Informe o nome do medicamento: ")
    preco_medicamento = int(input("Informe o preço do medicamento: "))
    soma_preco_medicamentos = soma_preco_medicamentos + preco_medicamento
    
    if cont == 0:
        medicamento_mais_barato = nome_medicamento
        preco_medicamento_mais_barato = preco_medicamento
    else:
        if preco_medicamento < preco_medicamento_mais_barato:
            medicamento_mais_barato = nome_medicamento
            preco_medicamento_mais_barato = preco_medicamento
            
media_preco_medicamentos = soma_preco_medicamentos / 5

print(f"O medicamento mais barato é: {medicamento_mais_barato} e custa: R$ {preco_medicamento_mais_barato}")
print(f"A média aritmética dos preços dos medicamentos é: R$ {media_preco_medicamentos:.2f}")'''


print(f"Medicamento 1")
nome_barato = input("Nome : ")
preco_barato = float(input("Preço: R$ "))  #20
total = preco_barato #20
print(total, preco_barato)

for cont in range(2,6):
    print(f"Medicamento {cont}")
    nome  = input("Nome: ")
    preco = float(input("Preço: R$ ")) #10
    print(preco)
    print(total)
    total = total + preco #30
    print(total)

    menor = int(preco < preco_barato)
    print(menor)

    preco_barato = preco_barato * (1 - menor) + preco * menor 
    print(preco_barato)   
    nome_barato = nome_barato * (1 - menor) + nome * menor   
    
media = total / 5

print(f"Média dos preços dos 5 medicamentos: R$ {media}")
print(f"Medicamento mais barato: {nome_barato} com o preço de R$ {preco_barato}")

