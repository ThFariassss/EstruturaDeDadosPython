def exibir_mensagem():
    print("Olá Mundo!")
def exibir_mensagem_2(nome):
    print(f"Seja bem vindo{nome}!")
def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja Bem vindo {nome}!")
exibir_mensagem()#exibe a mensagem ola mundo:1
exibir_mensagem_2(nome="Thiago")#Passa o nome 
exibir_mensagem_3()#Anonimo:3
exibir_mensagem_3(nome="Rafaella")#Passa o Nome
def exibir_idade():
    print(22)
def exibir_idade_2(idade):
    print(f"Sua idade é{idade}!")
exibir_idade()
exibir_idade_2(idade= 21)

#RETORNANDO VALORES
def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

def func_3():
    print("Olá mundo!")
    return None


print(calcular_total([10, 20, 30]))
print(retorna_antecessor_e_sucessor(10))
print(func_3())#Retorna NONE

#Argumentos Nomeados: chave = valor
def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat","Palio",2002, "ABC-1234")

#ARGS e Kwargs:O metodo recebe os valores como tupla e dicionario respectivamente
def exibir_poema(data_extenso, *args, **Kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in
Kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema(
"Quarta-Feira, 27 de dezembro de 2023"
"Zen of Python", "Beautiful is better than ugly.", autor = "Tim Peters",
ano =1999)
