# 1. (n + n) - Parenteses são executados primeiro / Do mais interno para o mais externo
resultado1 = (300 + 5) * 2 #Resultado esperado 610 
print("O resultado da expressão da variável 'resultado1' é: ", resultado1)

# 2. Exponenciação (**) - Vem depois dos parênteses, mas ANTES da multiplicação
# O cálculo é: 2 elevado a 3 (8), depois multiplicado por 10.
resultado2 = 10 * 2 ** 3 
print("O resultado da exponenciação (2**3) * 10 é: ", resultado2)

# 3. (n * n) / Multiplicação e Divisão tem a mesma precedência, 
# e eles vem depois dos parênteses, depois de exponenciação e antes de soma / subtração.
resultado3 = 700 + 11 * 2 #resultado esperado 722
print("O resultado da expressão da variável 'resultado3' é: ", resultado3)

# 4. (n - n) - Subtração e Soma tem a mesma precedência, eles vem por último
resultado4 = 10 * 100 + 900 #resultado esperado 1900
print("O resultado da expressão da variável 'resultado4' é: ", resultado4)

# Conceito PEMDAS: Parênteses -> Expoentes -> Mult/Div -> Soma/Subtração