import random

print("--" * 30)
print("SISTEMA DE SORTEIO DE NOMES")
print("--" * 30)

nomes = []
while True:
    nome = input("Digite um nome: ")
    nomes.append(nome)
    
    op = input("Deseja continuar [S][N]? ")
    if op.upper() == "N":
        break

random.shuffle(nomes)
print(f"Ordem embaralhada: {nomes}")

sorteio = random.choice(nomes)
print(f"O nome sorteado foi: {sorteio}")

op2 = input(f"Deseja fazer um novo sorteio [S][N]? ")
if op2.upper() == "S":
    
    nomes.remove(sorteio)
    if len(nomes) > 0:
        
        sorteio2 = random.choice(nomes)
        print(f"O segundo nome sorteado foi: {sorteio2}")
