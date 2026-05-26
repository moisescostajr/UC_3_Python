print("*"*20)
print("*"*5, "Bem Vindo ao Jogo da Forca", "*"*5)
print("*"*20)

palavra_secreta = "banana"
letras_acertadas = ["_","_","_","_","_","_"]

acertou = False
enforcou = False

while (not acertou and not enforcou):
    chute = input("Qual a letra? \n")
    
    posicao = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            #print("Encontrei a letra {} na posição {}".format(letra, posicao))
            letras_acertadas[posicao] = letra
        
        posicao = posicao + 1

    print(letras_acertadas)
        
print("Fim do Jogo")