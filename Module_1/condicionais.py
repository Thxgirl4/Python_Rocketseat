# decisões no código

# if, elif e else

# exemplo de if

idade = 18
print("Exemplo de comando if")
if idade >= 18:
    print("Você é maior de idade")
elif idade >= 12:
    print("Você é adolescente")
else:
    print("Você é menor de idade")

mensagem = "Pode tirar CNH" if idade >= 18 else "Não pode tirar a CNH" 
print(mensagem)   