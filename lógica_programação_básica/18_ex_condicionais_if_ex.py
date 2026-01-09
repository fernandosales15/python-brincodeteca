# Exercício 2 - Sobre Condicionais e If / Elif / Else em Python.

print(" ---- Exercício 2 - Condicionais If / Elif / Else ---- ")
print(" ---- INICIANDO O PROGRAMA ---- ") 

primeiro_valor = int(input("Digite o 1º valor: "))
print(" ---- Primeiro valor registrado com sucesso ---- ")

segundo_valor = int(input("Digite o 2º valor: "))
print(" ---- Segundo valor registrado com sucesso ---- ") 

print(" --- CONTINUANDO O PROGRAMA --- ")
print(" ---- ANALISANDO OS VALORES E FAZENDO AS COMPARAÇÕES ---- ") 

if primeiro_valor > segundo_valor:
    print(f"O 1º valor registrado na variável 'primeiro_valor' = {primeiro_valor} é maior que o 2º valor registrado na variável 'segundo_valor' = {segundo_valor}.")
elif primeiro_valor == segundo_valor:
    print(f"O 1º valor registrado na variável 'primeiro_valor' = {primeiro_valor} é igual ao 2º valor da variável 'segundo_valor' = {segundo_valor}.")
else:
    print(f"O 2º valor registrado na variável 'segundo_valor' = {segundo_valor} é maior que o 1º valor registrado na variável 'primeiro_valor' = {primeiro_valor}.")

print(" ---- PROGRAMA FINALIZADO - ATÉ A PRÓXIMA! ---- ")
