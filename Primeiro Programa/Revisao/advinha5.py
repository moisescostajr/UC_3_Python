numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
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
    
    rodada = rodada + 1

print("FIM DE JOGO")