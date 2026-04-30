preco_unitario = 12.50
quantidade = int(input("Quantas camisas você deseja comprar? "))
if quantidade <= 5:
    desconto = 0.03
elif quantidade <= 10:
    desconto = 0.05
else:
    desconto = 0.07

total_sem_desconto = quantidade * preco_unitario
valor_do_desconto = total_sem_desconto * desconto
total_com_desconto = total_sem_desconto - valor_do_desconto


print("Quantidade de camisas: ", quantidade)
print("Preço unitário: R$", preco_unitario)
print(f"Desconto aplicado: {desconto * 100:.2f}%")
print(f"Total sem desconto: R$ {total_sem_desconto:.2f}")
print(f"Valor do desconto: R$ {valor_do_desconto:.2f}")
print(f"Total a pagar: R$ {total_com_desconto:.2f}")