perfis_permitidos = ("Aluno", "Professor", "Técnico")
tipos_problemas = ("Internet", "Computador", "Projetor", "Teclado", "Mouse")
usuarios = []
chamados = []
def salvar_usuario_arquivo(usuario):
    try:
        arquivo = open("C:/Users/corin/OneDrive - Senac MS Edu/Documents/cadastro_usuario.txt", "a", encoding="utf-8")
        arquivo.write(
            
            usuario["nome"] + ";" +
            usuario["login"] + ";" +
            usuario["senha"] + ";" +
            usuario["perfil"] + "\n"
        )                
        arquivo.close()        
    except:        
        print("Erro ao salvar os dados do usuário no arquivo")       
    finally:     
        print("Dados salvos com sucesso!")
        
def salvar_arquivo_chamado(chamado):  
    try:        
        arquivo_chamado = open("C:/Users/corin/OneDrive - Senac MS Edu/Documents/chamados.txt", "a", encoding="utf-8") 
        arquivo_chamado.write(
            
            chamado["nome"] + ";" +
            chamado["problema"] + ";" +
            chamado["descricao"] + ";" +
            chamado["status"] + "\n"            
        )
        arquivo_chamado.close()
        print("Chamado salvo com sucesso!")
    except:
        
        print("Erro ao registrar chamado no arquivo")
        
def fazer_login():   
    login = input("Informe seu login: ")   
    senha = input("Informe sua senha: ")   
    for usuario in usuarios:
        
        if usuario["login"] == login and usuario["senha"] == senha:
            
            print("Login Realizado com sucesso!")
            
            return usuario
        
    print("Login e Senha incorreta!")               
    return None
    
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

def registrar_chamados(usuario_logado):   
    chamado = {}   
    chamado["usuario"] = usuario_logado["nome"]  
    print("Tipos de problema")   
    for problema in tipos_problemas:      
        print("-", problema)
        
    chamado["problema"] = input("Digite o tipo de problema: ")  
    if chamado["problema"] not in tipos_problemas:     
        print("Tipo de problema inválido")     
        return   
    
    chamado["descricao"] = input("Descreva o problema: ")   
    chamado["status"] = "aberto"  
    chamados.append(chamado) 
    salvar_arquivo_chamado(chamado)   
    print("Chamado registrado com sucesso!")
    
def carregar_chamado():  
    try:     
        arquivo_chamado = open("C:/Users/corin/OneDrive - Senac MS Edu/Documents/chamados.txt", "r", encoding="utf-8")     
        chamados.clear()    
        for linha in arquivo_chamado:        
            linha = linha.strip()        
            if linha != "":
                
                dados = linha.split(";")
                chamado = {
                    "usuario": dados[0],
                    "problema": dados[1],
                    "descricao": dados[2],
                    "status": dados[3]
                    } 
                chamados.append(chamado)
                
        arquivo_chamado.close()
    except FileNotFoundError:    
        print("O arquivo ainda não foi criado")
        
    finally:   
        print("Chamados carregados com sucesso!")
            
def carregar_usuario(): 
    try:    
        arquivo = open("C:/Users/corin/OneDrive - Senac MS Edu/Documents/cadastro_usuario.txt", "r", encoding="utf-8")   
        for linha in arquivo:    
            linha = linha.strip()    
            if linha != "":      
                dados = linha.split(";")
                
                usuario = {
                    "nome": dados[0],
                    "login": dados[1],
                    "senha": dados[2],
                    "perfil": dados[3]
                    }
                
                usuarios.append(usuario)
                         
        arquivo.close()
        
    except FileNotFoundError:   
        print("O arquivo ainda não foi criado")  
        
    finally:   
        print("Usuário carregado com sucesso!")
        
def menu_sistema(usuario_logado):
    while True:   
        print("Menu Sistema")
        print("1 - Registrar Chamado")
        print("2 - Listar Chamados")
        print("3 - Sair")
    
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:       
            registrar_chamados(usuario_logado)       
        elif opcao == 2:      
            carregar_chamado()      
            if len(chamados) == 0:          
                print("Nenhum chamado registrado!")
            
            else:         
                for chamado in chamados:             
                    print(
                        chamado["usuario"], "-",
                        chamado["problema"], "-",
                        chamado["descricao"], "-",
                        chamado["status"]
                    )    
        elif opcao == 3:     
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
            if usuario_logado != None:
                
                menu_sistema(usuario_logado)
                
        elif opcao == 3:      
            if len(usuarios) == 0:
                
                print("Nenhum usuário cadastrado.")         
            else:
                
                for usuario in usuarios:
                    
                    print(usuario["nome"], "-", usuario["login"], "-", usuario["perfil"])         
        elif opcao == 4:
            
            print("Sair")         
            break      
        else:         
            print("opção inválida")

carregar_usuario()

menu_principal()