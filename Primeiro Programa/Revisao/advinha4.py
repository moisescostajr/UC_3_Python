numero_secreto = 42
total_de_tentativas = 3

while(total_de_tentativas > 0):
    chute = int(input('Digite um número: '))
    
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    
    if (acertou):
        print('Você acertou o numero!!!')
        break
    elif(maior):
        print("Voce Errou! O Numero que você digitou é MAIOR!")
    else:
        print("Voce Errou! O Numero que você digitou é MENOR!")
    
    total_de_tentativas = total_de_tentativas - 1