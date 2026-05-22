'''Controle de Hotel com tratamento de erro em python
O algoritmo deve cadastrar hóspede com: Nome, Idade, CPF, Tipo de Quarto e Quantidade de Diárias.
O algoritmo deve fazer a reserva de quartos, a quantidade de diárias, o valor da hospedagem e a disponibilidade
de quartos. Os valores dos quartos são: Standard = R$ 120,00; Luxo = R$ 250,00 e Premium = R$ 400,00.
Situação = Até R$ 500,00 de gastos = Hospedagem Econômica, de R$ 501,00 até R$ 1500,00 = Hospedagem
Intermediária e acima de R$ 1500,00 = Hospedagem Premium. Criar o código em python e usar tratamento de erros,
funções simples, listas e tuplas'''

TIPOS_QUARTO = ("Standard", "Luxo", "Premium")
PRECOS       = (120.00, 250.00, 400.00)

def cadastrar_hospede():
    hospede = {}
    try:
        hospede["nome"] = input("Digite o nome do hóspede: ")
        hospede["idade"] = int(input("Digite a idade do hóspede: "))
        hospede["cpf"] = int(input("Digite o CPF do hóspede: "))
        return hospede

    except:
        print("Erro nos dados digitados")

def menu():
    hospedes = []
    while True:
        print("----Menu----")
        print("1 - Cadastrar Hóspede")
        print("2 - Reservar um Quarto")
        print("3 - Sair")
        op = input("Escolha uma opção: ")
        

        if op == "1":
            hospede = cadastrar_hospede()
            hospedes.append(hospede) 

        elif op == "2":
            reservar_quartos(quartos)

        elif op == "3":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida")
        

def reservar_quartos(quartos):
    if len(quartos) == 0:
        print("Nenhum quarto reservado!")
    else:
        print("----Relatório----")
        for produto in produtos:
            print("________________________")
            print(f"Nome: {produto["nome"]}")          
            print(f"Categoria: {produto["categoria"]}")   
            print(f"Quantidade em Estoque: {produto["estoque"]}") 
            print(f"Preço: R$ {produto["preco"]:.2f}")  
            
            print("\nSituação do Estoque:")

            if produto["estoque"] > 10:       
                print("Estoque Bom!")
            elif produto["estoque"] >= 5:     
                print("Estoque Médio")
            else:
                print("Estoque Baixo")

menu()