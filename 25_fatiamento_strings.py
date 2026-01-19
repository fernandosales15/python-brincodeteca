"""
Fatiamento de strings
0123456789...
-9-8-7-6-5-4-3-2-1
fatiamento [inicio:fim:passo]
inicio = índice onde começa o fatiamento (inclusivo)
fim = índice onde termina o fatiamento (exclusivo)
passo = de quanto em quanto ele vai "pular" os caracteres

Exemplos: 'Olá mundo'

função 'len()' retorna o tamanho da string

"""

variavel_de_texto = 'Olá mundo'
print(f"O tamanho da string 'Olá mundo' é: {len(variavel_de_texto)} caracteres")
print(f"Vou fatiar a string 'Olá mundo' = {variavel_de_texto[0:5]}") 

print("-" * 5 + " INVERTENDO UMA STRING" + "-" *5)
nome_e_cargo = "Fernando - Associate Software Engineer" 
print(f"{nome_e_cargo[::-1]}") ## [::-1] é a forma padrão (Pythonica) de inverter. O passo -1 faz ir de trás pra frente.

print("-" * 5 + " FINISH - STRING INVERTIDA - VEJA ACIMA NO CONSOLE" + "-" *5)
print(len(nome_e_cargo))
print(f"Inversão maluca: {nome_e_cargo[-1::-2]}")
