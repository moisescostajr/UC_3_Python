'''Elabore um algoritmo para diagnosticar gripe comum.
Use os seguintes fatores:
Sintomas: febre moderada, nariz entopido, dor de garganta, tosse.
Duração dos sintomas: Menor que 7 dias, maior de 7 dias.
Classificação: Provável gripe comum ou sintomas atípicos, investigar outras condições.'''

print("-" * 28)
print (" Diagnóstico de Gripe Comum")
print("-" * 28)

print("Você apresenta o seguinte sintoma: Febre Moderada?")
sintoma_1 = input("Responda Sim ou Não: ")
print("Você apresenta o seguinte sintoma: Nariz Entupido?")
sintoma_2 = input("Responda Sim ou Não: ")
print("Você apresenta o seguinte sintoma: Dor de Garganta?")
sintoma_3 = input("Responda Sim ou Não: ")
print("Você apresenta o seguinte sintoma: Tosse?")
sintoma_4 = input("Responda Sim ou Não: ")
print("A duração dos sintomas é maior que 7 dias?")
duracao = input("Responda Sim ou Não: ")

if sintoma_1 == "Sim" and sintoma_2 == "Sim" and sintoma_3 == "Sim" and sintoma_4 == "Sim" and duracao == "Sim":
    print("Provável gripe comum.")
else:
    print("Sintomas atípicos, investigar outras condições.")
    
