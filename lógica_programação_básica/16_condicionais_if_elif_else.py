#if, elif, else 
#se, senão se, senão


print("---- INÍCIO DO PROGRAMA ----")

cargo = input("Digite o seu cargo no Nubank: ").strip() 

if cargo == "IC3":
    print("Você é um Associate Software Engineer.")
elif cargo == "IC4":
    print("Você é um Software Engineer.") 
elif cargo == "IC5":
    print ("Você é um Senior Software Engineer.")
else: 
    print("Você é um Lead Software Engineer ou outro cargo.")

print("---- FIM DO PROGRAMA ----")

condicao_primeira = True 

# O if verifica se o que vem a seguir é "Verdadeiro" (True).
# Como a variável 'condicao_primeira' já vale True, não precisamos fazer 'if condicao_primeira == True'.
if condicao_primeira:
    print("A primeira condição é verdadeira.")

condicao_segunda = False

if not condicao_segunda:
    print("Isso foi impresso porque condicao_segunda é False e usamos 'not'.")
