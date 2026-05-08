'''palavra = "PARALELEPIPEDO"
#print(palavra[2]) # Imprime a letra "R"
#print(palavra[3:7])
#lista=["A", "B", "C", "D"]
#print(lista[2])

frutas = ["Laranja", "Maçã", "Goiaba", "Pera"]
frutas = frutas + ["Uva", "Abacaxi", "Morango", "Banana", "Kiwi"]

#print(frutas [3:6])

frutas[7] = "Banana da terra"
frutas.remove("Uva") #remove um item da lista

print(frutas)'''

numeros = [1, 2, 3, 4, 5]
#print(numeros)
#numeros[1] = numeros [3] + numeros [2] #operações com listas
print(numeros)
numeros.append(6) #adiciona um item no final da lista
print(numeros)
numeros.extend(["Laranja", "Maçã", "Uva"]) #adiciona uma lista dentro de outra lista
print(numeros)
numeros.insert(2, "Casa") #adiciona um item em uma posição específica da lista
print(numeros)