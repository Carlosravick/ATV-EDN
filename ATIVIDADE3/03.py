temp = float(input())
origem = input().strip().lower()
destino = input().strip().lower()

def c_to_f(c): return c * 9/5 + 32
def c_to_k(c): return c + 273.15
def f_to_c(f): return (f - 32) * 5/9
def f_to_k(f): return c_to_k(f_to_c(f))
def k_to_c(k): return k - 273.15
def k_to_f(k): return c_to_f(k_to_c(k))

if origem == destino:
    resultado = temp
elif origem == "celsius":
    if destino == "fahrenheit":
        resultado = c_to_f(temp)
    elif destino == "kelvin":
        resultado = c_to_k(temp)
elif origem == "fahrenheit":
    if destino == "celsius":
        resultado = f_to_c(temp)
    elif destino == "kelvin":
        resultado = f_to_k(temp)
elif origem == "kelvin":
    if destino == "celsius":
        resultado = k_to_c(temp)
    elif destino == "fahrenheit":
        resultado = k_to_f(temp)
else:
    resultado = None

if resultado is not None:
    print(f"{resultado:.2f}")
else:
    print("Unidade inválida")
