total_compra = 0

quantidade_itens = int(input("quantidade de itens:"))
for i in range (1,quantidade_itens + 1):
    preco = float(input(f"Preço do item {i}: R$ "))
    total_compra += preco

media = total_compra / quantidade_itens

print(f"\nTotal da compra: R$ {total_compra:.2f}")
print(f"Média por item: R$ {media:.2f}")
