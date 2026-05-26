print("-"*10, ' ADVINHAR NUMERO ', '-'*10)
print("Escolha o Nivel do jogo. \n 1 - Nivel 1 \n 2 - Nivel 2 \n 3 - Nivel 3")
total_de_tentativas = int(input("Digite o nivel de dificuldade:\n"))

if (total_de_tentativas == 1):
    total_de_tentativas = 10
elif (total_de_tentativas == 2):
    total_de_tentativas = 5
else:
    total_de_tentativas = 3
    
numero_secreto = 42
pontuacao = 100

for tentativa in range(1, total_de_tentativas + 1):
    print('Tentativa {} de {}'.format(tentativa, total_de_tentativas))
    print(f'Seus Pontos: {pontuacao}')
    chute = int(input('Digite um número: '))
    
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    
    if (acertou):
        print('Você acertou o numero!!!')
        break
    elif(maior):
        print("Voce Errou! O Numero que você digitou é MAIOR!")
        pontuacao -= 10
    else:
        print("Voce Errou! O Numero que você digitou é MENOR!")
        pontuacao -= 10
    
print("FIM DE JOGO")