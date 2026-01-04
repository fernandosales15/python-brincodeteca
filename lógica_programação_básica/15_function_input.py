# Função 'input()' captura dados do usuário via teclado. O retorno é sempre uma String (str).
nome_sobrenome = input("Digite seu nome e sobrenome: ").strip() # .strip() remove espaços antes e depois
print(f'Perfeito! Você é o {nome_sobrenome}')

idade = int(input("Digite sua idade: ")) # Convertendo a string para inteiro para poder fazer cálculos.
print(f'Legal! Você tem {idade} anos de idade.')
