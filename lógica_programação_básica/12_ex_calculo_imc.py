# ... São 'Ellipsis' (reticências) usadas para indicar que um bloco de código está incompleto

nome_completo = 'Fernando Sales'
altura_metros = 1.70
peso_kg = 80
imc = peso_kg / (altura_metros * altura_metros)

print(f"O Analista {nome_completo} possui {altura_metros}, de altura")
print(f"e pesa {peso_kg} kg, portanto seu IMC é de {imc:.2f}" )

print(" ------- IMPRESSÃO DE MODO DIFERENTE ------- ")
print(nome_completo, "possui", altura_metros, "de altura, ")
print("e pesa", peso_kg, "kg, portanto seu IMC é de:", imc)
print(" ------- FIM DO PROGRAMA ------- ")