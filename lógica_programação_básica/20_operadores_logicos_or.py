# Operadores lógicos 'OR' 

login_entrada = input("Digite [E]ntrar ou [S]air: ")
senha_entrada = input("Digite a sua senha numerica: ") 
# Dica Senior: Evite converter input para int() imediatamente se não for fazer cálculos matemáticos.
# Se o usuário digitar letras, o programa quebraria. É mais seguro comparar strings.

# Usando o parenteses para deixar claro a precedência das operações.
if (login_entrada == 'E' or login_entrada == 'e') and senha_entrada == '1234':
    print("Acesso Permitido - Bem vindo!")

else: 
    print("Acesso Negado! - Unknown User ou Incorrect Password")

# --- CONCEITOS AVANÇADOS (SENIOR LEVEL) ---

# 1. Avaliação de Curto-Circuito (Short-Circuit)
# O Python é "preguiçoso" (eficiente). No 'or', se o primeiro valor for True,
# ele NEM CHECA o segundo.
print(True or False) # Retorna True imediatamente.
print(0 or False or "Fernando" or True) # Vai imprimir "Fernando", pois é o primeiro "Verdadeiro".

# 2. Idioma Pythonico: Definindo valores padrão (Default Values)
# Isso é muito usado em configurações de software!

senha_digitada = input("Digite uma senha (ou deixe vazio para usar a padrão): ")

# Se a senha_digitada for vazia (Falsy), o 'or' assume o próximo valor.
senha_final = senha_digitada or "123456" 

print(f"A senha que será usada no sistema é: {senha_final}")