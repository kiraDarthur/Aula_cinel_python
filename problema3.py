"""
junte dois dicionrios em um so
"""

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

d3 = {}

for letra,numero in d1.items():
    d3[letra] = numero
for letra,numero in d2.items():
    d3[letra] = numero

print(d3)
