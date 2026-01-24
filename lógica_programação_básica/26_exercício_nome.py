"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome_digitado = input("Digite o seu nome e sobrenome: ")
idade_digitada = input("Digite a sua idade: ")

# Em Python, strings vazias "" valem False. Strings preenchidas valem True.
# Por isso, podemos simplificar a checagem:
if nome_digitado and idade_digitada:
    print(f"Seu nome é {nome_digitado}")
    print(f"Seu nome invertido é {nome_digitado[::-1]}")
    print(f"Seu nome contém ou não espaços? {' ' in nome_digitado}")
    print(f"Seu nome tem {len(nome_digitado)} letras")
    print(f"A primeira letra do seu nome é {nome_digitado[0]}")
    print(f"A última letra do seu nome é {nome_digitado[-1]}")
else:
    print("Desculpe, você deixou campos vazios.")
          