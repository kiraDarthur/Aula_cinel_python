"""
dade uma frase, conte quantas vezes cada palavra aparrece
"""
frase = "Python é bom e python é facil"

palavras = frase.split()
contador = {}

for p in palavras:
    if p in contador:
        contador[p] += 1
    else:
        contador[p] = 1
print(palavras)
print(contador)
#split separa as STR


