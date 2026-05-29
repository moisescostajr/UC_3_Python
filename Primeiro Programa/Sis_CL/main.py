perfis_permitidos = ("Aluno", "Professor", "Técnico")
usuarios = []
def salvar_usuario_arquivo(usuario):
    try:
        arquivo = open("C:/Users/corin/OneDrive - Senac MS Edu/Documents/cadastro_usuario.txt", "w", encoding="utf-8")
        arquivo.write(
            usuario["nome"] + ";" +
            usuario["login"] + ";" +
            usuario["senha"] + ";" +
            usuario["perfil"]+ "\n"
        )        
        arquivo.close()
    except:
        print("Erro ao salvar os dados do usuário no arquivo")
    finally:
        print("Dados salvos com sucesso!")
        
def fazer_login():
    login = input("Informe seu login: ")
    senha = input("Informe sua senha: ")
    for usuario in usuarios:
        if usuario["login"] == login and usuario["senha"] == senha:
            print("Login Realizado com sucesso!")
            return usuario
        print("Login e Senha incorreta!")
        
def cadastrar_usuario():
    usuario = {}
    usuario["nome"] = input("Digite o nome completo: ")
    usuario["login"] = input("Digite o seu login: ")
    usuario["senha"] = input("Digite a sua senha: ")
    print("Perfis permitidos")
    for perfil in perfis_permitidos:
        print("-", perfil)
    usuario["perfil"] = input("Digite o perfil: ")
    if usuario["perfil"] not in perfis_permitidos:
        print("Perfil Inválido")
        return
    for i in usuarios:
        if i["login"] == usuario["login"]:
            print("Esse login já existe!")
            return
    usuarios.append(usuario)
    salvar_usuario_arquivo(usuario)
    print("Usuário cadastrado com sucesso!")

def menu_sistema():
    
    while True:
        
        print("Menu Sistema")
        print("1 - Registrar Chamado")
        print("2 - Listar Chamados")
        print("3 - Sair")
    
        opcao = input("Escolha uma opção")
    
        if opcao == 1:
            print("opção 1")
        if opcao == 2:
            print("opção 2")
        if opcao == 3:
            print("Saindo da conta!")
        
            break
        else:
            print("Opção inválida")
    
def menu_principal():
    while True:
        print("SISTEMA DE CHAMADOS ESCOLAR")
        print("1 - Cadastrar Usuários")
        print("2 - Fazer Login")
        print("3 - Listar Usuários Cadastrados")
        print("4 - Sair")
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números")
            continue
        finally:
            print("Opção tratada com sucesso!")
        if opcao == 1:
            cadastrar_usuario()
        elif opcao == 2:
            usuario_logado = fazer_login()
        elif opcao == 3:
            print("opção 3")
        elif opcao == 4:
            print("Sair")
            break
        else:
            print("opção inválida")
menu_principal()
            
