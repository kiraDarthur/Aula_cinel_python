"""
troque as chaves pelos valores
"""
d = {
    "a": 1,
    "b": 2,
    "c": 3
}

lista_nova = {}
for x,y in d.items():
    lista_nova[y]= x

print(lista_nova)