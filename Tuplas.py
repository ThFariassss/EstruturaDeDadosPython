#São imutáveis e listas são mutaveis, podemos criar classes através da classe tuple
frutas = ("Laranja","pera","uva",)
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple ([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",)
print(pais)

#Acesso Direto
frutas = ("maça","Laranja","pera","uva",)
print(frutas[0])
print(frutas[2])
print(frutas[-1])
print(frutas[-2])

#tuplas aninhadas, matrizes
matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (5, 6, "c"),
)
print(matriz[0])
print(matriz[0][0])
print(matriz[0][1])
print(matriz[0][-1])
print(matriz[-1][-1])

#fatiamento
tuplas =("p","y","t","h","o","n",)
print(tuplas[2:])
print(tuplas[:2])
print(tuplas[1:3])
print(tuplas[0:3:2])
print(tuplas[::])
print(tuplas[::-1])

#iterar tuplas
carros = ("gol","celta","palio",)
for indice, carro in enumerate(carros):
    print(f"{indice}: {carros}")

#metodos count
cores = ("vermelho","azul","verde","vermelho")
print(cores.count("vermelho"))
print(cores.count("azul"))
print(cores.count("verde"))

#index
linguagens = ("python","js","c","java","csharp")

print(linguagens.index("java"))
print(linguagens.index("python"))




