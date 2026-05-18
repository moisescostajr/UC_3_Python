print("-" * 55)
print("=== SISTEMA DE BOLETIM ON-LINE ===")
print("-" * 55)

alunos = []
disciplinas = []
notas = []

print("=== CADASTRAR DISCIPLINAS ===")

while True:
    nome_disciplina = input("Digite o nome da disciplina: ")
    disciplinas.append(nome_disciplina)
    continuar = input("Deseja cadastrar outra disciplina? (S/N): ")
    if continuar.upper() == "N":
        break

print("=== CADASTRAR ALUNOS ===")

while True:
    nome = input("Digite o Nome do aluno: ")
    idade = input("Digite a Idade do aluno: ")
    sexo = input("Digite o Sexo do aluno (M/F): ")
    serie = input("Digite a Série: ")

    aluno = [nome, idade, sexo, serie]
    alunos.append(aluno)

    continuar = input("Deseja cadastrar outro aluno? (S/N): ")
    if continuar.upper() == "N":
        break

print("=== LANÇAR NOTAS ===")

for i in range(len(alunos)):
    notas_aluno = []

    print(f"\nAluno: {alunos[i][0]}")

    for disciplina in disciplinas:
        print(f"Disciplina: {disciplina}")

        nota1 = float(input("Lançar Nota 1: "))
        nota2 = float(input("Lançar Nota 2: "))
        nota3 = float(input("Lançar Nota 3: "))
        nota4 = float(input("Lançar Nota 4: "))

        media = (nota1 + nota2 + nota3 + nota4) / 4

        notas_disciplina = [disciplina, media]
        notas_aluno.append(notas_disciplina)

    notas.append(notas_aluno)

print("=== BOLETIM ESCOLAR ===")

for i in range(len(alunos)):
    print(f"Nome:  {alunos[i][0]}")
    print(f"Idade: {alunos[i][1]}")
    print(f"Sexo:  {alunos[i][2]}")
    print(f"Série: {alunos[i][3]}")
    
    for nd in notas[i]:
        print(f"Disciplina: {nd[0]}: {nd[1]:.2f}")
