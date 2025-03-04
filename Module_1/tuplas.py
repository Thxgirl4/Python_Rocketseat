# ordenada e imutável

minha_tupla = (1, 2, 2, 3, 4)
print("exemplo de tupla: ", minha_tupla)  
print(minha_tupla[0])
print(minha_tupla[1])

print("tupla[-1]: ", minha_tupla[-1])

# método count () retorna a quantidade de ocorrências de um elemento na tupla
contagem = minha_tupla.count(2)
print("contagem de 2 na tupla: ", contagem)

indice = minha_tupla.index(3)
print("índice do elemento 3 na tupla: ", indice)