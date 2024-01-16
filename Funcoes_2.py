#Positional only
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 2000, "ABC-1234", marca = "Fiat", motor = 1.0 ,
combustivel = "Gasolina" )#Valido

#criar_carro(modelo = "Palio", ano=2000,placa ="ABC-1234", marca = "Fiat", motor = 1.0 ,
#combustivel = "Gasolina" )#invalido

#Keyword only
def criar_carro(*,modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
    
criar_carro(modelo = "Palio", ano=2000,placa ="ABC-1234", marca = "Fiat", motor = 1.0 ,
combustivel = "Gasolina" )#Valido 

#criar_carro("Palio", 2000, "ABC-1234", marca = "Fiat", motor = 1.0 ,
#combustivel = "Gasolina" )#Invalido

#kEYWORD and Positional only
def criar_carro(modelo, ano, placa, /, *,marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 2000, "ABC-1234", marca = "Fiat", motor = 1.0 ,
combustivel = "Gasolina" )#Valido

#criar_carro(modelo = "Palio", ano=2000,placa ="ABC-1234", marca = "Fiat", motor = 1.0 ,
#combustivel = "Gasolina" )#invalido

#OBJETOS DE PRIMEIRA Classe:Pode ser passado por parametro e usada em estruturas de dados
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def test(a, b):
    return a * b
def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")
exibir_resultado(10, 10, somar)
exibir_resultado(10,10, subtrair)
exibir_resultado(5,10, test)

op = somar
print(op(1,23))

#Escopo local e escopo Global:
salario = 2000

def salario_bonus(bonus):
    global salario

    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux = {lista_aux}")

    salario += bonus
    return salario

lista = [1]
salario_com_bonus = salario_bonus(500)
print(salario_com_bonus)
print(lista)
