"""
Exercício de Calculadora

"""

while True:
    print("\n--- Nova Operação ---")
    try:
        primeiro_numero = float(input("Digite o primeiro número: "))
        segundo_numero = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: Você precisa digitar um número válido.")
        continue # Volta para o início do loop

    operador = input("Digite o tipo de Operação Desejada (+, -, *, /): ")

    if len(operador) > 1:
        print("Digite apenas um operador. ")
        continue


    # Lógica de cálculo
    if operador == "+":
        resultado = primeiro_numero + segundo_numero
        print(f"Resultado: {primeiro_numero} + {segundo_numero} = {resultado}")

    elif operador == "-":
        resultado = primeiro_numero - segundo_numero
        print(f"Resultado: {primeiro_numero} - {segundo_numero} = {resultado}")

    elif operador == "*":
        resultado = primeiro_numero * segundo_numero
        print(f"Resultado: {primeiro_numero} * {segundo_numero} = {resultado}")

    elif operador == "/":
        if segundo_numero != 0:
            resultado = primeiro_numero / segundo_numero
            print(f"Resultado: {primeiro_numero} / {segundo_numero} = {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    else:
        print("Operador inválido.")

    # Verificação de saída
    sair = input("\nDeseja sair? [s]im: ").lower()
    if sair.startswith("s"):
        print("Encerrando a calculadora.")
        break