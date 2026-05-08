lista_aluno = []
class Aluno :
    def __init__(self, nome,apelido,num,curso):
        self.nome = nome
        self.apelido = apelido
        self.num = num
        self.curso = curso

    ############################################################

    #FUNÇÃO

def adicionar():
        nome = input("Qual o nome do aluno?")
        apelido = input(f"Qual o apelido do aluno {nome}?")

        num = int(input(f"QUal O Nº  do aluno {nome} {apelido} na turma ?"))

        while True:
            try:
                if num >= 0:
                    break
                num = input(f"Número tem que ser possitivo!\n"
                            f"Qual o Nº do aluno  {nome} {apelido} na turma ? ")
            except:
                num = input(f"Qual o Nº do aluno  {nome} {apelido} na turma ? ")

        curso = input(f"Que curso frequenta o aluno {nome} {apelido} ?")

        aluno = Aluno(nome, apelido, num, curso)

        lista_aluno.append(aluno)

def remover():
    num  = int(input("Qual o número do aluno a remover?"))
    for aluno in lista_aluno:
        if aluno.num == num:

            print(f"Aluno encontrado : {aluno.nome} {aluno.apelido}")

            confirmar = input("Tem certeza que quer apagar ?(s/n):").lower()

            if confirmar == "s":
                lista_aluno.remove(aluno)
                print("Aluno removido com sucesso!")
            else:
                print("Remoção cancelada!")
            return

    print("Aluno nao encontrado!")
def atualizar():
    pass

def mostrar():
    pass

def sair():
    pass



    #######################################################
while True :
        print("\n\n\n\n")
        print("#######################################")
        print("a). Adiciona aluno")
        print("b). Remover aluno")
        print("c). Atualizar aluno")
        print("d). Mostrar dados de todos alunos")
        print("e). Sair")
        print("######################################")
        #print("\n\n\n\n")

        op = input("Escolha a sua opçao: ").lower()

        match op:

            case "a":
                adicionar()

            case "b":
                remover()

            case "c":
                atualizar()

            case "d":
                mostrar()

            case "e":
                sair()



