#Operação de Divisão no While
print("Operação de Divisão")
while True:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    
    if num2 == 0:
        print("O divisor não pode ser zero")
        break
    print(f"{num1} / {num2} = {(num1/num2):.2f}")
    
print("Fim da Operação")
    