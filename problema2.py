"""
dado um dicionario de alunos e notas, encontre o aluno com maior nota
"""
notas = {
    "Ana": 8,
    "João": 6,
    "Maria": 9,
    "Pedro": 7
}
maior = 0
nome_aluno = 0

for  nome,nota in notas.items() :
    if nota > maior :
        maior = nota
        nome_aluno = nome

print(f"Melhor Aluno:{nome_aluno}\nNota:{maior}")
#.items() ele separa os items dentro do dicionario para  trabalhar melhor em ciclo for