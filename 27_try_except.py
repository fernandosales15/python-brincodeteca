"""
Conceito de 'try except' em Python
O bloco try except é utilizado para tratar erros que podem ocorrer durante a execução do código.
Isso permite que o programa continue rodando mesmo que um erro ocorra, ao invés de parar abruptamente.

"""

nome_digitado = input("Olá, digite o seu nome: ")
numero_digitado = input(f"Olá, {nome_digitado} digite um número: ")

try: 
    numero_digitado = int(numero_digitado) #Se a conversão for possível aqui, o código continua dentro do bloco try
    print(f"Legal {nome_digitado}, aceitei sem problemas o seu número {numero_digitado}")
    
except ValueError: # Boa prática: Especifique o erro (ValueError é o erro de conversão de tipos)
    print(f"Ops {nome_digitado}, não consegui transformar o que vocé digitou em número.")
    