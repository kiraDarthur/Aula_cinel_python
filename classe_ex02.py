lista_aluno = []
class Aluno :
    def __init__(self, nome,apelido,num,curso):
        self.nome = nome
        self.apelido = apelido
        self.num = num
        self.curso = curso

    def __str__(self):
        return (
            f"Nº do aluno:{self.num}\n"
            f"Nome completo:{self.nome} {self.apelido}\n"
            f"Cursoo: {self.curso}\n"
        )

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
    numero =  int(input("Qual o nº do aluno que deseja atualizar? "))
    for aluno in lista_aluno :
        if numero == aluno.num:
            nome = aluno.nome
            op =  input(f"Deseja alterar o nome {nome} (s/n)?")
            if op == "s":
                novonome = input("Qual nome correto?").strip().title()
                aluno.nome = novonome

        apelido = aluno.apelido
        op = input(f"Deseja alterrar o apelido {apelido} (s/n)").lower()
        if op == "s":
            novoapelido = input("Qual nome correto?").strip().title()
            aluno.apelido = novoapelido

        curso = aluno.curso
        op = input(f"Deseja alterrar o curso {curso} (s/n)").lower()
        if op == "s":
            novocurso = input("Qual nome correto?").strip().title()
            aluno.curso = novocurso

        print("Dados atualizados com sucesso")
        return
    print("Dados atualizados com sucesso")
def mostrar():
    for aluno in lista_aluno:
        print(aluno)
def sair():
    with open("aluno.csv","w", encoding="utf-8") as fp:
        for aluno in lista_aluno[0:len(lista_aluno)-1]:
            linha = aluno.nome +";"+ aluno.apelido + ";" + aluno.num + ";" + aluno.curso + "\n"
            fp.write(linha)

    linha =  aluno[-1].nome + ";" + aluno[-1].apelido



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



