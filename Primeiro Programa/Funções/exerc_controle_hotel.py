TIPOS_QUARTO = ("Standard", "Luxo", "Premium")
PRECOS = (120.00, 250.00, 400.00)

def cadastrar_hospede():
    try:    
        hospede = {}

        hospede["nome"] = input("Digite o Nome do hóspede: ")
        hospede["idade"] = int(input("Digite a Idade do Hóspede: "))
        hospede["cpf"] = int(input("Digite o CPF do Hóspede com apenas 11 dígitos: "))
        
        if len(str(hospede["cpf"])) <10 or len(str(hospede["cpf"])) > 11:
            print("Erro no CPF Informado")
            return
    
        
        print("\nTipos de quarto:")
        print(f"1 - Standard  R$ {PRECOS[0]:.2f}/diária")
        print(f"2 - Luxo      R$ {PRECOS[1]:.2f}/diária")
        print(f"3 - Premium   R$ {PRECOS[2]:.2f}/diária")

        op = int(input("Escolha o tipo (1, 2 ou 3): "))
        indice = op - 1

        hospede["tipo_quarto"] = TIPOS_QUARTO[indice]
        hospede["preco_diaria"] = PRECOS[indice]
        hospede["diarias"] = int(input("De quantas diárias você precisa? "))
        hospede["valor_total"] = hospede["preco_diaria"] * hospede["diarias"]

        if hospede["valor_total"] <= 500.00:
            hospede["classificacao"] = "Hospedagem Econômica"
        elif hospede["valor_total"] <= 1500.00:
            hospede["classificacao"] = "Hospedagem Intermediária"
        else:
            hospede["classificacao"] = "Hospedagem Premium"

        return hospede

    except (TypeError, ValueError):
        print("Erro nos dados")


def mostrar_relatorio(hospedes):
    if len(hospedes) == 0:
        print("Nenhum hóspede cadastrado.")
    else:
        print("---- Relatório ----")
        for hospede in hospedes:
            print("________________________")
            print(f"Nome          : {hospede["nome"]}")
            print(f"Idade         : {hospede["idade"]} anos")
            print(f"CPF           : {hospede["cpf"]}")
            print(f"Tipo de Quarto: {hospede["tipo_quarto"]}")
            print(f"Diárias       : {hospede["diarias"]}")
            print(f"Valor Total   : R$ {hospede["valor_total"]:.2f}")
            print(f"Situação      : {hospede["classificacao"]}")


def menu():
    hospedes = []

    while True:
        print("\n---- Menu ----")
        print("1 - Cadastrar Hóspede")
        print("2 - Gerar Relatório")
        print("3 - Sair")
        op = input("Escolha uma opção: ")

        if op == "1":
            qtd = int(input("Quantos hóspedes deseja cadastrar? "))
            for _ in range(qtd):
                hospede = cadastrar_hospede()
                hospedes.append(hospede)
                print(f"Hóspede {hospede["nome"]} cadastrado com sucesso!")

        elif op == "2":
            mostrar_relatorio(hospedes)

        elif op == "3":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida!")


menu()