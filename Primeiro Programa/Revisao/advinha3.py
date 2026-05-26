numero_secreto = 42
chute = int(input('Digite um número: '))

acertou = chute == numero_secreto
maior = chute > numero_secreto

if (acertou):
    print('Você acertou o numero!!!')
elif(maior):
    print("Voce Errou! O Numero que você digitou é MAIOR!")
else:
    print("Voce Errou! O Numero que você digitou é MENOR!")