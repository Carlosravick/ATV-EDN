notas = []
while True:
    entrada = input()
    if entrada == "":
        break
    notas.append(float(entrada))

if notas:
    media = sum(notas) / len(notas)
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhuma nota registrada")
