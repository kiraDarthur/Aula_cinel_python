class contacto():
    def __init__(self,numero,nome):
        self.numero = numero
        self.nome = nome

class Agenda:
    def __init__(self):
        self.lista_contactos = []
    def adicionar(self):
        nome = input("Digite seu Nome: ")
        numero = input("Digite seu Numero: \n")

        novo_contato = contacto(numero,nome)

        self.lista_contactos.append(novo_contato)
        print("Contato adiconado com sucesso!!")


    def remover(self):
        num = input("Digite o numero Telefonico para remover : ")
        try:
            if num < 9:
                print("Estar a faltar numeros repita .")
                num = input("Digite o numero Telefonico para remover : ")
    def procurar(self):
        pass

    def listar(self):
        pass




#Interface do Ultilizador
minha_agenda = Agenda()

while True :
    print("######################")
    print("1 - Adicionar\n2 - Remover\n3 - Procurar\n4 - Listar\n0 - Sair\n")
    op = input("Escolha a sua opçao: \n")

    match op:
        case "1" :
            minha_agenda.adicionar()
        case "2":
            minha_agenda.remover()
        case "3":
            minha_agenda.procurar()
        case "4":
            minha_agenda.listar()
        case "0":
            sair = input("Tem certeza que quer sair ? (s/n)")

            if sair == "s".lower():
                print("Você  saiu do programa ,ATÉ MAIS !!!")
                break
            else:
                sair = input("Tem certeza que quer sair ? (s/n)")

