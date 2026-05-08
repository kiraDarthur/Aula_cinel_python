"""
1º
Crie um programa que receba uma palavra e crie um dicionário que conte quantas vezes cada letra aparece.
"""
"""
nome = input("Digite um nome :")

y= {}

for x in nome.strip():
    if x in y:
        y[x] +=1
    else:
        y[x] =1

print(y)
"""
"""
2º
Crie um programa que some todos os valores do dicionário.
"""
"""
numeros = {"a": 10, "b": 20, "c": 30, "d": 40}
soma = 0
for x,y in numeros.items():
    soma += y
print(soma)
"""

"""
3º
Crie um programa que crie um novo dicionário apenas com alunos que tiraram nota maior ou igual a 7.
"""
"""
notas = {
    "Ana": 8,
    "Pedro": 5,
    "Maria": 9,
    "João": 4
}
maior_nota = 0
alunos__nota_alta ={}
for nome,nota in notas.items():
    if nota > 6:
        alunos__nota_alta[nome] = nota

print(alunos__nota_alta)
"""
"""
4º
Peça ao usuário uma frase e crie um dicionário com a contagem de cada palavra.

Exemplo:

Entrada:

python é bom python é fácil

Saída esperada:

{'python':2, 'é':2, 'bom':1, 'fácil':1}

"""
"""
frase = input("Digite uma frase: ")

contagem_frase = {}

for palavras in frase.split():
    if palavras in contagem_frase:
        contagem_frase[palavras] +=1
    else:
        contagem_frase[palavras] =1

print(contagem_frase)
"""

"""
5º
Dado um dicionário:

pessoas = {
    "nome": "Carlos",
    "idade": 25,
    "cidade": "Lisboa"
}

Crie um programa que verifique se a chave "idade" existe no dicionário.
"""
"""
pessoas = {
    "nome": "Carlos",
    "idade": 25,
    "cidade": "Lisboa"
}
if "idade" in pessoas: #se idade existe  no dicionario pessoas
        print("Existe  uma chave chamada: <idade> ")
"""
######################################################################################
#PERGUNTA DE NIVEL MAIS ALTO
"""
1º
Peça ao usuário uma frase e crie um dicionário onde a chave é o tamanho da palavra e o valor é uma 
lista de palavras com esse tamanho.

Exemplo

Entrada

python é muito poderoso

Saída esperada (exemplo):

{
6: ['python'],
1: ['é'],
5: ['muito'],
8: ['poderoso']
}

⚠️ Regras:

use split()

se já existir a chave, adicione na lista

se não existir, crie uma lista
"""

frase = "python é muito poderoso"

frase_x = {}
for letras in frase.split():
    frase_x[len(letras)] = letras
print(frase_x)
