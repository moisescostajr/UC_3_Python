abrindo_arquivo = open("C:/Users/corin/OneDrive - Senac MS Edu/Documents/primeiro_arquivo.txt", "w")
abrindo_arquivo.write("Escrevendo meu primeiro arquivo")
abrindo_arquivo.close()

abrindo_arquivo = open("C:/Users/corin/OneDrive - Senac MS Edu/Documents/primeiro_arquivo.txt", "r")
print(abrindo_arquivo.readlines())
abrindo_arquivo.close()

