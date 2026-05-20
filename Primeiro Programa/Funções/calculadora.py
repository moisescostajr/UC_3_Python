def soma(a, b):
    soma = a + b
    return soma
def subtracao(a, b):
    soma = a - b
    return subtracao
def multiplicacao(a, b):
    soma = a * b
    return multiplicacao
def divisao(a, b):
    soma = a / b
    return divisao

def menu():
    print("Calculadora")
    print("1 - Soma ")
    print("2 - Subtração ")
    print("3 - Multiplicação ")
    print("4 - Divisão ")
    op = int(input("Informe a operação "))
    a = float(input("Informe a 1º Numero "))
    b = float(input("Informe o 2º Numero "))
    
    if op == 1:
        print(soma(a, b))
    elif op == 2:
        print(subtracao(a, b))
    elif op == 3:
        print(multiplicacao(a, b))
    elif op == 4:
        print(divisao(a, b))
    else:
        print("Opção Inválida")
    
menu()
    