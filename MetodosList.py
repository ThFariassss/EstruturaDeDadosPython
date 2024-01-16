#Append
lista = []
lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])
print(lista)
#Clear
lista = [1, "Python",[40, 30, 20]]
lista.clear()
print(lista)
#Copy
lista = [1, "Python",[40, 30, 20]]
l2 = lista.copy()
print(lista)
print(id(l2), id(lista))
#Count
cores = ["Vermelho", "preto","azul","preto"]
print(cores.count("Vermelho"))
print(cores.count("preto"))
print(cores.count("azul"))
#extend 
linguagens = ["Python","Js","c"]

print(linguagens)
linguagens.extend(["Java","csharp"])#junta os 2
print(linguagens)
#index
linguagens = ["Python","Js","c","Java","csharp"]
print(linguagens.index("Java"))
print(linguagens.index("Js"))
#pop Lista de pratos() = fim da lista
linguagens = ["Python","Js","c","Java","csharp"]

print(linguagens.pop())#pega o csharp q é o ultimo
print(linguagens.pop())#penultimo
print(linguagens.pop())#..
print(linguagens.pop(0))#0= python

#REMOVE
linguagens = ["Python","Js","c","Java","csharp"]

linguagens.remove("c")
print(linguagens)

#REVERSE vai colocar sua lista ao contrario
linguagens = ["Python","Js","c","Java","csharp"]
linguagens.reverse()
print(linguagens)

#sort, ordena a lista
linguagens = ["Python","Js","c","Java","csharp"]
linguagens.sort()
print(linguagens)

linguagens = ["Python","Js","c","Java","csharp"]
linguagens.sort(reverse=True)
print(linguagens)

linguagens = ["Python","Js","c","Java","csharp"]
linguagens.sort(key=lambda x: len(x))#lambda função anônima, x = argumento(python,js..)
print(linguagens)#printa do menor ao maior

linguagens = ["Python","Js","c","Java","csharp"]
linguagens.sort(key=lambda x: len(x), reverse = True)
print(linguagens)#printa do maior ao menor.

#len
linguagens = ["Python","Js","c","Java","csharp"]
len(linguagens)
print(linguagens)

#sorted é uma função, mesma coisa que o sort.
linguagens = ["Python","Js","c","Java","csharp"]

print(sorted(linguagens, key=lambda x: len(x)))

linguagens = ["Python","Js","c","Java","csharp"]
print(sorted(linguagens, key=lambda x:len (x), reverse = True))

frutas =["maçã", "laranja", "uva", "pera"]
print(frutas[3])


