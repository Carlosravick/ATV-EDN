import string

def eh_palindromo(texto):
    texto_limpo = ''.join(c.lower() for c in texto if c.isalnum())
    return texto_limpo == texto_limpo[::-1]

# Testes
frases = [
    "A man, a plan, a canal, Panama",
    "Isso não é um palíndromo",
    "Socorram-me, subi no ônibus em Marrocos"
]

for frase in frases:
    print("Sim" if eh_palindromo(frase) else "Não")
