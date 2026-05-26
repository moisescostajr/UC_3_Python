meses = ["0", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

mes_escolhido = int(input("Digite um número referente ao mês"))

if mes_escolhido >= 0 and mes_escolhido < len(meses):
    print("O mês escolhido foi: ", mes_escolhido, "é:", meses[indice])
else:
    print("Índice inválido!")




