dados = {"Nome": "Thiago", "idade": 21, "telefone": "(51)-985920699"}
print(dados["Nome"])
print(dados["idade"])
print(dados["telefone"])
dados["Nome"] = "Rafaella"
print(dados)
dados["Idade"] = "21"
print(dados)
dados["telefone"] = "98789-44"
print(dados)

#Dicionarios aninhados:podem armazenar qualquer tipo de objeto como valor ={strings e numeros}
contatos = {
    "thiagomrst1@gmail.com":{"nome": "Thiago","telefone": "51985920699"},
    "thiagomrst@gmail.com":{"nome": "Th","telefone": "519785231"},
    "rafa.mar@hotmail.com":{"nome": "Rafaella","telefone": "51985154"},
    "thiagolias@hotmail.com":{"nome": "Charizard","telefone": "1212115", "extra": {"a": 1}},
}
print(contatos ["thiagomrst1@gmail.com"]["telefone"])

extra = contatos ["rafa.mar@hotmail.com"]
print(extra)

#Iterar: for
for chave in contatos:
    print(chave,contatos[chave])
for chave, valor in contatos.items():
    print(chave, valor)