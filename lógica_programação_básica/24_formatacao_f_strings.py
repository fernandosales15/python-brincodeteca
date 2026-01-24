"""
Formatação básica de strings
s - string
d - int (decimal)
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""

variable = 'ABC'
num = 1000
float_num = 1234.5678

print(f"--- Básico: s, d, f ---")
# O Python geralmente detecta sozinho, mas você pode forçar.
print(f"String normal: {variable:s}") 
print(f"Inteiro: {num:d}")
print(f"Float (padrão): {float_num:f}") # Padrão costuma ser 6 casas decimais

print(f"\n--- Controle de Casas Decimais (.nf) ---")
# Muito usado para dinheiro. O .2f diz: "Quero 2 casas após o ponto, Float".
# Ele arredonda automaticamente (5678 vira 57).
print(f"Duas casas: {float_num:.2f}") 
print(f"Uma casa: {float_num:.1f}")

print(f"\n--- Alinhamento e Preenchimento (Padding) ---")
# Sintaxe: :[caractere_preenchimento][alinhamento][largura_total]
# < Esquerda | > Direita | ^ Centro

print(f"Esquerda (padrão texto): {variable:<10}.") # Ocupa 10 espaços, texto na esquerda
print(f"Direita (padrão num):   {variable:>10}.") # Ocupa 10 espaços, texto na direita
print(f"Centro:                 {variable:^10}.") # Ocupa 10 espaços, texto no meio

# Preenchendo com traços ou zeros
print(f"Preencher com -: {variable:-^10}") 
print(f"Preencher com 0: {num:0>10}") # Zeros à esquerda até ter 10 dígitos

print(f"\n--- Sinais (+ e -) e Separadores ---")
# O '+' força aparecer o sinal de mais em números positivos.
# A vírgula ',' coloca o separador de milhar (padrão americano).
print(f"Sinal forçado: {num:+}") 
print(f"Sinal forçado negativo: {-num:+}")
print(f"Separador de milhar: {1000000:,}") # Saída: 1,000,000
print(f"Separador + Float: {float_num:,.2f}") # Combinação poderosa!

print(f"\n--- Hexadecimal (x e X) ---")
# Base 16 (0-9 e A-F). Muito usado para cores (#FFFFFF) ou endereços de memória.
print(f"Hex minúsculo: {15:x}") # 15 em hex é 'f'
print(f"Hex maiúsculo: {255:X}") # 255 em hex é 'FF'
print(f"Hex com 4 dígitos: {255:04X}") # 00FF

print(f"\n--- Conversion Flags (!r, !s, !a) ---")
# !r chama o repr() -> Mostra como o objeto é para o desenvolvedor (com aspas)
# !s chama o str() -> Mostra como o objeto é para o usuário (sem aspas)

nome_com_aspas = "Fernando"
print(f"Normal (!s): {nome_com_aspas!s}")
print(f"Repr (!r):   {nome_com_aspas!r}") # Note que ele imprime as aspas em volta

print(f"\n--- Exemplo Complexo (O 'Tudo em Um') ---")
# Preenche com 0, Alinha a direita (>), Largura 10, separador milhar (,), 2 casas float (.2f)
print(f"Formatado: {float_num:0>10,.2f}")

print(f"\n--- Dica de Ouro (Debug Rápido) ---")
# Em vez de escrever f"num = {num}", basta usar o sinal de igual dentro da f-string.
# O Python imprime o nome da variável e o valor. Ajuda muito a não ter que decorar!
print(f"{num=}")
