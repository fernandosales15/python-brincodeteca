"""Operadores Lógicos: in / not in - Verifica a presença ou ausência de um valor em uma 
coleção pelo índice e retorna True / False."""

nome = "Fernando"
print("F" in nome) #Resulta em 'True' pois existe a letra "F" na variável nome.
print("S" in nome) #Resulta em 'False' pois não existe a letra "S" na variável nome.

#Acessando letra pelo índice
print(nome[1]) #Imprimirá a letra "e", que está no índice 1 da string "Fernando".
print(nome[-3]) #Imprimirá a letra "n", que está no índice -3 da string "Fernando".

# --- DICA SENIOR: Operador 'not in' e Legibilidade ---
# O 'not in' verifica a AUSÊNCIA. É a forma "Pythonica" de escrever.
# Evite: if not "a" in nome: (Funciona, mas é menos legível)
# Prefira: if "a" not in nome: (Lê-se como inglês: "if a not in name")

print("z" not in nome) # True (z não está em Fernando)
print("n" not in nome) # False (n está em Fernando)

busca = input("Digite uma letra para buscar no nome: ")

if busca in nome:
    print(f"Encontrei a letra '{busca}' no nome {nome}!")
else:
    print(f"A letra '{busca}' NÃO está no nome {nome}.")