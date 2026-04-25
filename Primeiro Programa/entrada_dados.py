#Exemplo de Dados e Conversão de tipos de Dados
nome = input("Digite o seu nome:")
print("O seu nome é:", nome)
print(type(nome))
idade = int(input("Digite a sua idade:")) #Aqui ele converte a string digitada para um numero inteiro
print("A sua idade é:", idade)
print(type(idade))

base = float(input("Digite o valor da base:"))
altura = float(input("Digite o valor da altura:"))
area = base * altura
print("A área do retangulo é:", area)

