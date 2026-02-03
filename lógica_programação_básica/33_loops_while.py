"""
Loops (Repetições) - while
Repete o código enquanto a condição for verdadeira (True).

"""

print("-" * 10 + "INICIANDO O LOOP" + "-" * 10)

condicao_numerica = 1000

while condicao_numerica >= 0:
    print(f"Atualmente o número é {condicao_numerica}")
    condicao_numerica -= 1 #Reduz o valor da variável em 1 a cada iteração.

    if condicao_numerica == 1:
        print("Finalizando o loop...")
        break #Encerra o loop quando a condição for atendida.)

print("-" * 10 + "LOOP FINALIZADO" + "-" * 10)

condicao_texto = True

while condicao_texto:
    nome = input("Digite o seu nome (ou 'sair' para encerrar): ")

    # Verificamos PRIMEIRO se é para sair
    if nome.lower() == "sair": 
        print("Encerrando o Loop...")
        break
    
    print(f"Olá, {nome} você está preso em um loop eterno, até que digite sair.")