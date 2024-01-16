frutas = ["Laranja","Maca","uva"]
print(frutas)

frutas = []
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari","F8",420000,2021,2900,"Rio grande do Sul", True]
print(carro)

frutas = ["Melancia","Morango","Bergamota"]
print(frutas[2])
print(frutas[-2])

#MATRIZES BI

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]
print(matriz[0])

print(matriz[0][0])

print(matriz[1][-1])

print(matriz[2][-1])

#FATIAMENTO
lista = ["p","y","t","h","o","n"]

print(lista[2:])

print(lista[:2])

print(lista[1:3])

print(lista[0:3:2])

print(lista[::])

print(lista[::-1])

#Iterar listas for
carros =["Gol","celta","palio"]

for carro in carros:
    print(carro)

#Função Inumerate
carros =["Ferrari","BMW","Mercedes"]

for i, carro in enumerate(carros):
    print(f"{i}: {carro}")

#Compreensão de listas, cria uma nova lista com base nos valores de uma lista existente

numeros =[1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2==0:
        pares.append(numero)
        print(pares)
    
numeros = [1, 30, 21, 2, 9, 65, 34]
pares =[numero for numero in numeros if numero % 2 ==0]
print(pares)

#Modificando valores 
numeros =[1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero**2)
    print(quadrado)

numeros =[1, 30, 21, 2, 9, 65, 34]
quadrado = [numero **2 for numero in numeros]
print(quadrado)
