#Copy:
contatos = {
    "thiagomrst1@gmail.com": {"nome": "Thiago", "telefone": "9859-20699"}

}
copia = contatos.copy()
copia["thiagomrst1@gmail.com"] =  {"nome": "Th"}

print(contatos["thiagomrst1@gmail.com"])

print(copia["thiagomrst1@gmail.com"])

#fromkeys: Ele cria um novo dicionário com chaves fornecidas e um valor padrão opcional para todas essas chaves.
print(dict.fromkeys(["nome", "telefone"]))#none
print(dict.fromkeys(["nome","telefone"], "vazio"))#valor vazio

#get: é utilizado para obter o valor associado a uma chave em um dicionário
contatos = {
    "thiagomrst1@gmail.com": {"nome": "Thiago", "telefone": "9859-20699"}
}
print(contatos.get("chave"))#se não encontrar a chave = none
print(contatos.get("chave", {}))#se não encontrar, retorna vazio
print(contatos.get("thiagomrst1@gmail.com", {}))#essa chave existe e encontra e retorna a chave q existe.

#items: é usado para obter uma visão de itens (pares chave-valor) de um dicionário
contatos = {
    "thiagomrst1@gmail.com": {"nome": "Thiago", "telefone": "9859-20699"}
}
print(contatos.items())

#keys:As keys() podem ser usadas para acessar os elementos do dicionário como podemos fazer para a lista,
contatos = {
    "thiagomrst1@gmail.com": {"nome": "Thiago", "telefone": "9859-20699"}
}
print(contatos.keys())

#pop:remove e retorna o valor que ele removeu
contatos = {
    "thiagomrst1@gmail.com": {"nome": "Thiago", "telefone": "9859-20699"}
}
print(contatos.pop("thiagomrst1@gmail.com"))

print(contatos.pop("thiagomrst1@gmail.com", {}))

#setDefault:étodo de dicionário que retorna o valor associado à chave especificada.
contato = {'nome': 'Thiago', 'telefone': '9859206-99'}
print(contato.setdefault("nome", "Rafaella"))
print(contato)
print(contato.setdefault("idade", 28))
print(contato)

#update:usado para atualizar um dicionário com elementos de outro dicionário ou de uma sequência de pares chave-valor
contatos = {
    "thiagomrst1@gmail.com": {"nome": "Thiago", "telefone": "9859-20699"}
}
contatos.update({"thiagomrst1@gmail.com": {"nome": "Th"}})
print(contatos)
contatos.update({"rafa.mar@hotmail.com": {"nome": "Rafa"}})
print(contatos)

#values:retorna uma visão dos valores no dicionário
contatos = {
    "thiagomrst1@gmail.com":{"nome": "Thiago","telefone": "51985920699"},
    "thiagomrst@gmail.com":{"nome": "Th","telefone": "519785231"},
    "rafa.mar@hotmail.com":{"nome": "Rafaella","telefone": "51985154"},
    "thiagolias@hotmail.com":{"nome": "Charizard","telefone": "1212115", "extra": {"a": 1}},
}
print(contatos.values())

#in:verificar se um determinado valor está presente em uma sequência (como uma lista, tupla, string, etc.) ou em uma estrutura de dados que suporte a operação de pertencimento.
contatos = {
    "thiagomrst1@gmail.com":{"nome": "Thiago","telefone": "51985920699"},
    "thiagomrst@gmail.com":{"nome": "Th","telefone": "519785231"},
    "rafa.mar@hotmail.com":{"nome": "Rafaella","telefone": "51985154"},
    "thiagolias@hotmail.com":{"nome": "Charizard","telefone": "1212115", "extra": {"a": 1}},
}
print("thiagomrst1@gmail.com" in contatos)
print("thmrst1@gmail.com" in contatos)
print("idade" in contatos ["thiagomrst1@gmail.com"])
print("telefone" in contatos ["rafa.mar@hotmail.com"])

#del:
contatos = {
    "thiagomrst1@gmail.com":{"nome": "Thiago","telefone": "51985920699"},
    "thiagomrst@gmail.com":{"nome": "Th","telefone": "519785231"},
    "rafa.mar@hotmail.com":{"nome": "Rafaella","telefone": "51985154"},
    "thiagolias@hotmail.com":{"nome": "Charizard","telefone": "1212115", "extra": {"a": 1}},
}
del contatos["thiagomrst1@gmail.com"]["telefone"]
del contatos["rafa.mar@hotmail.com"]
print(contatos)

