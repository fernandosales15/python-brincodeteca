"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero_inteiro = input("Digite um número inteiro: ")

try:
    numero_inteiro = int(numero_inteiro)
except ValueError:
    print(f"O número {numero_inteiro} não é um número inteiro")
else:
    if numero_inteiro % 2 == 0:
        print(f"O número {numero_inteiro} é par")

    else:
        print(f"O número {numero_inteiro} é impar")


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

"""

hora_digitada = input("Digite a hora atual: ")

try:
    hora_digitada = int(hora_digitada)
except ValueError: 
    print(f"A hora {hora_digitada} não é um número inteiro")
    exit()

if hora_digitada >= 0 and hora_digitada <= 18:
    print("Boa tarde.")
elif hora_digitada >= 19 and hora_digitada <= 23:
    print("Boa noite.")
else:
    print("Bom dia.")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 

"""

nome_digitado = input("Digite o seu nome: ")

if len(nome_digitado) <=4:
    print("Seu nome é curto")
elif len(nome_digitado) >= 5 and len(nome_digitado) <= 6:
    print("Seu nome é normal")
else: 
    print("Seu nome é muito grande")