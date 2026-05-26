numero_secreto = 42
chute = int(input('Digite um número: '))

if (chute == numero_secreto):
    print('Você acertou o numero!!!')
elif(chute > numero_secreto):
    print("Voce Errou! O Numero que você digitou é MAIOR!")
else:
    print("Voce Errou! O Numero que você digitou é MENOR!")