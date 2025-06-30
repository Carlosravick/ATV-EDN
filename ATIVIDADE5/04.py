from datetime import datetime

data_nascimento = input()
data_nasc = datetime.strptime(data_nascimento, "%d/%m/%Y")
data_hoje = datetime.now()

dias_vivo = (data_hoje - data_nasc).days
print(dias_vivo)
