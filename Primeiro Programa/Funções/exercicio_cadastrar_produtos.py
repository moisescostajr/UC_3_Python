def cadastrar_produto():
    produto = {}
    produto["nome"] = input("Digite o nome do produto: ")
    produto["categoria"] = input("Digite a categoria do produto: ")
    produto["estoque"] = int(input("Digite a quantidade do estoque: "))
    produto["preco"] = float(input("Digite o preço do produto: "))
    return produto 

def menu():
    produtos = []
    while True:
        print("----Menu----")
        print("1 - Cadastrar Produto")
        print("2 - Gerar Relatório")
        print("3 - Sair")
        op = input("Escolha uma opção: ")

        if op == "1":
            qtd_produtos = int(input("Quantos produtos você deseja cadastrar?: "))
            for _ in range(qtd_produtos):
                produto = cadastrar_produto()
                produtos.append(produto) 

        elif op == "2":
            mostrar_relatorio(produtos)

        elif op == "3":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida")

def mostrar_relatorio(produtos):
    if len(produtos) == 0:
        print("Nenhum produto cadastrado")
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