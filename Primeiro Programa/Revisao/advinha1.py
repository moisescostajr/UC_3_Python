numero_secreto = 42
chute = int(input('Digite um número: '))

if (chute == numero_secreto):
    print('Você acertou o numero!!!')
else:
    if(chute > numero_secreto):
        print("Você errou! O seu chute foi maior que o numero secreto.")
    else:
        print("Você errou! O seu chute foi menor que o numero secreto.")