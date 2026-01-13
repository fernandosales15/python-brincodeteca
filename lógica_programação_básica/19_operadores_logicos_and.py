# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

# Definindo constantes para as credenciais (Boas Práticas: Evitar "Magic Strings" no meio da lógica)
USUARIO_CORRETO = "Nandos"
SENHA_CORRETA = "1234"

login = input("Digite o seu username: ")
senha = input("Digite a sua senha: ")

if login == USUARIO_CORRETO and senha == SENHA_CORRETA: #AND - Ambas as condições precisam ser verdadeiras
    print(f"Acesso Permitido - Bem vindo {login}!")
else:
    print("Acesso Negado! - Unknown User ou Incorrect Password")

print(True and False and False) #Irá parar a operação no 'False' e retornar false.

print(bool(" ")) #Retorna 'True', pois existe um valor preenchido, o espaço em branco.
print(bool("")) #Retorna 'False', pois a string está vazia.
print(0 and True) #Retorna 0, pois é o primeiro valor falsy
print(0.0 and True) #Retorna 0.0, pois é o primeiro valor falsy
