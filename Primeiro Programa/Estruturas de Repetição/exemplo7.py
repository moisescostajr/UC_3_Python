mulheres = 0
homens_acima18 = 0
cont = 0

for cont in range(5):
    
    idade = int(input("Informe sua idade: "))
    if idade < 0:
        break
    sexo = input("Informe seu sexo (M/F): ")
    if sexo == "F" or sexo == "f":
        mulheres = mulheres + 1
    elif sexo == "M" or sexo == "m":
        if idade >= 18:
            homens_acima18 = homens_acima18 + 1
            print(f"Quantidades de mulheres: {mulheres}")
            print(f"Quantidade de homens acima de 18 anos: {homens_acima18}")
            