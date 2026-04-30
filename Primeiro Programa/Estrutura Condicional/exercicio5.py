nome = input("Digite o seu nome: ")
if len(nome) > 10: #len retorna o tamanho da string
    print("O seu nome possui mais de 10 caracteres")
else:
    print("O seu nome possui", len(nome), "caracteres")