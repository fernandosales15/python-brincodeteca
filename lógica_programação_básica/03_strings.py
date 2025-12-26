# Strings (str) - Aula 03

# 1. Alternando aspas: aspas simples dentro de duplas (e vice-versa) funcionam sem problemas.
print(1, "Olá, Fernando! Você será 'Associate Software Engineer'")
print(2, 'Olá, Fernando! Você será "Associate Software Engineer"')

# 2. Caractere de escape (\): permite usar o mesmo tipo de aspa dentro da string.
print("Fernando, você será \"Associate Software Engineer\"")

# 3. Raw strings (r): Faz com que o Python ignore os caracteres de escape.
# Note como a saída irá mostrar literalmente a barra invertida.
print(r"Fernando, você será \"Associate Software Engineer\"")
