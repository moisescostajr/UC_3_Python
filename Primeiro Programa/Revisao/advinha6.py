numero_secreto = 42
total_de_tentativas = 3

for tentativa in range(1, total_de_tentativas + 1):
    print('Tentativa {} de {}'.format(tentativa, total_de_tentativas))
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
    
print("FIM DE JOGO")