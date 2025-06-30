senha = input()

tem_numero = any(c.isdigit() for c in senha)
comprimento_ok = len(senha) >= 8

if comprimento_ok and tem_numero:
    print("Senha válida")
else:
    print("Senha inválida")
