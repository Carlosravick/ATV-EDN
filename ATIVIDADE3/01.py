
idade = int(input("Digite a sua idade: "))


if 0 <= idade <= 12:
    categoria = "Criança"
elif 13 <= idade <= 17:
    categoria = "Adolescente"
elif 18 <= idade <= 59:
    categoria = "Adulto"
elif idade >= 60:
    categoria = "Idoso"
else:
    categoria = "Idade inválida"


print(f"Você é classificado como: {categoria}")