"""
'flags' em Python são usadas para indicar condições booleanas, ou seja, verdadeiro (True) ou falso (False). Elas são frequentemente utilizadas em estruturas de controle de fluxo, como condicionais e loops, para determinar o caminho que o programa deve seguir com base em certas condições.
'is' e 'is not' são operadores de identidade em Python. Eles são usados para comparar se dois objetos são o mesmo objeto na memória, ou seja, se eles têm o mesmo ID.
'None' é um valor especial em Python que representa a ausência de valor ou um valor nulo. É comumente usado para indicar que uma variável não foi inicializada ou que uma função não retorna nenhum valor significativo.

"""

condicao_verdadeira = True
passou_no_if = None # Flag (Bandeira) - Inicializada como "Nada"

if condicao_verdadeira:
    passou_no_if = True # Ação: "Levantar a bandeira" (Sinalizar que passou aqui)
    print(f"Flag alterada! passou_no_if agora é {passou_no_if}")
else:
    print("Não passou no if")

# Verificando o estado da Flag
if passou_no_if is None:
    print("A flag continua None (não passou no if).")
elif passou_no_if is True:
    print("A flag é True (passou no if com sucesso).")

# --- DICA SENIOR: Diferença entre 'is' e '==' ---
# is -> Verifica IDENTIDADE (É o mesmo objeto na memória?)
# == -> Verifica VALOR (O conteúdo é igual?)

print(f"passou_no_if é None? {passou_no_if is None}") 
print(f"passou_no_if NÃO é None? {passou_no_if is not None}")