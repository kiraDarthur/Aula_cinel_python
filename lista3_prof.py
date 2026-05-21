class Contacto:
    def __init__(self,nome,apelido,datanasc,email,telefone):
        self.nome = nome
        self.apelido = apelido
        self.daranasc = datanasc
        self.email= email
        self.telefone = telefone

    def __str__(self):
        return (f"___\nNome:{self.nome}\nApelido{self.apelido}\nData de nascimento: {self.daranasc}"
                f"\nE-Mail{self.email}\nTelefone{self.telefone}")
class Agenda :
    def ___init___(self):
        self.lista = []
    def adicionar(self,contacto):
        self.lista.append(contacto)

    def novo(self):
        nome = input("diga").title().strip()
        apelido = input("diga").title().strip()
        datanasc = input("diga").title().strip()
        email = input("diga").title().strip()
        telefone = input("diga").title().strip()
        self.lista.append(Contacto(nome, apelido, datanasc, email, telefone))


    def remover(self,telefone):
        for elem in self.lista:
            if elem.telefone == telefone:
                self.lista.remove(elem)
                print("Contacto removido com sucesso!")
                return

    def procurar (self,nome):

        for elem  in self.lista:
            if elem.nome == nome :
                print(elem)
                encontrar  = True

        if not encontrar :
            print("Esse nome não existe na agenda")

    def listar(self):
        if len(self.lista) == 0:
            print("Não existem contactos na agenda")
            return

        self.lista.sort(self.lista.nome)


ag = Agenda()
#criar objeto em forma manual
ag.adicionar(Contacto("Ana","Silva","12-12-2000","anasilva@hotmail.com","918123123"))
ag.adicionar(Contacto("Arthur","Fonseca","12-12-2010","arthura@hotmail.com","918999123"))
ag.adicionar(Contacto("itachi","andrade","12-12-2019","itachi@hotmail.com","918123987"))

while True :
    print("######################")
    print("1 - Adicionar\n2 - Remover\n3 - Procurar\n4 - Listar\n0 - Sair\n")
    op = input("Escolha a sua opçao: \n")

    match op:
        case "1" :
            ag.adicionar()

        case "2":
            telefone = input("Qual o contacto telefonico que deseja remover?")
            ag.remover(telefone)

        case "3":
            nome = input("Qual o nome do contacto?").title().strip()
            ag.procurar(nome)

        case "4":
            ag.listar()

        case "0":
            sair = input("Tem certeza que quer sair ? (s/n)")

            if sair == "s".lower():
                print("Você  saiu do programa ,ATÉ MAIS !!!")
                break
            else:
                sair = input("Tem certeza que quer sair ? (s/n)")

        #case other:
                #print("Opção invalida")
        #input("«ENTER» para continuar ")