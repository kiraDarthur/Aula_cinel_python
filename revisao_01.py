fp = with open("numeros.txt", "r")
#le tudo e quebra em linhas
cont = fp.read().split("\n")
#
numero = list(map(int, cont))



soma = sum(numero)
media = soma / len(numero)
quantidade = 0

