pares = 0
impares = 0

while True:
    entrada = input()
    if entrada == "":
        break
    num = int(entrada)
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Pares: {pares}")
print(f"Ímpares: {impares}")
