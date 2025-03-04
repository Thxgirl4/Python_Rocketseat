# elementos ordenados e mutáveis

minha_lista = [1, 2, 3, 4, 5, "Jordão", True, False] 

# exibindo a lista
print("lista de exemplo ", minha_lista) 

# exibindo a lista por indice

# mudando o valor do indice 0
minha_lista[0] = "python"
print("lista[0] ", minha_lista[0])
print("lista[5] ", minha_lista[5])

#fatiar a lista do 1 ao 7 
print("lista[1-7] ", minha_lista[1:7])

# do proximo elemnto até o final
print("lista[2:] ", minha_lista[2:])


# métodos de listas

# append(): add um elemento ao final da lista
minha_lista.append("Certo")
print("lista após append: ", minha_lista)

# método index: retorna o indidce do primeiro elemnto = ao valor especificado
indice = minha_lista.index("Certo")
print("indice do elemento certo: ", indice)

# método insert: insere um elemento em um indice especifico
minha_lista.insert(2, 15)
print("lista após insert: ", minha_lista)

# método pop(): remove e retorna um elemento da lista especifico
# se não especificar o indice, remove o último elemento da lista
elemento_removido = minha_lista.pop(3)
print("elemento removido: ", elemento_removido)
print("lista após pop: ", minha_lista)

# método remove: remove o primeiro elemento com valor especificado
minha_lista.remove(True)
print("lista após remove(True): ", minha_lista)

# método sort: para organizar a lista em ordem crescente
minha_lista2 = [16, 15, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
minha_lista2.sort()
print("lista ordenada: ", minha_lista2) # faz a organização da lista com numeros