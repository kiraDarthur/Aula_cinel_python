"""
 Cria um dicionário com 5 alunos e respetivas notas (entre 0 e 20) e: •
  Mostra todos os alunos • Calcula a média das notas • Listagem dos alunos
   com nota positiva (>= 10) """

alunos = {"Ana": 15, "Rui": 8, "Maria": 18, "Jose": 10, "Eva": 12}

for nome, nota in alunos.items():

if nota >= 10:

print(f"Aprovado: {nome} com {nota}")


