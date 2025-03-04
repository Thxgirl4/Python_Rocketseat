# Declaração
nome_completo = "Ana Julia"

nome_completo_aspas = """Ana Julia 
Silva"""

nome_complet_quebra = "Ana \
    Julia"

nome = "Ana"
sobrenome = "Castro"

# Formatação
print("Nome completo (1 forma): ", nome_completo)
print("Nome completo (2 forma): " + nome_completo)
print("Nome completo (3 forma): " + "Ana " + "Julia")
print("Nome completo (4 forma): " + "Ana Julia", "Silva")

print("Nome completo (5 forma): ", nome_completo_aspas)
print("Nome completo (6 forma): ", nome_complet_quebra)

# %s - string
print("Nome completo (7 forma): %s" %nome_completo) 
print("Nome completo (8 forma): %s %s" %(nome, sobrenome))
# format - transforma em string
print(f"Nome completo (9 forma): {nome} {sobrenome}")
print("Nome completo (9 forma): {} {}".format(sobrenome, nome))

# .upper() e .lower() - são imutaveis, o valor da variavel não é alterado
# .count() - para contar
# .find() - para encontrar
# .encode() - transforma em bytes
# .decode() - transforma em string
# .replace() - substitui 
# .join() - usado para separar 
# .split() - usado para separar tipo lista
# .strip() - remove espaços subjacentes, começo e final
# .rstrip() - remove espaços a direita
# .lstrip() - remove espaços a esquerda
# .startswith - verifica se começa com 

