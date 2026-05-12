'''Uma transportadora deseja calcular a prioridade de entrega. Receba os dados, distancia da entreha, se é urgente ou não.
Classificação: Urgente -> entrega prioritária;
Distancia acima de 300km -> entrega longa e
Distancia abaixo de 300km -> entrega padrão.'''

print("-" * 34)
print(" Sistema de Prioridade de Entrega")
print("-" * 34)

distancia = float(input("Informe a distancia da entrega em km: \n"))
urgente = input("A sua entrega é URGENTE? Responda Sim ou Não: ")
if urgente == "Sim":
    print("Entrega Prioritária")
elif distancia > 300:
    print("Entrega Longa")
else:
    print("Entrega Padrão")
    
    
      