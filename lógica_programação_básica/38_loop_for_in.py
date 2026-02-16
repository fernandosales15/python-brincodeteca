"""

Os loops 'for' são usados para iterar sobre uma sequência 
(como uma lista, tupla, dicionário, conjunto ou string) ou outros objetos iteráveis. 
O loop 'for' é útil quando você sabe o número de iterações que deseja realizar ou 
quando deseja percorrer os elementos de uma coleção.

NOTA MENTAL: Não há vergonha em rever o básico. 
Sêniores consultam a documentação de 'for loops' e 'if/else' frequentemente quando mudam de linguagem.
O importante é entender a lógica de iteração, a sintaxe é apenas detalhe.

"""

cargo_engineer = "Software Engineer"
nivel_carreira = ["Associate", "Pleno", "Senior", "Lead", "Principal", "Staff", "Distinguished", "Fellow"]


# O 'for' funciona assim: "Para cada ITEM dentro da COLEÇÃO"
# Você define o nome do ITEM (letra) e qual é a COLEÇÃO (cargo_engineer)
for letra in cargo_engineer:
    print(letra) #Imprime uma letra por linha/vez da variável 'cargo_engineer'

# DICA SENIOR: Convenção "Singular in Plural"
# Se sua lista está no plural (ex: niveis), use o nome da variável no singular (ex: nivel).
# Isso torna o código autoexplicativo.
for nivel in nivel_carreira:
    print(nivel) #Imprime cada nível de carreira por linha/vez da variável 'nivel_carreira'


# Prova de conceito: O nome da variável pode ser qualquer coisa
# O Python não liga, mas seu colega de trabalho vai achar estranho!
for batata in cargo_engineer:
    # Aqui, 'batata' vai assumir o valor de cada letra ('S', 'o', 'f'...)
    print(f"A letra atual (chamada de batata) é: {batata}") 
