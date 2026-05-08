"""
 Importe o conteúdo do ficheiro para um dicionário onde a chave será o 1º
campo (NIF). Os restantes elementos de cada linha deverão ser
armazenados como lista associados à chave NIF.
• Deverá indicar quantos registos foram lidos do ficheiro
"""

with open ("clientes.csv" , "r",newline="",encoding="utf-8") as ficheiro:
    clientes = {}
    for linha in ficheiro:
        linha = linha.strip()
        if not linha:
            continue
        campos = linha.split(';')
        nif = campos[0]
        nome = campos[1]
        local = campos[2]
        idade = campos[3]
        regiao = campos[4]
        #print(nif,nome,local,idade,regiao)
        resto = nome ,local,idade,regiao
        #print(resto)
        teste = campos[1:]
        #clientes[nif] =resto
        clientes[nif] = teste
    print(clientes)
