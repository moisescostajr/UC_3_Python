dados = [] # lista vazia
#nomes = {} # dicionario vazio
#nomes = () # tupla vazia

def cadastrar(nome, idade, sexo):
    dados.append([nome, idade, sexo])
    print("Cadastro realizado")
    
nome = input("Digite o nome ")
idade = int(input("Digite a idade "))
sexo = input("F - Feminino / M - Masculino ")
cadastrar(nome, idade, sexo)

