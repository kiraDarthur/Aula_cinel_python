"""
2. Cria um dicionário com 5 alunos e respetivas notas (entre 0 e 20) e:
• Mostra todos os alunos
• Calcula a média das notas
• Listagem dos alunos com nota positiva (>= 10)


"""

notas_alunos = {"arthur":10,"ana":2,"itachi":11,"naruto":9,"sasuke":11}
soma =  0
i = 0
aprovados = []
aluno = []
for alunos, notas in notas_alunos.items():
    aluno.append(alunos)
    soma += notas
    if notas >= 10:
       aprovados.append(alunos)


media = soma /len(notas_alunos)



print(f"Os alunos são: {aluno}"
      f"\nA media da sala foi de: {media}"
          f"\nAlunos com notas maiores ou iguais a 10 : {aprovados}")
