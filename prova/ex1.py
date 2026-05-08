"""
Cria um programa que: • Leia um ficheiro numeros.txt (1 número por cada
linha do ficheiro) • Some todos os números • Mostre o total da soma e
apresente a média desses valores no ecrã
"""
soma = 0

contagem = 0

with open("numeros.txt", "r") as ficheiro:

for linha in ficheiro:

numero = int(linha.strip()) # strip() remove espaços e \n

soma += numero contagem += 1

print(f"Total: {soma}, Média: {soma/contagem}")


