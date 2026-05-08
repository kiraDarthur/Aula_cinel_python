"""
3. Cria um programa que: • Leia um ficheiro produtos.txt no formato
nome;preco • Guarde os dados num dicionário • Mostre o produto mais caro
 Mostre o mais barato
produtos = {} """

ficheiro = open("produtos.txt", "r")



for linha in ficheiro:

    dados = linha.strip().split(";")

    nome = dados[0]

    preco = float(dados[1])

    produtos[nome] = preco



ficheiro.close()



if len(produtos) > 0:

    nomes = list(produtos.keys())

    primeiro_nome = nomes[0]



    mais_caro_nome = primeiro_nome

    mais_caro_valor = produtos[primeiro_nome]



    mais_barato_nome = primeiro_nome

    mais_barato_valor = produtos[primeiro_nome]



    for nome, preco in produtos.items():

        if preco > mais_caro_valor:

            mais_caro_valor = preco

            mais_caro_nome = nome



        if preco < mais_barato_valor:

            mais_barato_valor = preco

            mais_barato_nome = nome



    print("Produto mais caro:", mais_caro_nome, "que custa", mais_caro_valor)

    print("Produto mais barato:", mais_barato_nome, "que custa", mais_barato_valor)

else:

    print("O ficheiro estava vazio.")



