#Estrutura IF,  ELSE, ELIF
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 6:
    print("Aprovado com média: ", media)
elif media >= 3 and media <= 5.9:
    print("Recuperação com média: ", media)
else:
    print("Reprovado com média: ", media)