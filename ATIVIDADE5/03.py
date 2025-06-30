valor_original = float(input())
porcentagem_desconto = float(input())

valor_desconto = valor_original * (porcentagem_desconto / 100)
preco_final = valor_original - valor_desconto

print(f"Preço final: R$ {preco_final:.2f}")
