import csv

lcores = ["Preto", "Branco", "Azul", "Verde", "Vermelho",
"Amarelo", "Castanho", "Rosa", "Laranja", "Cinzento"]

dcores= {}

#for cor in lcores:
    #coring = input(f"Qual a tradução para {cor}?").title()
    #dcores[cor] = coring #isso cria o dicionario

#print(dcores)"

dcores= {
    'Preto': 'Black', 'Branco': 'White', 'Azul': 'Blue', 'Verde': 'Green',
    'Vermelho': 'RED', 'Amarelo': 'Yellow', 'Castanho': 'Brow', 'Rosa': 'Pink'
    , 'Laranja': 'Orange', 'Cinzento': 'Gray'
}

while True:
    corPT = input("Qual a cor a traduzir de PT para ING ?").title()

    if corPT == "":
        print(">>Programa terminou<<".upper())
        break
    if corPT in dcores:
        print(f"{corPT} -> {dcores[corPT]}")
    else:
        print("Essa cor nao foi encontrada no dicionario".upper())ç
#criar arquivo
with open("coress.csv", "w",newline="", encoding="utf-8") as ficheiro: #with open ele abri o ficheiro e ja  feicha ,
    # "passa o nome .csv", "w" de escrever,newline="" evita linhas em branco, encoding = "utf-8" coloca as regras pt,
    escritor = csv.writer(ficheiro) #ele  coloca   no padrao csv,damos o nome desa variavel de ficheiro com as .

    for pt, ing in dcores.items():# separa o dicionario em duas parte .item passa para com virgula
        escritor.writerow([pt,ing])#writerow(): "Escreve uma linha no ficheiro CSV"

print("Ficheiro csv crado com sucesso!")