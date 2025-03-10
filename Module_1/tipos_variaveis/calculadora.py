operacao = input("Digite a operação desejada (soma, sub, mult, div): ")
numero1 = int(input("Digite o 1º numero: "))
numero2 = int(input("Digite o 2º numero: "))

if operacao == "soma":
        resultado = numero1 + numero2

elif operacao == "sub":
        resultado = numero1 - numero2

elif operacao == "mult":
        resultado = numero1 * numero2

elif operacao == "div":
        resultado = numero1 / numero2

else:
        resultado = "operação não suportada"

print("O resultado da operação é: ", str(resultado))


