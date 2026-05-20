dados = []
disciplinas = []

def cadastrar_aluno():
    nome = input("Informe o nome do aluno: ")
    idade = int("Informe a idade do aluno: ")
    sexo = input("Informe o sexo: F - Feminino / M - Masculino")
    dados.append([nome, idade, sexo])
    print("Aluno cadastrado com sucesso!!!")
    
def cadastrar_disciplinas():
    disciplina = input("Digite o nome da disciplina: ")
    ch = int(input("Informe a carga horária"))
    disciplinas.append([disciplina, ch])
    print("Disciplina cadastrada com sucesso!!!")
    
while True:
    print("---Sistema Acadêmico---")
    print(" 1 - Cadastar Aluno?")
    print(" 2 - Cadastrar Disciplina?")
    op = int(input("Informe o que deseja: "))
    
    if op == 1:
        cadastrar_aluno()
    elif op == 2:
        cadastrar_disciplinas()
    else:
        print("Saindo do Sistema...")

