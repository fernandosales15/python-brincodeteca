#Operadores Lógicos: not - Inverte o valor lógico de uma expressão.

print(not True) #Resulta em 'False' no console. 
print(not False) #Resulta em 'True' no console.


senha_digitada = input("Digite a Senha: ")

#Se a senha digitada for diferente de "Senha123", o acesso será negado. Senha não for True
if not senha_digitada == "Senha123": 
    print("Acesso Negado! Senha Incorreta.")
else: 
    print("Acesso Permitido! Bem-vindo ao Sistema.")

# --- DICA SENIOR: O Poder do 'not' com valores vazios ---
# Em Python, strings vazias "", o número 0, e listas vazias [] são considerados "False" (Falsy).
# Usamos o 'not' para verificar se algo ESTÁ VAZIO de forma elegante.

if not senha_digitada:
    print("Atenção: Você não digitou nada no campo de senha!")