# 'f-strings' são strings formatadas, por exemplo o ':.2f' formata para duas casas decimais

nome_sobrenome = "Fernando Sales"
empresa_que_trabalha = "Nubank"
cargo_atual = "Ombudsman Senior Analyst"
cargo_desejado = "Associate Software Engineer"
anos_de_empresa_atual = 6.7
anos_necessarios_para_migrar = 7.0

print(f"O {nome_sobrenome}, atualmente trabalha no {empresa_que_trabalha} como {cargo_atual}.")
print(f"Ele deseja migrar para Tech e ser {cargo_desejado}.")
print(f"Entretanto, ele está atualmente com {anos_de_empresa_atual:.1f} anos de empresa, ")
print(f"e precisa completar {anos_necessarios_para_migrar:.1f} anos para poder migrar. ")