class aluno :
    def __init__(self,nome,apelido,num,curso):
        self.nome = nome
        self.apelido =  apelido
        self.num = num
        self.curso = curso

    def  mostrar(self):
        print(f"Nº:{self.num}")
        print(f"Nome completo: {self.nome} {self.apelido}")
        print(f"Curso :{self.curso}")



fistname = input("QUal o seu 1º nome? ")
lastname = input("QUal o seu 2º nome? ")
course= input("Qual curso voce faz ?")
numbers = input("QUal é seu numero ? ")

aluno1 = aluno(fistname,lastname,numbers,course)

aluno1.mostrar()