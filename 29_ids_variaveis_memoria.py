"""
Conceito de IDs, Variáveis e Memória em Python
Em Python, uma variável é um nome que referencia um valor armazenado na memória.
Cada variável tem um ID único que pode ser obtido usando a função id().
Esse ID representa o endereço de memória onde o valor está armazenado.
"""

# Exemplo de criação de variáveis e obtenção de seus IDs
variavel_a = "Fernando"
print(id(variavel_a)) #imprime o ID (endereço de memória) da variável_a

variavel_b = "Fernando Sales"
print(id(variavel_b)) #imprime o ID (endereço de memória) da variável_b - mesmo valor de variável_a
print(id(variavel_b)) # O ID será DIFERENTE, pois o conteúdo da string mudou ("Fernando" vs "Fernando Sales")

# Para ter o MESMO ID, precisamos apontar para o mesmo objeto:
variavel_c = variavel_a
print(f"ID da variavel_a: {id(variavel_a)}")
print(f"ID da variavel_c: {id(variavel_c)}") # Agora sim: Mesmo ID, pois variavel_c é apenas um apelido para variavel_a