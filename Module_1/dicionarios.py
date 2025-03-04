# coleção não ordenada de pares chave-valor
pessoa = {"nome": "Icaro", "idade": 12, "cidade": "BH"} # chave-valor

print("Dicionario de exemplo: ", pessoa)

# Acessando valores por chave
print("Nome: ", pessoa['nome'])
print("Idade: ", pessoa["idade"])
print("Cidade: ", pessoa["cidade"])

# atribuir valor ao dicionario
pessoa["sobrenome"] = "Castro"
print("Sobrenome: ", pessoa["sobrenome"])

# atualizar valor
pessoa["idade"] = 15
print("Idade atualizada: ", pessoa["idade"])

# remover chave-valor
del pessoa["cidade"]
print("Dicionario após remoção: ", pessoa)

# método: keys(), values(), items()

# transformar em lista - 
chaves = list(pessoa.keys())
# chaves = pessoa.keys()
print("Chaves do dicionario: ", chaves)
print("Primeira chave: ", chaves[0])

# método values()
valores = list(pessoa.values())
print("Valores do dicionario: ", valores)
print("Primeiro valor: ", valores[0])

# método items()
itens = list(pessoa.items())
print("Pares chave-valor do dicionario: ", itens)
print("Primeiro valor:", itens[0] [1]) 
print("Primeira chave-valor: %s = %s " % (itens[0][0], itens[0][1]))

