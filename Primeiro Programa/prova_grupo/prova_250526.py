print("=" * 45)
print("   Sistema de Gestão de Hemonúcleo")
print("=" * 45)

#-----------------------------------------------------------------


def mostrar_recomendacoes():
    recomendacoes = [
        "- Não beba álcool nas 12h antes da doação.",
        "- Evite alimentos gordurosos no dia anterior.",
        "- Não fume 2h antes nem 2h depois da doação.",
        "- Beba bastante água antes e depois da doação.",
    ]
    print("\n--- Recomendações ---")
    for i in recomendacoes:
        print(f"{i}")
    return "Boa doação!!!" 

#-----------------------------------------------------------------

print("\n--- Cadastro do Doador ---")

nome = input("Digite o nome do doador: ")

while True:
    try:
        idade = int(input("Digite a Idade: "))
        break
    except ValueError:
        print("Digite um número válido para a idade.")

responsavel = "não precisa" 

if idade >= 16 and idade <= 17:
    while True:
        responsavel = input("O responsável legal está presente? (Sim/Não): ").strip().lower()
        if responsavel in ("sim", "não", "nao",):
            break
        print("Digite apenas Sim ou Não.")        

while True:
    try:
        peso = float(input("Peso em kg: "))
        break
    except ValueError:
        print("Digite um número válido para o peso.")

while True:
    primeira_doacao = input("É a primeira doacao? (Sim/Não): ").strip().lower()
    if primeira_doacao in ("sim", "não", "nao"):
        break
    print("Digite apenas Sim ou Não.")

while True:
    tem_documento = input("Possui documento com foto? (Sim/Não): ").strip().lower()
    if tem_documento in ("sim", "não", "nao"):
        break
    print("Digite apenas Sim ou Não")

while True:
    boa_saude = input("Está com boa saúde? (Sim/Não): ").strip().lower()
    if boa_saude in ("sim", "não", "nao"):
        break
    print("Digite apenas Sim ou Não")

while True:
    alimentado = input("Está bem alimentado e descansado? (Sim/Não): ").strip().lower()
    if alimentado in ("sim", "não", "nao"):
        break
    print("Digite apenas Sim ou Não")

if idade < 16:
    print("\nIMPEDIDO: Idade abaixo de 16 anos.")
elif idade >= 16 and idade <= 17 and responsavel == "não":
    print("\n IMPEDIDO: Doação permitida SOMENTE com a presença de um responsável legal")
elif idade > 69:
    print("\nIMPEDIDO: Idade acima de 69 anos.")
elif primeira_doacao == "sim" and idade > 60:
    print("\nIMPEDIDO: Primeira doação não permitida após os 60 anos.")
elif peso <= 51:
    print("\nIMPEDIDO: Peso abaixo de 51 kg.")
elif tem_documento != "sim":
    print("\nIMPEDIDO: Necessário documento oficial com foto.")
elif boa_saude != "sim":
    print("\nIMPEDIDO: Doador não está em boas condições de saúde.")
elif alimentado != "sim":
    print("\nIMPEDIDO: Doador precisa estar alimentado e descansado.")

else:
    print("\nAprovado para a próxima fase da triagem!")
    
#-----------------------------------------------------------------


    print("\n--- Histórico Médico ---")

    impedimentos_medicos = {
        "Teve hepatite após os 11 anos de idade?": "Hepatite após os 11 anos.",
        "Tem Doença de Chagas, Câncer ou Sífilis?": "Doença de Chagas, Câncer ou Sífilis.",
        "É portador do HIV ou parceiro de portador?": "HIV.",
        "Tem múltiplos parceiros sexuais?": "Múltiplos parceiros sexuais.",
        "Usa drogas injetáveis ou compartilha seringas?": "Uso de drogas injetáveis.",
    }

    impedido = False
    for pergunta, motivo in impedimentos_medicos.items():
        resposta = input(f"{pergunta} (Sim/Não): ").strip().lower()
        if resposta == "sim":
            print(f"\nIMPEDIDO DEFINITIVAMENTE: {motivo}")
            impedido = True
            break

    if not impedido:
        print("\nAprovado para a próxima fase da triagem!")
        
#-----------------------------------------------------------------


        print("\n--- Período de Espera ---")

        tatuagem = input("Fez tatuagem ou colocou piercing nos últimos 12 meses? (Sim/Não): ").strip().lower()
        transfusao = input("Fez transfusão de sangue nos últimos 12 meses? (Sim/Não): ").strip().lower()
        parto = input("Teve um parto ou está amamentando? (Sim/Não): ").strip().lower()
        prep = input("Usou PrEP/PEP nos últimos 12 meses? (Sim/Não): ").strip().lower()
        endoscopia = input("Fez endoscopia nos últimos 6 meses? (Sim/Não): ").strip().lower()
        gripe = input("Ficou gripado nos últimos 14 dias? (Sim/Não): ").strip().lower()
        dengue = input("Teve dengue recentemente? (Sim/Não): ").strip().lower()
        
        espera = 0

        if tatuagem == "sim" or transfusao == "sim" or parto == "sim" or prep == "sim":
            espera = "Aguardar 12 meses após o procedimento."
        elif endoscopia == "sim":
            espera = "Aguardar 6 meses após o procedimento."
        elif gripe == "sim":
            espera = "Aguardar 14 dias após a gripe."
        elif dengue == "sim":
            tipo_dengue = input("Foi dengue grave? (Sim/Não): ").strip().lower()
            if tipo_dengue == "sim":
                espera = "Aguardar 6 meses após dengue grave."
            else:
                espera = "Aguardar 30 dias após dengue clássica."

        if espera:
            print(f"\nDOAÇÃO SUSPENSA TEMPORARIAMENTE: {espera}")

        else:
            print("\nAprovado para a Doação!")
            
#-----------------------------------------------------------------


            print("\n--- Intervalo Entre Doações ---")

            sexo = input("Sexo biológico (M/F): ").strip().lower()

            while True:
                try:
                    doacoes_no_ano = int(input("Quantas doações fez nos últimos 12 meses? "))
                    dias_desde_ultima = int(input("Há quantos dias foi a última doação? (0 se nunca doou) "))
                    break
                except ValueError:
                    print("Digite um número válido.")

            intervalo = 0

            if sexo == "m":
                if doacoes_no_ano >= 4:
                    intervalo = "Limite de 4 doações por ano atingido - aguarde o próximo ano."
                elif dias_desde_ultima > 0 and dias_desde_ultima < 60:
                    intervalo = f"Aguardar mais {60 - dias_desde_ultima} dia(s) (mínimo: 60 dias)."
            else:
                if doacoes_no_ano >= 3:
                    intervalo = "Limite de 3 doações por ano atingido - aguarde o próximo ano."
                elif dias_desde_ultima > 0 and dias_desde_ultima < 90:
                    intervalo = f"Aguardar mais {90 - dias_desde_ultima} dia(s) (mínimo: 90 dias)."

            if intervalo:
                print(f"\nDOAÇÃO SUSPENSA: {intervalo}")
                

            else:
                print("=" * 45)
                print(f"PARABÉNS, {nome.upper()}!")
                print("  Você está APTO(A) para doar sangue!")
                print("=" * 45)
                
#-----------------------------------------------------------------


                mensagem = mostrar_recomendacoes()
                print(f"\n ***{mensagem}***")
                
#-----------------------------------------------------------------

                

print("-" * 45)
print("  Obrigado pelo uso do Sistema Hemonúcleo!")
print("-" * 45)


#-----------------------------------------------------------------
