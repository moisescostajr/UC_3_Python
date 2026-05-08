salario = float(input("Digite o seu salário: R$ "))

print("-*" * 20)
print("1 - Programador de Sistemas (30% de aumento)")
print("2 - Analista de Sistemas (20% de aumento)")
print("3 - analista de Banco de Dados (15% de aumento)")
print("-*" * 20)

cargo = int(input("Digite o número do seu cargo: "))
if cargo < 1 or cargo >3:
    print("Cargo Inválido")
    exit()
    
elif cargo == 1:
    salario = salario * 1.30
    print("Aumento de 30%")
elif cargo == 2:
    salario = salario * 1.20
    print("Aumento de 20%")
elif cargo == 3:
    salario = salario * 1.15
    print("Aumento de 15%")
    
print(f"Novo salário de R$: {salario:.2f}")

