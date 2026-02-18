"""
range - função que gera uma sequência de números, muito utilizada em loops for
A função range() é uma função embutida do Python que gera uma sequência de números inteiros.
Ela é frequentemente usada em loops 'for' para iterar um número específico de vezes ou para

Sintaxe: range(start, stop, step)
start: Início (inclusivo, padrão 0)
stop: Fim (exclusivo)
step: Passo (padrão 1)

"""

numeros = range(0, 10, 1) # Reduzi para 10 para facilitar a visualização

# DICA SENIOR: O range é "Lazy" (Preguiçoso)
# Se você der print(numeros), ele não mostra a lista [0, 1, 2...], mostra o objeto range.
# Isso economiza memória. Ele só gera o número quando o loop pede.
print(f"Objeto range: {numeros}") 
print(f"Lista convertida (apenas para debug): {list(numeros)}")

# Iterando
for numero in numeros:
    print(numero) 

print("-" * 20)

# --- VARIAÇÕES DO RANGE ---

# 1. Omissão de parâmetros (Start=0, Step=1)
for i in range(5):
    print(f"Padrão (0 até 4): {i}")

# 2. Passo (Step) diferente de 1 (Pares)
for i in range(0, 11, 2):
    print(f"Pares (0 a 10): {i}")

# 3. Passo Negativo (Contagem Regressiva)
for i in range(10, 0, -1):
    print(f"Regressiva: {i}")

print("-" * 20)

# --- DICA DE ALGORITMOS: Range com Len ---
# Em algoritmos, muitas vezes precisamos saber a POSIÇÃO (índice) do elemento,
# não apenas o valor. Usamos range(len(lista)).

tech_giants = ["Google", "Amazon", "Apple", "Microsoft"]

for i in range(len(tech_giants)):
    print(f"Rank {i+1}: {tech_giants[i]}")
