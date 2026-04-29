#Arvore de Decisão
print("## PROGRAMA DE EMPRÉSTIMO ##")
print("Responda: 0 para NÃO e 1 para SIM")

negativado = int(input("Você possui nome NEGATIVADO? "))
if negativado == 1:
    print("Empréstimo NEGADO")
else:
    clt = int(input("Você possui carteira assinada? "))
    if clt == 0:
        print("Empréstimo NEGADO")
    else:
        casa = int(input("Você possui casa própria? "))
        if casa == 0:
            print("Empréstimo NEGADO")
        else:
            print("Empréstimo APROVADO")