cargos = {
    1: ("Programador de Sistemas", 0.30),
    2: ("Analista de Sistemas", 0.20),
    3: ("Analista de Banco de Dados", 0.15)
}

for numero, (cargo, aumento) in cargos.items():
    print(f"{numero} - {cargo} ({int(aumento * 100)}% de aumento)")

opcao = int(input("Escolha o cargo (1, 2 ou 3): "))

if opcao in cargos:
    cargo, aumento = cargos[opcao]
    salario = float(input(f"Digite o salário do funcionário ({cargo}): R$ "))
    novo_salario = salario * (1 + aumento)
    print(f"Aumento: {int(aumento * 100)}%")
    print(f"Novo salário: R$ {novo_salario:.2f}")
else:
    print("Cargo Inválido")