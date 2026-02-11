"""
'While'dentro de 'while'
Um while alinhado, é uma repetição dentro de outra. 

"""

quantidade_linhas = 0
quantidade_colunas = 0

# NÍVEL 0: Raiz do código
while quantidade_linhas <= 5:
   # NÍVEL 1: Dentro do primeiro while (Loop Externo)
    print(f"--- Iniciando a Linha: {quantidade_linhas} ---")

    while quantidade_colunas <= quantidade_linhas:
        # NÍVEL 2: Dentro do segundo while (Loop Interno)
        print(f"  -> Coluna {quantidade_colunas} da Linha {quantidade_linhas}")
        quantidade_colunas += 1 # Incrementa a coluna
    
    # VOLTA AO NÍVEL 1: Fora do while interno, mas ainda dentro do externo
    quantidade_colunas = 0 # Resetamos a coluna para a próxima linha começar do zero
    quantidade_linhas += 1 # Passamos para a próxima linha