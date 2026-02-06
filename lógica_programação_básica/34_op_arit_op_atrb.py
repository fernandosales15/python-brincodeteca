"""

Operadores Aritméticos e de Atribuição - São usados para realizar operações matemáticas e atribuir valores a variáveis.
+= : Adiciona o valor à variável e atribui o resultado à variável.
-= : Subtrai o valor da variável e atribui o resultado à variável.
*= : Multiplica a variável pelo valor e atribui o resultado à variável.
/= : Divide a variável pelo valor e atribui o resultado à variável.
%= : Calcula o resto da divisão da variável pelo valor e atribui o resultado à variável.
**= : Eleva a variável à potência do valor e atribui o resultado à variável.
//=: Realiza a divisão inteira da variável pelo valor e atribui o resultado à variável.

Também funcionam com strings, onde o operador += é usado para concatenar strings.

"""

contador_zerado = 0

while contador_zerado < 100:
    print(f"Contador: {contador_zerado}")
    contador_zerado += 1 # Incrementa o contador em 1 a cada iteração.

    if contador_zerado == 50:
        print("Atingimos a metade do caminho, continuando...")

variavel_numerica_em_string = '1'
variavel_numerica_em_string += '0'
print(variavel_numerica_em_string)

# --- EXEMPLOS PRÁTICOS DOS OUTROS OPERADORES (DICA SENIOR) ---

saldo = 1000
print(f"Saldo Inicial: {saldo}")

saldo -= 200 # Subtração: 1000 - 200 = 800
print(f"Após compra (-= 200): {saldo}")

saldo *= 1.5 # Multiplicação: 800 * 1.5 = 1200.0
print(f"Após rendimento (*= 1.5): {saldo}")

saldo /= 4 # Divisão: 1200.0 / 4 = 300.0 (Note que vira float)
print(f"Após divisão de bens (/= 4): {saldo}")

numero_potencia = 2
numero_potencia **= 10 # Potência: 2 elevado a 10
print(f"2 elevado a 10 (**= 10): {numero_potencia}")

resto_divisao = 10
resto_divisao %= 3 # Módulo: Resto de 10 dividido por 3
print(f"Resto de 10 / 3 (%= 3): {resto_divisao}")