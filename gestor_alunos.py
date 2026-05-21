class ALuno:
    def __init__(self,*,nome,idade=0,media):
        self.nome = nome
        self.idade = idade
        self.media = media


##funçao
def adicionar():
    nome = input("Nome do aluno: ")
    idade = int(float("Qual a sua idade?"))
    media = float(input("Qual o valor da média?"))
    aluno = ALuno(nome=nome,idade=idade,media=media)
    turma.append(aluno)
turma =[]
def listar():
    pass

def procurar():
    pass

def decrecente():
    pass

def remover():
    num = int(input("Qual o número do aluno a remover?"))
    for nome in turma:
        if idade.num == num:

            print(f"Pessoa encontrada : {nome.nome} ")

            confirmar = input("Tem certeza que quer apagar ?(s/n):").lower()

            if confirmar == "s":
                turma.remove(nome)
                print("Pessoa foi removida com sucesso!")
            else:
                print("Remoção cancelada!")
            return

    print("Pessoa nao encontrado!")

def sair():
    pass

while True:
    print("##################################################\n")
    print("1º)Adicionar um novo aluno.")
    print("2º)Listar todos os alunos.")
    print("3º)Procurar um aluno pelo nome.")
    print("4º)Listar alunos ordenados pela maior média.")
    print("5º)Remover aluno.")
    print("6º)A Sair do programa.")
    op = input("Escolha a sua opçao: \n")

    match op:

        case "1":
            adicionar()

        case "2":
            listar()

        case "3":
            procurar()

        case "4":
            decrecente()

        case "5":
            remover()

        case "6":
            sair()





