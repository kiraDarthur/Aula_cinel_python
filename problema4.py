""""
Crie um dicionario que separe numeros pares e impares
"""
numeros = [1,2,3,4,5,6,7,8]
resultado = {
    "pares": [],
    "impares" : []
}


for n in numeros:
    if n % 2 == 0:
        resultado["pares"].append(n)
    else:
            resultado["impares"].append(n)

#for parar,impare in resultado.items() :
   #print(f"{parar} \n{impare}")

print(resultado)