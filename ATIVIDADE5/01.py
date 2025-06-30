def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    return valor_conta * (porcentagem_gorjeta / 100)

# Teste
valor_conta = 150.0
porcentagem = 10
gorjeta = calcular_gorjeta(valor_conta, porcentagem)
print(f"Gorjeta para conta de R$ {valor_conta} com {porcentagem}%: R$ {gorjeta:.2f}")
