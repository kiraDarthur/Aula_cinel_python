
"""
Cria um programa que: • Leia um ficheiro de texto (qualquer) •
 Conte quantas vezes cada palavra aparece • Mostre as palavras e
  respetivas contagens """

contagem_palavras = {}

With open("texto.txt", "r") as ficheiro:



for linha in ficheiro:

    palavras = linha.strip().split()



    for palavra in palavras:

        palavra = palavra.lower()



        if palavra in contagem_palavras:

            contagem_palavras[palavra] = contagem_palavras[palavra] + 1

        else:

            contagem_palavras[palavra] = 1



for palavra, contagem in contagem_palavras.items():


    print(palavra, ":", contagem)








