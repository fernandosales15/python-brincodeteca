"""
Break e Continue são palavras-chave usadas para controlar o fluxo de loops (while, for) em Python.
- Break: Encerra o loop imediatamente, saindo dele completamente.
- Continue: Pula a iteração atual do loop e passa para a próxima iteração.

"""

contador_de_numeros = 0

while contador_de_numeros <= 120:
    contador_de_numeros += 1 # DICA SENIOR: Incrementamos ANTES para evitar loop infinito com continue

    if contador_de_numeros == 75:
        print(f"--> Pulei a impressão do número {contador_de_numeros} usando continue.")
        continue # Pula a iteração atual quando o contador atingir 75.

    if contador_de_numeros == 100:
        print("Contador atingiu o número 100, saindo do loop.")
        break # Encerra o loop quando o contador atingir 100.

    # O print vem aqui embaixo. Se o 'continue' for acionado acima, esta linha NUNCA será lida.
    print(f"Contador: {contador_de_numeros}")