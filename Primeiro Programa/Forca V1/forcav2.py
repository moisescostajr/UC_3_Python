print("*"*20)
print("*"*5, "Bem Vindo ao Jogo da Forca", "*"*5)
print("*"*20)

palavra_secreta = "banana"

acertou = False
enforcou = False

while (not acertou and not enforcou):
    chute = input("Qual a letra? \n")
    
    posicao = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            print("Encontrei a letra {} na posição {}".format(letra, posicao))
        
        posicao = posicao + 1
    
print("Fim do Jogo")