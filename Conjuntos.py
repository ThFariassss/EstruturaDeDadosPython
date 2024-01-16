#Set: Elimina duplicatas
numeros =  set([1,2,3,4,1,2,5])
print(numeros)

letras = set("abacaxi")
print(letras)

carros = set(("Palio","Gol","Renault","Gol"))
print(carros)

#acessar os dados:é necessário converter o conjunto para lista.
numeros = {1,2,3,2}
numeros = list(numeros)
print(numeros)

#iterar conjuntos através de um for
carros = {"gol","celta","palio"}
for carro in carros:
    print(carro)

#função enumerate:saber o indice do elemento
carros = {"gol","celta","palio"}
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

#Métodos da classe set:
#UNION:
conjunto_a= {1,2,}
conjunto_b= {2,3,}
print(conjunto_a.union(conjunto_b))

#Intersect:
conjunto_a={1,2,3}
conjunto_b={2,3,4}
print(conjunto_a.intersection(conjunto_b))

#Difference:
conjunto_a={1,2,3}
conjunto_b={2,3,4}
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

#symmetric_difference
conjunto_a={1,2,3}
conjunto_b={2,3,4}
print(conjunto_a.symmetric_difference(conjunto_b))

#issubset
conjunto_a={1,2,3}#Todos elementos de A, pertencem a B?
conjunto_b={4,1,2,5,6,3}#Todos elementos de B, pertencem a A?
print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))

#issuperset
onjunto_a={1,2,3}#Todos elementos de B, pertencem a A?
conjunto_b={4,1,2,5,6,3}#Todos elementos de A, pertencem a B?
print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))

#isdisjoint:Todos os elementos de um conjunto, não estão em outros conjunto.
conjunto_a={1,2,3,4,5}
conjunto_b={6, 7, 8, 9,}
conjunto_c={1, 0}
print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))

#add
sorteio = {1, 23}
sorteio.add(25)
sorteio.add(42)
sorteio.add(25)
print(sorteio)

#Clear
sorteio = {1, 23}
sorteio.clear()
print(sorteio)

#Copy
sorteio = {1, 23}
sorteio.copy()
print(sorteio)

#discard
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
numeros.discard(1)
numeros.discard(45)#n existe e n da erro
print(numeros)

#pop
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(numeros.pop())#tira o 0
print(numeros.pop())#tira o 1
print(numeros.pop())#tira o 2

#Remove
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
numeros.remove(0)
print(numeros)

#len
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(len(numeros))

#in
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(1 in numeros)
print(10 in numeros)



